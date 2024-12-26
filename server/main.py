import os
import sys

# Add the project root to Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from server.bot.utils.schema import Question, Answer
from server.bot.main import QABot
from dotenv import load_dotenv
from markdown import markdown

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

bot = QABot()
load_dotenv()


@app.get("/")
def read_root():
    return {"message": "Welcome to the QA Bot API!"}


@app.post("/ask", response_model=Answer)
def ask_question(question: Question):
    """
    Ask a question to the bot and return the response
    :param question: User query
    :return: Answer to the user query from the bot
    """
    bot_response, metadata = bot.invoke(question.text)
    sources = list(set(doc.metadata["source"] for doc in metadata))
    markdown_files = [f"bot/data/policies/{source}.md" for source in sources]

    contents = []
    for file in markdown_files:
        try:
            with open(file, "r", encoding="utf-8") as f:
                markdown_content = f.read()
                contents.append(markdown(markdown_content))
        except FileNotFoundError:
            print(f"File not found: {file}")
        except Exception as e:
            print(f"Error reading {file}: {e}")

    return Answer(text=bot_response, sources=sources, content=contents)


@app.get("/health")
def health_check():
    return {"status": "healthy"}
