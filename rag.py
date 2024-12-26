from dataclasses import dataclass
import logging
import json
from datetime import datetime
import asyncio
from concurrent.futures import ThreadPoolExecutor
from functools import partial
from pydantic import BaseModel, Field
from pydantic_ai import Agent, RunContext

import os
import glob
from typing import List, Dict, Any
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQA, LLMChain
from langchain.prompts import PromptTemplate
from langchain.docstore.document import Document
from langsmith import traceable, Client
import httpx

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),  # Add console output
        logging.FileHandler('rag_bot.log', encoding='utf-8')  # Optional: log to file
    ]
)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)  # Ensure INFO and above are logged

class DatabaseConn:
    """This is a fake database for example purposes.

    In reality, you'd be connecting to an external database
    (e.g. PostgreSQL) to get information about customers.
    """

    @classmethod
    async def customer_name(cls, *, id: int) -> str | None:
        if id == 123:
            return 'John'

    @classmethod
    async def customer_balance(cls, *, id: int, include_pending: bool) -> float:
        return 123.45
   


class SupportDependencies:
    customer_id: int
    db: DatabaseConn


class SupportResult(BaseModel):
    support_advice: str = Field(description='Advice returned to the customer')
    block_card: bool = Field(description="Whether to block the customer's card")
    risk: int = Field(description='Risk level of query', ge=0, le=10)


