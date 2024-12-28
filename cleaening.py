import cohere
import asyncio
import json
import logging
import time
from tqdm import tqdm
from cohere import ClassifyExample
import os
# Set up logging
logging.basicConfig(
    filename='document_filtering.log', 
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Update constants
JSON_PATH = "/home/dumball/Downloads/interface-qa-bot-main/amazon_help_pages_us_prod/document_summaries.json"
BATCH_SIZE = 20  # Process 20 documents per request
co = cohere.AsyncClient()

class DocumentProcessor:
    def __init__(self, json_path: str, batch_size=BATCH_SIZE):
        self.json_path = json_path
        self.batch_size = batch_size
        self.filtered_docs = []
        self.total_docs = 0
        self.processed_docs = 0
        self.output_file = "filtered_documents_prod_new2.json"
        self.checkpoint_file = "checkpoint.json"
        # Load existing progress if any
        self.load_checkpoint()
        # Define classification examples with exact documents
        self.examples = [
            # Reimbursements
            ClassifyExample(text="FBA inventory reimbursement policy", label="reimbursements"),
            ClassifyExample(text="Referral fees reimbursement policy", label="reimbursements"),
            ClassifyExample(text="FBA inventory reimbursement policy: Customer return claims", label="reimbursements"),
            
            # Disputes
            ClassifyExample(text="Cancellation fee and cancellation fee dispute process", label="disputes"),
            ClassifyExample(text="FBA inventory reimbursement policy: Removals claims", label="disputes"),
            
            # Fees
            ClassifyExample(text="FBA fees", label="fees"),
            ClassifyExample(text="FBA fulfillment fee", label="fees"),
            ClassifyExample(text="Referral fees", label="fees"),
            ClassifyExample(text="List of useful fee tools", label="fees"),
            
            # Pricing
            ClassifyExample(text="Pricing health", label="pricing"),
            ClassifyExample(text="Minimum and Maximum Price Validation", label="pricing"),
            ClassifyExample(text="Assign a Price - Price Feed Schema", label="pricing"),
            
            # FBA
            ClassifyExample(text="FBA inventory", label="fba"),
            ClassifyExample(text="Reconcile your shipment", label="fba"),
            ClassifyExample(text="Removal Shipment Detail Report", label="fba"),
            
            # Lost/Damaged
            ClassifyExample(text="FBA Damaged Inventory Ownership", label="lost damaged"),
            ClassifyExample(text="FBA Damaged Inventory Ownership terms and conditions", label="lost damaged"),
            
            # Inventory
            ClassifyExample(text="Inventory performance", label="inventory"),
            ClassifyExample(text="FBA Inventory report", label="inventory"),
            
            # Tax
            ClassifyExample(text="Tax Guidelines", label="tax"),
            ClassifyExample(text="Amazon Tax-Exemption Program", label="tax"),
            ClassifyExample(text="Seller Fee Tax Invoice", label="tax"),
            
            # Safe-T
            ClassifyExample(text="Service Safe-T claims", label="safe-t"),
            ClassifyExample(text="Reimbursement for seller-fulfilled network prepaid returns", label="safe-t"),
            ClassifyExample(text="Customer Service by Amazon refund reimbursement policy", label="safe-t"),
            
            # Listings
            ClassifyExample(text="Listing photos", label="listings"),
            ClassifyExample(text="SKU lists and pack lists", label="listings"),
            
            # Not Found (irrelevant)
            ClassifyExample(text="Password reset instructions", label="not found"),
            ClassifyExample(text="Account security settings", label="not found"),
            ClassifyExample(text="General seller guidelines", label="not found"),
            ClassifyExample(text="Brazil Instructions to sellers", label="not found")
        ]

    def load_checkpoint(self):
        """Load progress from checkpoint file."""
        try:
            if os.path.exists(self.output_file):
                with open(self.output_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.filtered_docs = data.get('relevant_documents', [])
                    self.processed_docs = data.get('total_processed', 0)
                print(f"\nResuming from checkpoint: {self.processed_docs} documents processed")
                print(f"Found {len(self.filtered_docs)} relevant documents from previous run")
        except Exception as e:
            print(f"Error loading checkpoint: {str(e)}")
            logging.error(f"Error loading checkpoint: {str(e)}")

    async def classify_batch(self, batch: list) -> list:
        """Classify a batch of documents using Cohere."""
        try:
            # Prepare inputs for classification
            inputs = [
                f"Title: {doc.get('title', '')}\nSummary: {doc.get('summary', '')}"
                for doc in batch
            ]

            response = await co.classify(
                inputs=inputs,
                examples=self.examples,
            )

            # Process results and save relevant documents
            relevant_docs = []
            for doc, classification in zip(batch, response.classifications):
                # Create a copy of the document with classification info
                doc_with_classification = {
                    "path": doc.get("path"),
                    "title": doc.get("title"),
                    "summary": doc.get("summary"),
                    "url": doc.get("url"),
                    "classification": {
                        "label": classification.prediction,
                        "confidence": classification.confidence,
                        "all_labels": {
                            label: conf.confidence 
                            for label, conf in classification.labels.items()
                        }
                    }
                }
                
                # Only save if it's not "not found"
                if classification.prediction != "not found":
                    relevant_docs.append(doc_with_classification)
                    if doc_with_classification not in self.filtered_docs:
                        self.filtered_docs.append(doc_with_classification)

            # Print detailed classification results
            print(f"\nBatch ID: {response.id}")
            for i, classification in enumerate(response.classifications):
                print(f"\nDocument {i+1} (ID: {classification.id}):")
                print(f"Title: {batch[i].get('title', '')}")
                print(f"Prediction: {classification.prediction}")
                print(f"Confidence: {classification.confidence:.4f}")
                print("Label confidences:")
                for label_name, label_data in classification.labels.items():
                    print(f"  {label_name}: {label_data.confidence:.4f}")

            # Save after each batch
            self.save_results()
            
            return [doc in relevant_docs for doc in batch]

        except Exception as e:
            logging.error(f"Error in classification: {str(e)}")
            print(f"Classification error: {str(e)}")
            return [False] * len(batch)

    def save_results(self):
        """Save current results to file."""
        try:
            output_data = {
                'total_processed': self.processed_docs,
                'total_relevant': len(self.filtered_docs),
                'relevant_documents': self.filtered_docs,
                'last_updated': time.strftime('%Y-%m-%d %H:%M:%S')
            }
            
            with open(self.output_file, "w", encoding="utf-8") as json_file:
                json.dump(output_data, json_file, ensure_ascii=False, indent=4)
            
            print(f"\nSaved {len(self.filtered_docs)} documents to {self.output_file}")
            print(f"Last processed document: {self.filtered_docs[-1]['title'] if self.filtered_docs else 'None'}")
            
        except Exception as e:
            print(f"Error saving results: {str(e)}")
            logging.error(f"Error saving results: {str(e)}")

    async def process_documents(self) -> list:
        """Process all documents from JSON with progress bar."""
        try:
            print(f"Attempting to read JSON file from: {self.json_path}")
            with open(self.json_path, 'r', encoding='utf-8') as f:
                json_data = json.load(f)
            
            # Extract documents from the nested structure
            documents = []
            for path, doc_info in json_data.get("documents", {}).items():
                doc = {
                    "path": path,
                    "title": doc_info.get("name", ""),
                    "summary": doc_info.get("description", ""),
                    "url": doc_info.get("url", ""),
                }
                documents.append(doc)
            
            print(f"Successfully loaded {len(documents)} documents")
            
            if not documents:
                print("Warning: No documents found in JSON file")
                return []

            self.total_docs = len(documents)

            # Skip already processed documents
            documents = documents[self.processed_docs:]
            if not documents:
                print("All documents have been processed already")
                return self.filtered_docs

            print(f"Remaining documents to process: {len(documents)}")

            # Create progress bar
            with tqdm(total=len(documents), desc="Processing documents", unit="doc") as pbar:
                # Process documents in batches
                for i in range(0, len(documents), self.batch_size):
                    batch = documents[i:i + self.batch_size]
                    results = await self.classify_batch(batch)
                    
                    # Process results
                    relevant_count = 0
                    for doc, is_relevant in zip(batch, results):
                        if is_relevant:
                            self.filtered_docs.append(doc)
                            relevant_count += 1
                            logging.info(f"Found relevant document: {doc.get('title', '')}")
                    
                    self.processed_docs += len(batch)
                    print(f"Found {relevant_count} relevant documents in this batch")
                    pbar.update(len(batch))
                    self.save_results()

            return self.filtered_docs

        except Exception as e:
            logging.error(f"Error processing documents: {str(e)}")
            print(f"Error processing documents: {str(e)}")
            return []

async def main():
    try:
        print("\nStarting document filtering...")
        print(f"Batch size: {BATCH_SIZE} documents")
        
        processor = DocumentProcessor(JSON_PATH)
        
        if not os.path.exists(JSON_PATH):
            print(f"Error: JSON file not found at {JSON_PATH}")
            return
            
        relevant_docs = await processor.process_documents()
        
        if relevant_docs:
            print(f"\nSuccess! Found {len(relevant_docs)} relevant documents out of {processor.total_docs} total documents")
            logging.info(f"Completed processing with {len(relevant_docs)} relevant documents")
        else:
            print("\nNo relevant documents were found")
            logging.warning("No relevant documents found")
            
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")
        logging.error(f"Main process error: {str(e)}")

if __name__ == "__main__":
    asyncio.run(main())