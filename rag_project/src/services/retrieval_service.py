from typing import List, Dict, Any
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

class RetrievalService:
    """
    Service for document retrieval and similarity search.
    """
    def __init__(self, documents: List[Document], embedding_model=None):
        """
        Initialize retrieval service with documents.
        
        Args:
            documents (List[Document]): List of documents to index
            embedding_model (Optional): Embedding model to use
        """
        self.embedding_model = embedding_model or OpenAIEmbeddings()
        self.vector_store = FAISS.from_documents(documents, self.embedding_model)

    def search(
        self, 
        query: str, 
        top_k: int = 4, 
        search_type: str = 'similarity'
    ) -> List[Dict[str, Any]]:
        """
        Perform document retrieval based on query.
        
        Args:
            query (str): Search query
            top_k (int, optional): Number of top results to return
            search_type (str, optional): Type of search (similarity, mmr)
        
        Returns:
            List[Dict[str, Any]]: Retrieved documents with metadata
        """
        if search_type == 'similarity':
            retriever = self.vector_store.as_retriever(search_kwargs={"k": top_k})
        elif search_type == 'mmr':
            retriever = self.vector_store.as_retriever(
                search_type="mmr", 
                search_kwargs={"k": top_k, "fetch_k": top_k * 2}
            )
        else:
            raise ValueError(f"Unsupported search type: {search_type}")
        
        # Retrieve documents
        docs = retriever.get_relevant_documents(query)
        
        return [
            {
                'content': doc.page_content,
                'source': doc.metadata.get('source', 'Unknown'),
                'metadata': doc.metadata
            } for doc in docs
        ]

    def add_documents(self, new_documents: List[Document]):
        """
        Add new documents to the vector store.
        
        Args:
            new_documents (List[Document]): Documents to add
        """
        self.vector_store.add_documents(new_documents)

    def save_local(self, path: str):
        """
        Save vector store locally.
        
        Args:
            path (str): Path to save vector store
        """
        self.vector_store.save_local(path)

    @classmethod
    def load_local(cls, path: str, embedding_model=None):
        """
        Load vector store from local path.
        
        Args:
            path (str): Path to load vector store from
            embedding_model (Optional): Embedding model to use
        
        Returns:
            RetrievalService: Initialized retrieval service
        """
        embedding_model = embedding_model or OpenAIEmbeddings()
        vector_store = FAISS.load_local(path, embedding_model)
        
        # Create a dummy retrieval service with the loaded vector store
        service = cls([])
        service.vector_store = vector_store
        return service
