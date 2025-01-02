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
docs_path = os.path.join(os.path.dirname(__file__), "amazon_help_pages_us_prod")
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
        
        # Log the result for debugging
        logger.debug(f"Agent response: {result}")
        
        # Get the answer from the result
        answer = result.get("text", "No answer was generated")
        
        # Extract thought process from context
        thought_process = []
        if "context" in result:
            thought_process = [
                ctx.get("thought", "") 
                for ctx in result["context"] 
                if isinstance(ctx, dict) and ctx.get("thought")
            ]
        
        # Extract content as tools used
        tools_used = []
        if "content" in result:
            tools_used = [
                str(content) 
                for content in result["content"] 
                if content
            ]
        
        logger.info("Successfully processed question")
        logger.debug(f"Returning answer: {answer[:100]}...")  # Log first 100 chars of answer
        
        return AgentResponse(
            answer=answer,
            thought_process=thought_process or ["Direct response without intermediate steps"],
            tools_used=tools_used or ["No additional context used"]
        )
    except Exception as e:
        logger.error(f"Error processing question: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=500, 
            detail={"error": str(e), "type": "ProcessingError"}
        )

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# Add this at the bottom of the file
if __name__ == "__main__":
    import uvicorn
    
    logger.info("Starting API server...")
    config = uvicorn.Config(app, host="0.0.0.0", port=8000, log_level="info")
    server = uvicorn.Server(config)
    server.run()
