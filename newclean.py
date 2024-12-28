import os
import json
import logging
import asyncio
import aiohttp
from datetime import datetime
from typing import List, Dict
from tqdm import tqdm

# Configuration
API_KEY = "6b88c45717cb464ead0aab7bf924b3d9"
ENDPOINT = "https://azure-open-ai-interface-developers.openai.azure.com"
DEPLOYMENT_NAME = "gpt-4o-mini"
API_VERSION = "2024-08-01-preview"
BATCH_SIZE = 50
RETRY_DELAY = 26

class AsyncDocumentProcessor:
    def __init__(self, json_path: str):
        self.json_path = json_path
        self.filtered_docs = []
        
    async def query_openai(self, session: aiohttp.ClientSession, batch: List[Dict], retry_count=0) -> List[bool]:
        while True:  # Keep retrying until successful or max retries reached
            try:
                batch_content = "\n\n".join([
                    f"Document {i+1}:\nTitle: {doc.get('title', '')}\nSummary: {doc.get('summary', '')}"
                    for i, doc in enumerate(batch)
                ])

                messages = [
                    {
                        "role": "system",
                        "content": "You are a document classifier. For each document, respond with 'Relevant' or 'Irrelevant' on a new line."
                    },
                    {
                        "role": "user",
                        "content": f"""Analyze if each document discusses: reimbursements, claims, disputes, fees, pricing, FBA, shipments, lost items, damaged items, inventory management, tax compliance, Seller Flex, Safe-T claims, or product listings.\n\n{batch_content}"""
                    }
                ]

                url = f"{ENDPOINT}/openai/deployments/{DEPLOYMENT_NAME}/chat/completions?api-version={API_VERSION}"
                
                async with session.post(
                    url,
                    json={
                        "messages": messages,
                        "max_tokens": 100,
                        "temperature": 0,
                        "top_p": 1
                    },
                    headers={
                        "api-key": API_KEY,
                        "Content-Type": "application/json"
                    }
                ) as response:
                    if response.status == 429:
                        if retry_count >= 3:
                            print(f"Max retries ({retry_count}) reached, skipping batch")
                            return [False] * len(batch)
                            
                        retry_count += 1
                        print(f"Rate limit hit, waiting {RETRY_DELAY} seconds... (retry {retry_count}/3)")
                        await asyncio.sleep(RETRY_DELAY)
                        continue  # Retry the request
                        
                    response_json = await response.json()
                    
                    if response.status != 200:
                        print(f"Error {response.status}: {response_json}")
                        return [False] * len(batch)
                        
                    responses = response_json['choices'][0]['message']['content'].strip().split('\n')
                    return [r.strip().lower() == 'relevant' for r in responses]

            except Exception as e:
                print(f"Error in API call: {str(e)}")
                if retry_count >= 3:
                    return [False] * len(batch)
                retry_count += 1
                print(f"Retrying after error... (retry {retry_count}/3)")
                await asyncio.sleep(RETRY_DELAY)

    async def process_documents(self) -> List[Dict]:
        try:
            with open(self.json_path, 'r', encoding='utf-8') as f:
                json_data = json.load(f)

            documents = [
                {
                    "path": path,
                    "title": doc_info.get("name", ""),
                    "summary": doc_info.get("description", ""),
                    "url": doc_info.get("url", ""),
                }
                for path, doc_info in json_data.get("documents", {}).items()
            ]

            print(f"\nProcessing {len(documents)} documents in batches of {BATCH_SIZE}")

            batches = [documents[i:i + BATCH_SIZE] 
                      for i in range(0, len(documents), BATCH_SIZE)]

            async with aiohttp.ClientSession() as session:
                processed_docs = []
                pbar = tqdm(total=len(batches), desc="Processing batches")
                
                for i, batch in enumerate(batches):
                    print(f"\nProcessing batch {i+1}/{len(batches)}")
                    # Wait RETRY_DELAY seconds between batches
                    if i > 0:
                        print(f"Waiting {RETRY_DELAY} seconds before next batch...")
                        await asyncio.sleep(RETRY_DELAY)
                        
                    results = await self.query_openai(session, batch)
                    
                    # Add relevant documents to processed list
                    relevant_docs = [doc for doc, is_relevant in zip(batch, results) if is_relevant]
                    processed_docs.extend(relevant_docs)
                    print(f"Found {len(relevant_docs)} relevant documents in this batch")
                    
                    # Save progress after each batch
                    with open("filtered_documents_prod_new.json", "w", encoding="utf-8") as f:
                        json.dump(processed_docs, f, ensure_ascii=False, indent=4)
                        
                    pbar.update(1)
                    
                pbar.close()
                self.filtered_docs = processed_docs

            return self.filtered_docs

        except Exception as e:
            print(f"Error processing documents: {str(e)}")
            return []

    async def process_batch(self, session: aiohttp.ClientSession, batch: List[Dict]) -> List[bool]:
        return await self.query_openai(session, batch)

async def main():
    processor = AsyncDocumentProcessor("/home/dumball/Downloads/interface-qa-bot-main/amazon_help_pages_us_prod/document_summaries.json")
    start_time = datetime.now()
    
    relevant_docs = await processor.process_documents()
    
    duration = datetime.now() - start_time
    print(f"\nProcessed {len(relevant_docs)} relevant documents in {duration.total_seconds():.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())