class PolicyAnalyzer:
    def __init__(self, policies_dir: str):
        self.policies_dir = policies_dir
        self.summaries = {}
        self.selected_docs = []
        self.summaries_file = os.path.join(policies_dir, "document_summaries.json")
        self.executor = ThreadPoolExecutor(max_workers=10)
        logger.info(f"Initialized PolicyAnalyzer with directory: {policies_dir}")

    def load_stored_summaries(self) -> Dict[str, Dict]:
        """Load previously stored summaries if they exist."""
        if os.path.exists(self.summaries_file):
            try:
                with open(self.summaries_file, 'r', encoding='utf-8') as f:
                    stored_data = json.load(f)
                logger.info(f"Loaded {len(stored_data)} stored summaries")
                return stored_data
            except Exception as e:
                logger.error(f"Error loading stored summaries: {str(e)}")
        return {}

    def store_summaries(self):
        """Store summaries with metadata."""
        summary_data = {
            'last_updated': datetime.now().isoformat(),
            'documents': {}
        }

        for file_path, summary in self.summaries.items():
            doc_name = os.path.basename(file_path)
            summary_data['documents'][file_path] = {
                'name': doc_name,
                'summary': summary,
                'size': os.path.getsize(file_path),
                'last_modified': datetime.fromtimestamp(os.path.getmtime(file_path)).isoformat()
            }

        try:
            with open(self.summaries_file, 'w', encoding='utf-8') as f:
                json.dump(summary_data, f, indent=2)
            logger.info(f"Stored {len(self.summaries)} document summaries to {self.summaries_file}")
        except Exception as e:
            logger.error(f"Error storing summaries: {str(e)}")

    def get_document_summary(self, file_path: str, max_lines: int = 5) -> str:
        """Get the first few lines of a markdown document as a summary."""
        logger.debug(f"Getting summary for file: {os.path.basename(file_path)}")
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = []
                for i, line in enumerate(f):
                    if i >= max_lines:
                        break
                    if line.strip():  # Skip empty lines
                        lines.append(line.strip())
                summary = ' '.join(lines)
                logger.debug(f"Generated summary ({len(summary)} chars): {summary[:100]}...")
                return summary
        except Exception as e:
            logger.error(f"Error reading file {file_path}: {str(e)}")
            return f"Error reading file: {str(e)}"

    async def context_relavance(self, file_path: str) -> str:
        """Get the contextual relavance and summary of the document"""
        stored_data = self.load_stored_summaries()
        


        

        

    async def analyze_documents(self) -> Dict[str, str]:
        """Analyze all markdown documents in hierarchical directory structure."""
        logger.info("Starting document analysis...")

        # First, try to load stored summaries
        stored_data = self.load_stored_summaries()

        # Recursively find all markdown files in the directory structure
        md_files = []
        for root, _, files in os.walk(self.policies_dir):
            for file in files:
                if file.endswith('.md'):
                    md_files.append(os.path.join(root, file))

        logger.info(f"Found {len(md_files)} markdown files in directory structure")

        # Process files concurrently
        async def process_file(file_path):
            doc_info = stored_data.get('documents', {}).get(file_path, {})
            file_mtime = datetime.fromtimestamp(os.path.getmtime(file_path)).isoformat()

            if not doc_info or doc_info.get('last_modified') != file_mtime:
                logger.debug(f"Generating new summary for modified/new file: {os.path.basename(file_path)}")
                return file_path, self.get_document_summary(file_path)
            else:
                logger.debug(f"Using stored summary for: {os.path.basename(file_path)}")
                return file_path, doc_info['summary']

        # Create tasks for all files
        tasks = [asyncio.create_task(process_file(file_path)) for file_path in md_files]
        results = await asyncio.gather(*tasks)

        # Update summaries dictionary
        self.summaries.update(dict(results))

        # Store updated summaries
        self.store_summaries()

        logger.info(f"Completed analysis of {len(self.summaries)} documents")
        return self.summaries


    async def analyze_document_relevance(self, file_path: str, summary: str, query: str, llm: ChatOpenAI) -> tuple:
        """Analyze relevance of a single document."""
        logger.debug(f"Analyzing relevance of: {os.path.basename(file_path)}")
        # messages = 
        
       # context_relavance = ""
        prompt = f"""Given the user query: "{query}"
        And this document summary: "{summary}"
        Rate the relevance of this document to the query on a scale of 1-10.
        Return only the number."""

        response = await llm.ainvoke(prompt)
        relevance_score = int(response.content.strip())
        logger.debug(f"Relevance score for {os.path.basename(file_path)}: {relevance_score}")
        
        return {'file_path': file_path, 'relevance_score': relevance_score, 'reasoning': response.content}

    async def select_relevant_documents(self, query: str) -> List[str]:
        """
        Select relevant documents based on query and summaries using concurrent processing.
        """
        logger.info(f"Selecting relevant documents for query: {query}")
        
        # Create OpenAI client without custom callbacks
        llm = ChatOpenAI(
            model_name="gpt-4o-mini", 
            temperature=0
        )
        logger.info("Initialized ChatOpenAI for relevance analysis")

        # Prepare all markdown files in the policies directory
        policy_files = glob.glob(os.path.join(self.policies_dir, "**/*.md"), recursive=True)
        logger.info(f"Total policy documents found: {len(policy_files)}")

        # Detailed logging of all policy files
        logger.info("Policy Documents List:")
        for file_path in policy_files:
            logger.info(f"- {os.path.basename(file_path)}")

        # Analyze relevance of documents concurrently
        relevance_tasks = []
        for file_path in policy_files:
            # Get document summary
            summary = self.get_document_summary(file_path)
            
            # Create task for relevance analysis
            task = asyncio.create_task(
                self.analyze_document_relevance(file_path, summary, query, llm)
            )
            relevance_tasks.append(task)
        
        # Wait for all relevance analysis tasks to complete
        relevance_results = await asyncio.gather(*relevance_tasks)
        
        # Filter and sort relevant documents
        relevant_docs = [
            result['file_path'] 
            for result in relevance_results 
            if result['relevance_score'] > 5  # Adjust threshold as needed
        ]
        
        # Detailed logging of retrieved relevant documents
        logger.info(f"Total relevant documents retrieved: {len(relevant_docs)}")
        logger.info("Relevant Documents:")
        for doc_path in relevant_docs:
            # Log document name and its relevance details
            doc_name = os.path.basename(doc_path)
            doc_details = next(
                (result for result in relevance_results if result['file_path'] == doc_path), 
                None
            )
            
            if doc_details:
                logger.info(f"- {doc_name} (Relevance Score: {doc_details['relevance_score']:.2f})")
                logger.info(f"  Reasoning: {doc_details.get('reasoning', 'No reasoning available')}")

        return relevant_docs


