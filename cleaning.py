import numpy as np
from pathlib import Path
import faiss
from typing import List, Tuple
from collections import defaultdict
import os
import json
import pickle
from tqdm import tqdm
from ratelimit import limits, sleep_and_retry
import google.generativeai as genai
from concurrent.futures import ThreadPoolExecutor
import threading
from sklearn.cluster import DBSCAN
import time
import backoff
import logging

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('document_processing.log'),
        # Removing StreamHandler to keep console clean
    ]
)
logger = logging.getLogger(__name__)

# Constants
EMBEDDINGS_CACHE_FILE = "document_embeddings.pkl"
DOCUMENT_MAP_FILE = "document_map.json"
MAX_REQUESTS_PER_MINUTE = 1500
RATE_LIMIT_PERIOD = 60
NUM_THREADS = 10
MAX_RETRIES = 5

# Thread-safe progress bar and logging
thread_lock = threading.Lock()
progress_bar = None

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

@backoff.on_exception(
    backoff.expo,
    (Exception),
    max_tries=MAX_RETRIES,
    max_time=300,
    on_backoff=lambda details: logger.warning(f"Backing off {details['wait']:0.1f} seconds after {details['tries']} tries"),
    giveup=lambda e: "Request payload size exceeds the limit" in str(e)  # Don't retry payload size errors
)
@sleep_and_retry
@limits(calls=MAX_REQUESTS_PER_MINUTE, period=RATE_LIMIT_PERIOD)
def get_embedding(text: str) -> np.ndarray:
    """Get embedding for a single text with rate limiting and retries."""
    try:
        logger.debug(f"Getting embedding for text of length {len(text)}")
        result = genai.embed_content(
            model="models/text-embedding-004",
            content=text
        )
        logger.debug("Successfully got embedding")
        return np.array(result['embedding'], dtype=np.float32)
    except Exception as e:
        logger.error(f"Error getting embedding: {str(e)}")
        raise

def chunk_text(text, max_bytes=10000):
    """Split text into chunks that are under the byte limit"""
    # Convert to bytes to get accurate byte count
    text_bytes = text.encode('utf-8')
    
    if len(text_bytes) <= max_bytes:
        return [text]
    
    # Split into sentences or paragraphs first
    chunks = []
    current_chunk = ""
    
    # You can adjust the splitting logic based on your needs
    for paragraph in text.split('\n\n'):
        paragraph_bytes = paragraph.encode('utf-8')
        
        if len(current_chunk.encode('utf-8')) + len(paragraph_bytes) < max_bytes:
            current_chunk += paragraph + '\n\n'
        else:
            if current_chunk:
                chunks.append(current_chunk.strip())
            current_chunk = paragraph + '\n\n'
    
    if current_chunk:
        chunks.append(current_chunk.strip())
    
    return chunks

def get_embeddings_for_text(text):
    """Get embeddings for text, chunking only if necessary"""
    # First check the text size
    text_bytes = len(text.encode('utf-8'))
    
    if text_bytes <= 10000:
        # Small enough to process directly
        try:
            return [get_embedding(text)]
        except Exception as e:
            logger.error(f"Failed to get embedding for text: {str(e)}")
            raise
    else:
        # Too large, needs chunking
        logger.info(f"Text size ({text_bytes} bytes) exceeds limit, chunking...")
        chunks = chunk_text(text)
        logger.info(f"Split into {len(chunks)} chunks")
        
        # Log size of each chunk
        for i, chunk in enumerate(chunks):
            chunk_size = len(chunk.encode('utf-8'))
            logger.info(f"Chunk {i+1}: {chunk_size} bytes")
        
        embeddings = []
        for i, chunk in enumerate(chunks):
            chunk_size = len(chunk.encode('utf-8'))
            logger.info(f"Processing chunk {i+1}/{len(chunks)} ({chunk_size} bytes)")
            try:
                embedding = get_embedding(chunk)
                embeddings.append(embedding)
            except Exception as e:
                logger.error(f"Failed to get embedding for chunk {i+1}: {str(e)}")
                raise
                
        return embeddings

def process_document(file_path: Path) -> Tuple[str, np.ndarray]:
    """Process a single document and return its path and embedding."""
    try:
        logger.info(f"Processing document: {file_path}")
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            content_size = len(content.encode('utf-8'))
            logger.info(f"Document size: {content_size} bytes")
            
            if content_size > 10000:
                logger.info(f"Document {file_path} requires chunking")
            
            # Get embeddings (might be multiple if document was chunked)
            embeddings = get_embeddings_for_text(content)
            
            # If we got multiple embeddings, average them
            if len(embeddings) > 1:
                logger.info(f"Averaging {len(embeddings)} embeddings for {file_path}")
                embedding = np.mean(embeddings, axis=0)
            else:
                embedding = embeddings[0]
            
            # Update progress bar thread-safely
            with thread_lock:
                progress_bar.update(1)
                current = progress_bar.n
                total = progress_bar.total
                logger.info(f"Processed {current}/{total} documents")
            
            return str(file_path), embedding
    except Exception as e:
        logger.error(f"Error processing {file_path}: {e}")
        return None

