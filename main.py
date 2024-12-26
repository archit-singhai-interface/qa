import os
import sys

# Add the project root directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from server.bot.utils.read_docs import load_markdowns
import uvicorn
from server.main import app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)