class RAGBot:
    def __init__(self, policies_dir: str, model_name: str = "gpt-4o-mini"):
        """
        Initialize RAGBot with policies directory.
        
        Args:
            policies_dir (str): Path to the directory containing policy documents
        """
        # Initialize logging
        self.logger = logging.getLogger(__name__)
        
        # Initialize language model
        self.llm = ChatOpenAI(
            model_name=model_name,  # or another appropriate model
            temperature=0.1,  # low temperature for more deterministic responses
            max_tokens=1000
        )
        
        # Initialize document analyzer
        self.analyzer = PolicyAnalyzer(policies_dir)
        self.vector_store = None
        self.qa_chain = None
        
        # Langsmith configuration with robust setup
        try:
            # Retrieve Langsmith API key
            langsmith_api_key = os.getenv('LANGSMITH_API_KEY', '')
            
            # Only configure if API key is present
            if langsmith_api_key:
                # Set Langsmith environment variables
                os.environ['LANGCHAIN_TRACING_V2'] = 'true'
                os.environ['LANGCHAIN_ENDPOINT'] = 'https://api.smith.langchain.com'
                os.environ['LANGCHAIN_API_KEY'] = langsmith_api_key
                
                # Import Client here to avoid import errors
                from langsmith import Client
                
                # Initialize Langsmith client
                self.langsmith_client = Client()
                logger.info("Langsmith tracing enabled successfully")
            else:
                logger.warning("Langsmith API key not found. Tracing will be disabled.")
                self.langsmith_client = None
        except ImportError:
            logger.error("Langsmith package not installed. Tracing disabled.")
            self.langsmith_client = None
        except Exception as e:
            logger.error(f"Error configuring Langsmith: {e}")
            self.langsmith_client = None
        
        # Validate OpenAI API key
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables")
        logger.info(f"Using OpenAI API key: {api_key[:6]}...{api_key[-4:]}")
        logger.info(f"Initialized RAGBot with model: {model_name}")

    async def initialize(self):
        """Initialize the RAG bot by analyzing documents and creating the vector store."""
        logger.info("Initializing RAGBot...")
        
        try:
            # First analyze all documents
            await self.analyzer.analyze_documents()
            
            # Get selected documents - use all documents if none are selected by relevance
            selected_docs = await self.analyzer.select_relevant_documents("")
            if not selected_docs:
                logger.warning("No documents selected by relevance, using all available documents")
                selected_docs = glob.glob(os.path.join(self.analyzer.policies_dir, "**/*.md"), recursive=True)
            
            if not selected_docs:
                raise ValueError("No documents found in the specified directory")
            
            # Load and process documents
            documents = await self.load_selected_documents(selected_docs)
            if not documents:
                raise ValueError("No content could be loaded from the selected documents")
            
            # Create vector store
            logger.info(f"Creating vector store with {len(documents)} documents")
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=200,
                length_function=len,
            )
            
            # Run text splitting in executor to avoid blocking
            loop = asyncio.get_event_loop()
            texts = await loop.run_in_executor(None, text_splitter.split_documents, documents)
            
            if not texts:
                raise ValueError("No text chunks created from documents")
            
            # Initialize embeddings
            embeddings = OpenAIEmbeddings()
            
            # Create vector store
            self.vector_store = await loop.run_in_executor(
                None, 
                lambda: FAISS.from_documents(texts, embeddings)
            )
            
            logger.info("RAGBot initialization complete")
            
        except Exception as e:
            logger.error(f"Failed to initialize RAGBot: {str(e)}")
            raise RuntimeError(f"RAGBot initialization failed: {str(e)}") from e

    async def load_selected_documents(self, selected_docs: List[str]) -> List[Document]:
        """Load selected documents concurrently."""
        logger.info(f"Loading {len(selected_docs)} selected documents")
        
        async def load_document(file_path: str) -> List[Document]:
            try:
                logger.debug(f"Loading document: {os.path.basename(file_path)}")
                loop = asyncio.get_event_loop()
                loader = TextLoader(file_path, encoding='utf-8')
                docs = await loop.run_in_executor(None, loader.load)
                logger.debug(f"Loaded {len(docs)} segments from {os.path.basename(file_path)}")
                return docs
            except Exception as e:
                logger.error(f"Error loading {file_path}: {str(e)}")
                return []

        # Create tasks for concurrent document loading
        tasks = [asyncio.create_task(load_document(file_path)) for file_path in selected_docs]
        doc_lists = await asyncio.gather(*tasks)
        
        # Flatten the list of document lists
        documents = [doc for doc_list in doc_lists for doc in doc_list]
        logger.info(f"Successfully loaded {len(documents)} document segments")
        return documents

    async def ask(self, question: str) -> dict:
        """
        Ask a question using the RAG system with concurrent processing.
        
        This method is directly referenced in @[client/src/components/ChatUI.jsx]
        Specifically, it provides the data structure for the frontend chat interface.
        
        Expected response structure for @[client/src/components/ChatUI.jsx]:
        {
            "answer": str,           # Main response text
            "sources": List[str],    # Source document paths
            "content": List[str],    # Extracted content snippets
            "context": List[Dict],   # Detailed context information
            "relevant_docs": List[str]  # Relevant document paths
        }
        
        Args:
            question (str): The input question to process
        
        Returns:
            Dict: A dictionary containing the answer and relevant information
        """
        # Log the incoming question for @[client/src/components/ChatUI.jsx] tracking
        logger.info(f"RAG Query from ChatUI: {question}")
        
        try:
            # Ensure vector store is initialized for @[client/src/components/ChatUI.jsx] requests
            if self.vector_store is None:
                logger.info("Initializing vector store for ChatUI request")
                await self.initialize()
            
            # Select relevant documents for frontend display
            logger.info("Selecting documents for ChatUI")
            selected_docs = await self.analyzer.select_relevant_documents(question)
            logger.info(f"Found {len(selected_docs)} documents for ChatUI")
            
            # Prepare context for @[client/src/components/ChatUI.jsx] sources display
            context_docs = []
            for doc_path in selected_docs:
                try:
                    with open(doc_path, 'r') as f:
                        context_docs.append({
                            'source': os.path.basename(doc_path),  # Used in ChatUI sources
                            'content': f.read()[:500]  # Snippet for ChatUI context
                        })
                except Exception as e:
                    logger.error(f"Error reading document for ChatUI: {doc_path} - {e}")
            
            # Perform RAG query for @[client/src/components/ChatUI.jsx]
            logger.info("Performing RAG query for ChatUI")
            retrieval_chain = RetrievalQA.from_chain_type(
                llm=self.llm, 
                chain_type="stuff", 
                retriever=self.vector_store.as_retriever(search_kwargs={"k": 3})
            )
            
            # Execute query for frontend
            result = retrieval_chain.invoke({"query": question})
            
            # Prepare response compatible with @[client/src/components/ChatUI.jsx]
            response = {
                "answer": result.get('result', ''),  # Main text for ChatUI
                "sources": selected_docs,  # Document sources
                "content": [doc['content'] for doc in context_docs],  # Content snippets
                "context": context_docs,  # Detailed context for ChatUI
                "relevant_docs": selected_docs  # Relevant document paths
            }
            
            logger.info("RAG query processed for ChatUI")
            return response
        
        except Exception as e:
            logger.error(f"ChatUI RAG Query Error: {e}", exc_info=True)
            raise

    @traceable
    async def evaluate_retrieval(self, test_queries: List[Dict[str, str]], ground_truth: List[Dict[str, List[str]]] = None):
        """
        Evaluate the retrieval system's performance.
        
        Args:
            test_queries (List[Dict[str, str]]): List of test queries with 'query' key
            ground_truth (List[Dict[str, List[str]]], optional): List of ground truth documents for each query
        
        Returns:
            Dict: Evaluation metrics including precision, recall, and relevance scores
        """
        # Ensure vector store is initialized
        if not self.vector_store:
            await self.initialize()
        
        # Create retriever
        retriever = self.vector_store.as_retriever(search_kwargs={"k": 4})
        
        # Evaluation metrics
        evaluation_results = {
            'queries': [],
            'overall_metrics': {
                'mean_precision': 0,
                'mean_recall': 0,
                'mean_relevance_score': 0
            }
        }
        
        # Process each query
        for idx, query_data in enumerate(test_queries):
            query = query_data['query']
            
            # Retrieve documents
            retrieved_docs = await asyncio.get_event_loop().run_in_executor(
                None, 
                retriever.get_relevant_documents, 
                query
            )
            
            # Prepare query evaluation
            query_eval = {
                'query': query,
                'retrieved_docs': [],
                'precision': 0,
                'recall': 0,
                'relevance_score': 0
            }
            
            # If ground truth is provided, calculate metrics
            if ground_truth and idx < len(ground_truth):
                gt_docs = ground_truth[idx].get('documents', [])
                
                # Precision: Proportion of retrieved documents that are relevant
                retrieved_doc_paths = [doc.metadata.get('source', '') for doc in retrieved_docs]
                
                # Precision: Proportion of retrieved documents that are relevant
                relevant_docs = [doc for doc in retrieved_doc_paths if doc in gt_docs]
                query_eval['precision'] = len(relevant_docs) / len(retrieved_doc_paths) if retrieved_doc_paths else 0
                
                # Recall: Proportion of relevant documents that were retrieved
                query_eval['recall'] = len(relevant_docs) / len(gt_docs) if gt_docs else 0
                
                # Relevance scoring using cosine similarity or another metric
                query_eval['relevance_score'] = self._calculate_relevance_score(retrieved_docs, gt_docs)
            
            # Store retrieved document details
            query_eval['retrieved_docs'] = [
                {
                    'path': doc.metadata.get('source', 'Unknown'),
                    'content': doc.page_content[:200] + '...' if len(doc.page_content) > 200 else doc.page_content
                } for doc in retrieved_docs
            ]
            
            evaluation_results['queries'].append(query_eval)
        
        # Calculate overall metrics
        if evaluation_results['queries']:
            evaluation_results['overall_metrics'] = {
                'mean_precision': sum(
                    query['precision'] for query in evaluation_results['queries']
                ) / len(evaluation_results['queries']),
                'mean_recall': sum(
                    query['recall'] for query in evaluation_results['queries']
                ) / len(evaluation_results['queries']),
                'mean_relevance_score': sum(
                    query['relevance_score'] for query in evaluation_results['queries']
                ) / len(evaluation_results['queries'])
            }
        
        return evaluation_results
    
    def _calculate_relevance_score(self, retrieved_docs, ground_truth_docs):
        """
        Calculate relevance score between retrieved and ground truth documents.
        
        Args:
            retrieved_docs (List): Documents retrieved by the system
            ground_truth_docs (List): Ground truth documents
        
        Returns:
            float: Relevance score
        """
        from sklearn.feature_extraction.text import TfidfVectorizer
        from sklearn.metrics.pairwise import cosine_similarity
        
        # Combine document contents
        retrieved_texts = [doc.page_content for doc in retrieved_docs]
        
        # If no ground truth, return 0
        if not ground_truth_docs:
            return 0
        
        # Vectorize documents
        vectorizer = TfidfVectorizer()
        try:
            # Combine retrieved and ground truth documents
            all_docs = retrieved_texts + ground_truth_docs
            tfidf_matrix = vectorizer.fit_transform(all_docs)
            
            # Calculate cosine similarity
            similarities = cosine_similarity(
                tfidf_matrix[:len(retrieved_texts)], 
                tfidf_matrix[len(retrieved_texts):]
            )
            
            # Return average max similarity
            return float(similarities.max(axis=1).mean())
        except Exception as e:
            logger.error(f"Relevance score calculation error: {e}")
            return 0

    @traceable
    async def comprehensive_rag_evaluation(self, test_queries: List[str], ground_truth: List[Dict[str, Any]] = None):
        """
        Perform a comprehensive evaluation of the RAG system with multiple metrics.
        
        Args:
            test_queries (List[str]): List of test queries
            ground_truth (List[Dict[str, Any]], optional): Ground truth data for evaluation
        
        Returns:
            Dict: Comprehensive evaluation metrics
        """
        # Validate input
        if not isinstance(test_queries, list):
            raise ValueError("test_queries must be a list of strings")
        
        # Ensure vector store is initialized with documents
        if not self.vector_store:
            # Analyze documents first
            await self.initialize()
            
            # Load selected documents
            selected_docs = self.analyzer.selected_docs
            documents = await self.load_selected_documents(selected_docs)
            
            # Create vector store
            logger.info("Creating vector store")
            loop = asyncio.get_event_loop()
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=200,
                length_function=len,
            )
            texts = await loop.run_in_executor(None, text_splitter.split_documents, documents)
            embeddings = OpenAIEmbeddings()
            self.vector_store = await loop.run_in_executor(
                None, 
                lambda: FAISS.from_documents(texts, embeddings)
            )
            logger.info("Vector store creation complete")
        
        # Prepare evaluation results
        evaluation_results = {
            'query_evaluations': [],
            'overall_metrics': {
                'retrieval_precision': 0,
                'retrieval_recall': 0,
                'answer_relevance': 0,
                'answer_factuality': 0,
                'context_diversity': 0
            }
        }
        
        # Process each query
        for idx, query in enumerate(test_queries):
            # Retrieve documents
            retriever = self.vector_store.as_retriever(search_kwargs={"k": 4})
            retrieved_docs = await asyncio.get_event_loop().run_in_executor(
                None, 
                retriever.get_relevant_documents, 
                query
            )
            
            # Prepare query evaluation
            query_eval = {
                'query': query,
                'retrieved_docs': [],
                'metrics': {
                    'retrieval_precision': 0,
                    'retrieval_recall': 0,
                    'context_relevance': 0,
                    'context_diversity': 0
                }
            }
            
            # Evaluate retrieved documents
            if ground_truth and idx < len(ground_truth):
                gt_docs = ground_truth[idx].get('documents', [])
                
                # Retrieval Precision: Proportion of retrieved docs that are relevant
                retrieved_doc_paths = [doc.metadata.get('source', '') for doc in retrieved_docs]
                relevant_docs = [doc for doc in retrieved_doc_paths if doc in gt_docs]
                query_eval['metrics']['retrieval_precision'] = len(relevant_docs) / len(retrieved_doc_paths) if retrieved_doc_paths else 0
                
                # Retrieval Recall: Proportion of relevant docs retrieved
                query_eval['metrics']['retrieval_recall'] = len(relevant_docs) / len(gt_docs) if gt_docs else 0
            
            # Context Diversity Evaluation
            context_texts = [doc.page_content for doc in retrieved_docs]
            query_eval['metrics']['context_diversity'] = self._calculate_context_diversity(context_texts)
            
            # Generate answer using retrieved context
            qa_chain = RetrievalQA.from_chain_type(
                llm=self.llm,
                chain_type="stuff",
                retriever=retriever,
                return_source_documents=True,
            )
            
            # Evaluate answer
            try:
                response = await asyncio.get_event_loop().run_in_executor(
                    None, 
                    lambda: qa_chain({"query": query})
                )
                
                # Assess answer relevance and factuality
                answer_eval = self._evaluate_answer_quality(
                    query, 
                    response.get('result', ''), 
                    retrieved_docs
                )
                
                # Merge answer evaluation metrics
                query_eval['metrics'].update(answer_eval)
                
                # Store retrieved document details
                query_eval['retrieved_docs'] = [
                    {
                        'path': doc.metadata.get('source', 'Unknown'),
                        'content': doc.page_content[:200] + '...' if len(doc.page_content) > 200 else doc.page_content
                    } for doc in retrieved_docs
                ]
            except Exception as e:
                logger.error(f"Error evaluating query {query}: {e}")
            
            evaluation_results['query_evaluations'].append(query_eval)
        
        # Calculate overall metrics
        if evaluation_results['query_evaluations']:
            # Average metrics across queries
            evaluation_results['overall_metrics'] = {
                metric: sum(
                    query['metrics'].get(metric, 0) 
                    for query in evaluation_results['query_evaluations']
                ) / len(evaluation_results['query_evaluations'])
                for metric in evaluation_results['overall_metrics']
            }
        
        return evaluation_results
    
    def _calculate_context_diversity(self, context_texts: List[str], threshold: float = 0.3) -> float:
        """
        Calculate the diversity of retrieved context documents.
        
        Args:
            context_texts (List[str]): List of context document texts
            threshold (float): Cosine similarity threshold for considering texts different
        
        Returns:
            float: Context diversity score (0-1)
        """
        from sklearn.feature_extraction.text import TfidfVectorizer
        from sklearn.metrics.pairwise import cosine_similarity
        
        if len(context_texts) <= 1:
            return 1.0
        
        # Vectorize texts
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(context_texts)
        
        # Calculate pairwise cosine similarities
        similarities = cosine_similarity(tfidf_matrix)
        
        # Count unique contexts
        unique_contexts = 0
        for i in range(len(context_texts)):
            is_unique = True
            for j in range(i):
                if similarities[i, j] > threshold:
                    is_unique = False
                    break
            if is_unique:
                unique_contexts += 1
        
        return unique_contexts / len(context_texts)
    
    def _evaluate_answer_quality(self, query: str, answer: str, retrieved_docs: List[Document]) -> Dict[str, float]:
        """
        Evaluate the quality of the generated answer.
        
        Args:
            query (str): Original query
            answer (str): Generated answer
            retrieved_docs (List[Document]): Retrieved context documents
        
        Returns:
            Dict: Answer quality metrics
        """
        # Use the instance's LLM for advanced evaluation
        llm = self.llm
        
        # Relevance evaluation
        relevance_prompt = PromptTemplate(
            input_variables=["query", "answer", "context"],
            template="""Evaluate the relevance of the answer to the query based on the context.
            Query: {query}
            Context: {context}
            Answer: {answer}
            
            Provide a relevance score from 0-1, where:
            0 = Not relevant at all
            0.5 = Partially relevant
            1 = Highly relevant
            
            Score:"""
        )
        
        # Factuality evaluation
        factuality_prompt = PromptTemplate(
            input_variables=["context", "answer"],
            template="""Assess the factuality of the answer based on the given context.
            Context: {context}
            Answer: {answer}
            
            Provide a factuality score from 0-1, where:
            0 = Contains significant inaccuracies
            0.5 = Mostly accurate with some minor discrepancies
            1 = Completely factual and supported by the context
            
            Score:"""
        )
        
        try:
            # Prepare context
            context = "\n---\n".join([doc.page_content for doc in retrieved_docs])
            
            # Evaluate relevance
            relevance_chain = LLMChain(llm=llm, prompt=relevance_prompt)
            relevance_score = float(relevance_chain.run(
                query=query, 
                answer=answer, 
                context=context
            ))
            
            # Evaluate factuality
            factuality_chain = LLMChain(llm=llm, prompt=factuality_prompt)
            factuality_score = float(factuality_chain.run(
                context=context, 
                answer=answer
            ))
            
            return {
                'answer_relevance': relevance_score,
                'answer_factuality': factuality_score
            }
        except Exception as e:
            logger.error(f"Answer quality evaluation error: {e}")
            return {
                'answer_relevance': 0,
                'answer_factuality': 0
            }

