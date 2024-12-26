from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Any
import os
from dotenv import load_dotenv
from agent import AmazonSellerAgent
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Validate environment variables
required_vars = [
    'AZURE_OPENAI_ENGINE',
    'AZURE_OPENAI_ENDPOINT',
    'AZURE_OPENAI_API_KEY',
    'AZURE_OPENAI_API_VERSION'
]

missing_vars = [var for var in required_vars if not os.getenv(var)]
if missing_vars:
    raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize the agent
docs_path = os.path.join(os.path.dirname(__file__), "amazon_help_pages_us")
seller_agent = AmazonSellerAgent(docs_path=docs_path)

class Question(BaseModel):
    text: str

class AgentResponse(BaseModel):
    answer: str
    thought_process: List[str]
    tools_used: List[str]

@app.post("/seller/ask", response_model=AgentResponse)
async def ask_seller_question(question: Question):
    """Endpoint to ask questions about Amazon Seller documentation"""
    logger.info(f"Received question: {question.text}")
    
    try:
        logger.info("Processing question through agent")
        result = await seller_agent.think_and_respond(question.text)
        
        logger.info("Successfully processed question")
        return AgentResponse(
            answer=result["answer"],
            thought_process=[ctx["thought"] for ctx in result["context"]],
            tools_used=[str(tool) for tool in result.get("sources", [])]
        )
    except Exception as e:
        logger.error(f"Error processing question: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=500, 
            detail={"error": str(e), "type": "ProcessingError"}
        )

# Add this at the bottom of the file
if __name__ == "__main__":
    import uvicorn
    
    logger.info("Starting API server...")
    config = uvicorn.Config(app, host="0.0.0.0", port=8000, log_level="info")
    server = uvicorn.Server(config)
    server.run()