def load_or_create_embeddings(md_files: List[Path]) -> tuple:
    """Load cached embeddings or create new ones using multiple threads."""
    global progress_bar
    
    logger.info(f"Starting embedding process for {len(md_files)} files")
    
    if os.path.exists(EMBEDDINGS_CACHE_FILE) and os.path.exists(DOCUMENT_MAP_FILE):
        logger.info("Found cache files, attempting to load...")
        with open(EMBEDDINGS_CACHE_FILE, 'rb') as f:
            embeddings_array = pickle.load(f)
        with open(DOCUMENT_MAP_FILE, 'r') as f:
            document_map = json.load(f)
            
        # Verify if cache is valid
        current_files = {str(f) for f in md_files}
        cached_files = set(document_map['file_paths'])
        
        if current_files == cached_files:
            logger.info("Cache is valid, using cached embeddings")
            return embeddings_array, document_map['file_paths']
        else:
            logger.info("Cache is invalid, will create new embeddings")
    
    logger.info(f"Creating new embeddings using {NUM_THREADS} threads")
    
    # Initialize progress bar
    progress_bar = tqdm(total=len(md_files), desc="Processing documents")
    
    # Process documents using thread pool with smaller chunks
    results = []
    chunk_size = 50  # Reduced chunk size
    
    for i in range(0, len(md_files), chunk_size):
        chunk = md_files[i:i + chunk_size]
        logger.info(f"Processing chunk {i//chunk_size + 1}, files {i} to {min(i+chunk_size, len(md_files))}")
        
        with ThreadPoolExecutor(max_workers=NUM_THREADS) as executor:
            chunk_futures = [executor.submit(process_document, file_path) for file_path in chunk]
            chunk_results = []
            
            for future in chunk_futures:
                try:
                    result = future.result()
                    if result is not None:
                        chunk_results.append(result)
                except Exception as e:
                    logger.error(f"Future failed: {str(e)}")
            
            results.extend(chunk_results)
            logger.info(f"Completed chunk with {len(chunk_results)} successful embeddings")
        
        # Small delay between chunks
        logger.info("Sleeping between chunks")
        time.sleep(2)
    
    # Close progress bar
    progress_bar.close()
    
    if not results:
        logger.error("No documents were successfully processed")
        raise Exception("No documents were successfully processed")
    
    logger.info(f"Successfully processed {len(results)} documents")
    
    # Separate paths and embeddings
    file_paths, embeddings = zip(*results)
    embeddings_array = np.array(embeddings, dtype=np.float32)
    
    # Save embeddings and document map
    logger.info("Saving results to cache")
    with open(EMBEDDINGS_CACHE_FILE, 'wb') as f:
        pickle.dump(embeddings_array, f)
    with open(DOCUMENT_MAP_FILE, 'w') as f:
        json.dump({'file_paths': file_paths}, f)
    
    logger.info("Embedding process complete")
    return embeddings_array, file_paths

def analyze_document_clusters(eps: float = 0.3, min_samples: int = 2):
    """Cluster documents using Gemini embeddings and DBSCAN."""
    # Get all markdown files recursively
    base_path = Path("amazon_help_pages_us_prod")
    md_files = list(base_path.rglob("*.md"))
    
    # Load or create embeddings
    embeddings_array, file_paths = load_or_create_embeddings(md_files)
    
    # Normalize the vectors
    faiss.normalize_L2(embeddings_array)
    
    # Create and save FAISS index
    dimension = embeddings_array.shape[1]
    index = faiss.IndexFlatIP(dimension)
    index.add(embeddings_array)
    faiss.write_index(index, "document_index.faiss")
    
    # Perform DBSCAN clustering
    clustering = DBSCAN(eps=eps, min_samples=min_samples, metric='cosine')
    labels = clustering.fit_predict(embeddings_array)
    
    # Organize results
    clusters = defaultdict(list)
    for idx, label in enumerate(labels):
        clusters[label].append({
            'path': file_paths[idx],
            'vector': embeddings_array[idx]
        })
    
    # Write results to log file instead of printing
    logger.info(f"\nModel: text-embedding-004")
    logger.info(f"Vector dimension: {dimension}")
    logger.info(f"Total documents processed: {len(file_paths)}")
    logger.info(f"Found {len(clusters)-1} clusters and {len(clusters[-1])} outliers\n")
    
    # Log outliers
    logger.info("Outliers:")
    logger.info("=" * 80)
    for doc in sorted(clusters[-1], key=lambda x: x['path']):
        logger.info(f"📄 {doc['path']}")
    
    # Log clusters
    logger.info("\nClusters:")
    logger.info("=" * 80)
    for cluster_id in sorted(clusters.keys()):
        if cluster_id == -1:
            continue
        
        docs = clusters[cluster_id]
        logger.info(f"\nCluster {cluster_id} ({len(docs)} documents):")
        logger.info("-" * 80)
        
        sorted_docs = sorted(docs, key=lambda x: x['path'])
        for doc in sorted_docs:
            logger.info(f"📄 {doc['path']}")

if __name__ == "__main__":
    logger.info("Starting document clustering process")
    analyze_document_clusters(eps=0.15, min_samples=2)
    logger.info("Document clustering complete")