class OpenAIRequestLogger:
    @staticmethod
    def log_request(request):
        """
        Log details of an outgoing request to OpenAI API
        
        Args:
            request (httpx.Request): The request being sent
        """
        try:
            # Attempt to decode the request body
            body = request.content.decode('utf-8') if request.content else ''
            
            # Parse the body if it's JSON
            try:
                body_json = json.loads(body)
            except (json.JSONDecodeError, TypeError):
                body_json = body
            
            # Log the request details
            logger.info("OpenAI API Request:")
            logger.info(f"URL: {request.url}")
            logger.info(f"Method: {request.method}")
            logger.info(f"Headers: {dict(request.headers)}")
            logger.info(f"Body: {json.dumps(body_json, indent=2)}")
        except Exception as e:
            logger.error(f"Error logging OpenAI request: {e}")

    @staticmethod
    def log_response(response):
        """
        Log details of an incoming response from OpenAI API
        
        Args:
            response (httpx.Response): The response received
        """
        try:
            # Attempt to decode the response body
            body = response.text
            
            # Parse the body if it's JSON
            try:
                body_json = json.loads(body)
            except (json.JSONDecodeError, TypeError):
                body_json = body
            
            # Log the response details
            logger.info("OpenAI API Response:")
            logger.info(f"Status Code: {response.status_code}")
            logger.info(f"Headers: {dict(response.headers)}")
            logger.info(f"Body: {json.dumps(body_json, indent=2)}")
        except Exception as e:
            logger.error(f"Error logging OpenAI response: {e}")

