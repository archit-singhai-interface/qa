import os
import sys
from typing import List, Tuple

# Add the project root to Python path
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(project_root)

from langchain_community.vectorstores import FAISS
from langchain_openai import AzureOpenAIEmbeddings, AzureOpenAI
from langchain.chains import RetrievalQA
from langchain.schema import Document
from dotenv import load_dotenv
from server.bot.utils.read_docs import load_markdowns
from server.bot.utils.templates import PROMPT

load_dotenv()

API_KEY = "6b88c45717cb464ead0aab7bf924b3d9"

class QABot:
    def __init__(self, path: str = "bot/data/policies"):
        """
        Initialize the QABot
        :param path (str): Path to the folder containing PDFs. The default is "policies". It is required to
                           initialize local storage for the first time or if any updates
        """
        self.embeddings = AzureOpenAIEmbeddings(
            model=os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME"),
            api_key=os.getenv("AZURE_OPENAI_EMBEDDING_API_KEY"),
            azure_endpoint=os.getenv("AZURE_OPENAI_EMBEDDING_ENDPOINT"),
            api_version=os.getenv("AZURE_OPENAI_EMBEDDING_API_VERSION"),
        )
        self.llm = AzureOpenAI(
            deployment_name=os.getenv("AZURE_OPENAI_ENGINE"),
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
            temperature=0.5,
            max_tokens=512,
        )
        self.storage_path = "storage"
        if os.path.exists(self.storage_path):
            self.vector_store = FAISS.load_local(self.storage_path, embeddings=self.embeddings,
                                             allow_dangerous_deserialization=True)
        else:
            self.path = path
            self._embed_docs()

    def _embed_docs(self) -> None:
        """
        Embed the documents and save the vector store locally
        """
        documents = load_markdowns(self.path)
        print(documents)
        self.vector_store = FAISS.from_documents(documents, self.embeddings)
        self.vector_store.save_local(self.storage_path)

    def invoke(self, query: str, k: int = 2) -> Tuple[str, List[Document]]:
        """
        Invoke the QABot
        :param query: User query
        :param k: Number of documents to retrieve for context. The default is 2
        :return: Tuple of result string and list of source documents
        """
        qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            retriever=self.vector_store.as_retriever(search_kwargs={"k": k}),
            return_source_documents=True,
        )
        prompt = PROMPT.format(query=query)
        result = qa_chain.invoke({"query": prompt})
        return result["result"], result["source_documents"]



if __name__ == "__main__":
    user_query = "Explain FBA-FC Damaged Inventory Reimbursement Policy"
    bot = QABot()
    result, source_docs = bot.invoke(user_query, k=3)

    print(result)
    print("\nSource Documents:")
    for doc in source_docs:
        print(f"- {doc.metadata['source']}")
