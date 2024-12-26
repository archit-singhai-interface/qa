import os
import asyncio
from dotenv import load_dotenv

from .config.settings import Settings
from .services.rag_bot import RAGBot
from .utils.logging_config import setup_logging
from .utils.error_handlers import log_and_handle_exception

# Setup logging
logger = setup_logging(__name__)

@log_and_handle_exception
async def main():
    """
    Main application entry point for RAG Bot.
    """
    # Load environment variables
    load_dotenv()
    
    # Validate configuration
    Settings.validate_config()
    
    # Initialize RAG Bot
    logger.info("Initializing RAG Bot")
    rag_bot = RAGBot()
    
    # Initialize bot
    await rag_bot.initialize()
    
    # Example queries
    test_queries = [
        'What is the policy for incorrect weight and dimensions?',
        'Explain the Amazon Seller Flex account suspension policy',
        'What are the reimbursement policies for fulfillment centers?'
    ]
    
    # Add ground truth if available
    ground_truth = [
        {'documents': ['server/bot/data/policies/Amazon Seller Flex - Incorrect Weight and Dimensions Policy.md']},
        {'documents': ['server/bot/data/policies/Amazon Seller Flex - Account Suspension Policy.md']},
        {'documents': ['server/bot/data/policies/FBA-FC reimbursement rate of damaged product and grade-based reimbursement.md']}
    ]
    
    # Demonstrate comprehensive evaluation
    try:
        evaluation_results = await rag_bot.comprehensive_rag_evaluation(test_queries, ground_truth)
        
        # Print evaluation results
        logger.info("\n--- Comprehensive RAG Evaluation Results ---")
        logger.info("\nOverall Metrics:")
        for metric, value in evaluation_results.overall_metrics.items():
            logger.info(f"{metric}: {value:.4f}")
        
        # Detailed query evaluations
        logger.info("\nQuery-level Evaluations:")
        for query_eval in evaluation_results.query_evaluations:
            logger.info(f"\nQuery: {query_eval.query}")
            logger.info("Metrics:")
            for metric, value in query_eval.metrics.items():
                logger.info(f"  {metric}: {value:.4f}")
            
            logger.info("\nRetrieved Documents:")
            for doc in query_eval.retrieved_docs:
                logger.info(f"  - {doc['path']}: {doc['content'][:200]}...")
    
    except Exception as e:
        logger.error(f"Evaluation error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    asyncio.run(main())
