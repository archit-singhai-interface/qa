from typing import List, Optional
import os
from pathlib import Path
import glob

from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI

class QABot:
    def __init__(self, policies_dir: str, model_name: str = "gpt-3.5-turbo"):
        self.policies_dir = policies_dir
        self.model_name = model_name
        self.vector_store = None
        self.qa_chain = None
        
    def load_documents(self) -> List[str]:
        """Load all markdown documents from the policies directory."""
        documents = []
        md_files = glob.glob(os.path.join(self.policies_dir, "**/*.md"), recursive=True)
        
        for file_path in md_files:
            try:
                loader = UnstructuredMarkdownLoader(file_path)
                documents.extend(loader.load())
            except Exception as e:
                print(f"Error loading {file_path}: {str(e)}")
                
        return documents
    
    def initialize(self):
        """Initialize the QA bot by loading documents and creating the vector store."""
        # Load documents
        documents = self.load_documents()
        
        # Split documents into chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len,
        )
        texts = text_splitter.split_documents(documents)
        
        # Create vector store
        embeddings = OpenAIEmbeddings()
        self.vector_store = FAISS.from_documents(texts, embeddings)
        
        # Create QA chain
        llm = ChatOpenAI(model_name=self.model_name, temperature=0)
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=self.vector_store.as_retriever(
                search_kwargs={"k": 3}
            ),
        )
    
    def ask(self, question: str) -> str:
        """Ask a question to the QA bot."""
        if not self.qa_chain:
            raise ValueError("QA bot not initialized. Call initialize() first.")
        
        response = self.qa_chain.invoke({"query": question})
        return response["result"]