if __name__ == '__main__':
    import asyncio
    from dotenv import load_dotenv

    # Load and validate environment variables
    load_dotenv()
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in environment variables")
    print(f"\nUsing OpenAI API key: {api_key[:6]}...{api_key[-4:]}")

    async def main():
        logger.info("Starting main application")
        policies_dir = "amazon_help_pages_us"
        rag_bot = RAGBot(policies_dir=policies_dir)
        
        logger.info("Initializing RAG bot")
        await rag_bot.initialize()
        
        question = "How do I start selling on Amazon FBA"
        logger.info(f"Testing with question: {question}")
        
        result = await rag_bot.ask(question)
        logger.info("Got answer from RAG bot")
        
        print(f"\nQuestion: {question}")
        print("\nAnswer:", result["answer"])
        print("\nRelevant Documents:")
        for doc in result["relevant_docs"]:
            print(f"- {doc}")
        
        print("\nContext Used:")
        for i, ctx in enumerate(result["context"], 1):
            print(f"\n[Context {i}] From {ctx.get('source', 'Unknown Source')}:")
            print(ctx.get('content', 'No content available'))
            print("-" * 80)

        # Demonstrate comprehensive evaluation
        test_queries = [
            'What is the policy for incorrect weight and dimensions?',
            'Explain the Amazon Seller Flex account suspension policy',
            'What are the reimbursement policies for fulfillment centers?'
        ]
        
        # Add ground_truth parameter if needed
        ground_truth = [
            {'documents': ['server/bot/data/policies/Amazon Seller Flex - Incorrect Weight and Dimensions Policy.md']},
            {'documents': ['server/bot/data/policies/Amazon Seller Flex - Account Suspension Policy.md']},
            {'documents': ['server/bot/data/policies/FBA-FC reimbursement rate of damaged product and grade-based reimbursement.md']}
        ]
        
        # Run comprehensive evaluation
        try:
            evaluation_results = await rag_bot.comprehensive_rag_evaluation(test_queries, ground_truth)
            
            # Print evaluation results
            print("\n--- Comprehensive RAG Evaluation Results ---")
            print("\nOverall Metrics:")
            for metric, value in evaluation_results['overall_metrics'].items():
                print(f"{metric}: {value:.4f}")
            
            # Detailed query evaluations
            print("\nQuery-level Evaluations:")
            for query_eval in evaluation_results['query_evaluations']:
                print(f"\nQuery: {query_eval['query']}")
                print("Metrics:")
                for metric, value in query_eval['metrics'].items():
                    print(f"  {metric}: {value:.4f}")
                
                print("\nRetrieved Documents:")
                for doc in query_eval['retrieved_docs']:
                    print(f"  - {doc['path']}: {doc['content'][:200]}...")
        
        except Exception as e:
            print(f"Evaluation error: {e}")
            import traceback
            traceback.print_exc()

    asyncio.run(main())
