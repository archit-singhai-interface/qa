import os
import sys
from typing import List, Tuple

# Add the project root to Python path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_root)

from langchain_community.vectorstores import FAISS
from langchain_openai import AzureOpenAIEmbeddings, AzureOpenAI
from langchain.chains import RetrievalQA
from langchain.schema import Document
from dotenv import load_dotenv
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Load environment variables
load_dotenv()

# Initialize Azure OpenAI models
embeddings = AzureOpenAIEmbeddings(
    model=os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME"),
    api_key=os.getenv("AZURE_OPENAI_EMBEDDING_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_EMBEDDING_ENDPOINT"),
    api_version=os.getenv("AZURE_OPENAI_EMBEDDING_API_VERSION"),
)

llm = AzureOpenAI(
    deployment_name=os.getenv("AZURE_OPENAI_ENGINE"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    temperature=0.5,
    max_tokens=512,
)

# Sample text for demonstration
documents = [
    """
    Artificial Intelligence (AI) is the simulation of human intelligence by machines. 
    Machine Learning is a subset of AI that enables systems to learn from data.
    Deep Learning is a type of Machine Learning that uses neural networks with multiple layers.
    Natural Language Processing (NLP) is a branch of AI that helps machines understand human language.
    Computer Vision is the field of AI that enables machines to interpret visual information.
    """,
    """
    Retrieval Augmented Generation (RAG) combines the power of large language models with external knowledge retrieval.
    RAG helps improve accuracy and provides source attribution for generated responses.
    It works by first retrieving relevant documents from a knowledge base, then using them as context for generation.
    This approach helps reduce hallucinations and keeps responses grounded in factual information.
    """
]

def create_qa_chain(docs: List[str], k: int = 2):
    # Split text into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
        length_function=len,
    )
    chunks = text_splitter.create_documents(docs)
    
    # Create vector store
    vector_store = FAISS.from_documents(chunks, embeddings)
    
    # Create RAG chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vector_store.as_retriever(search_kwargs={"k": k}),
        return_source_documents=True,
    )
    return qa_chain

def ask_question(qa_chain, query: str) -> Tuple[str, List[Document]]:
    result = qa_chain.invoke({"query": query})
    return result["result"], result["source_documents"]

if __name__ == "__main__":
    # Create QA chain
    qa_chain = create_qa_chain(documents, k=2)
    
    # Example questions
    questions = [
        "What is artificial intelligence?",
        "How does RAG work?",
        "What are the benefits of using RAG?",
    ]
    
    # Ask questions
    for question in questions:
        print("\nQuestion:", question)
        answer, sources = ask_question(qa_chain, question)
        print("\nAnswer:", answer)
        print("\nSource Documents:")
        for i, doc in enumerate(sources, 1):
            print(f"\n{i}.", doc.page_content.strip())
        print("\n" + "="*80)
