import asyncio
import os
import sys
from typing import List, Dict

# Ensure the parent directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Set Langsmith environment variables before importing
os.environ['LANGCHAIN_TRACING_V2'] = 'true'
os.environ['LANGCHAIN_ENDPOINT'] = 'https://api.smith.langchain.com'
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGSMITH_API_KEY', '')

from rag import RAGBot

async def run_retrieval_evaluation():
    """
    Run comprehensive retrieval system evaluation.
    
    This function demonstrates how to use the evaluate_retrieval method
    with sample test queries and ground truth data.
    """
    # Determine the policies directory 
    # Adjust this path to match your project structure
    policies_dir = os.path.join(os.path.dirname(__file__), 'policies')
    
    # Ensure the policies directory exists
    if not os.path.exists(policies_dir):
        print(f"Error: Policies directory not found at {policies_dir}")
        print("Please create a 'policies' directory with markdown files.")
        return
    
    # Initialize RAGBot with policies directory
    try:
        rag_bot = RAGBot(policies_dir)
    except ValueError as e:
        print(f"Configuration Error: {e}")
        print("Please set OPENAI_API_KEY in your environment variables.")
        return
    
    # Sample test queries
    test_queries = [
        {'query': 'What is the company policy on remote work?'},
        {'query': 'Explain the benefits package'},
        {'query': 'Describe the professional development opportunities'}
    ]
    
    # Sample ground truth (optional, for more detailed evaluation)
    ground_truth = [
        {
            'documents': [
                'policies/remote_work_policy.md',
                'policies/work_flexibility.md'
            ]
        },
        {
            'documents': [
                'policies/benefits_overview.md',
                'policies/employee_compensation.md'
            ]
        },
        {
            'documents': [
                'policies/professional_development.md',
                'policies/career_growth.md'
            ]
        }
    ]
    
    # Run evaluation
    try:
        # Ensure vector store is created
        await rag_bot.initialize()  
        
        # Run retrieval evaluation
        evaluation_results = await rag_bot.evaluate_retrieval(
            test_queries, 
            ground_truth
        )
        
        # Print detailed evaluation results
        print("\n--- Retrieval Evaluation Results ---")
        print("\nOverall Metrics:")
        for metric, value in evaluation_results['overall_metrics'].items():
            print(f"{metric}: {value:.4f}")
        
        print("\nQuery-level Details:")
        for query_result in evaluation_results['queries']:
            print(f"\nQuery: {query_result['query']}")
            print(f"Precision: {query_result['precision']:.4f}")
            print(f"Recall: {query_result['recall']:.4f}")
            print(f"Relevance Score: {query_result['relevance_score']:.4f}")
            print("Retrieved Documents:")
            for doc in query_result['retrieved_docs']:
                print(f"  - {doc['path']}: {doc['content']}")
    
    except Exception as e:
        print(f"Evaluation Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    # Use asyncio to run the async function
    asyncio.run(run_retrieval_evaluation())