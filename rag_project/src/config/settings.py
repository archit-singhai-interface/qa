import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Settings:
    # OpenAI Configuration
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', '')
    OPENAI_MODEL_NAME = os.getenv('OPENAI_MODEL_NAME', 'gpt-4o-mini')
    
    # Langsmith Configuration
    LANGSMITH_API_KEY = os.getenv('LANGSMITH_API_KEY', '')
    LANGCHAIN_TRACING_V2 = os.getenv('LANGCHAIN_TRACING_V2', 'false')
    LANGCHAIN_ENDPOINT = os.getenv('LANGCHAIN_ENDPOINT', 'https://api.smith.langchain.com')
    
    # Project Paths
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    POLICIES_DIR = os.path.join(BASE_DIR, '..', 'data', 'policies')
    
    # Retrieval Configuration
    RETRIEVAL_TOP_K = 4
    TEXT_CHUNK_SIZE = 1000
    TEXT_CHUNK_OVERLAP = 200

    @classmethod
    def validate_config(cls):
        """Validate critical configuration settings."""
        if not cls.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY is not set")
        return True
