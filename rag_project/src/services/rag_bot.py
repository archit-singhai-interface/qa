import os
import asyncio
import logging
from typing import List, Dict, Any, Optional

from langchain_community.chat_models import ChatOpenAI
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_core.language_models import BaseLanguageModel
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA

from ..config.settings import Settings
from ..models.policy_models import PolicyEvaluationResult, RAGEvaluationResults
from .policy_analyzer import PolicyAnalyzer
from ..utils.logging_config import setup_logging
from ..utils.error_handlers import log_and_handle_exception

logger = setup_logging(__name__)

class RAGBot:
    """
    Retrieval Augmented Generation (RAG) Bot for policy analysis.
    """
    def __init__(
        self, 
        policies_dir: Optional[str] = None, 
        model_name: Optional[str] = None
    ):
        """
        Initialize RAGBot with policies directory and language model.
        
        Args:
            policies_dir (str, optional): Path to policy documents
            model_name (str, optional): OpenAI model name
        """
        # Initialize logging
        self.logger = logger
        
        # Initialize language model
        self.llm = ChatOpenAI(
            model_name=model_name or Settings.OPENAI_MODEL_NAME,
            temperature=0.1,
            max_tokens=1000
        )
        
        # Initialize document analyzer
        self.analyzer = PolicyAnalyzer(policies_dir)
        self.vector_store = None
        self.qa_chain = None
        
        # Configure Langsmith tracing
        self._configure_langsmith()

    def _configure_langsmith(self):
        """
        Configure Langsmith tracing if API key is available.
        """
        try:
            if Settings.LANGSMITH_API_KEY and Settings.LANGCHAIN_TRACING_V2 == 'true':
                os.environ['LANGCHAIN_TRACING_V2'] = 'true'
                os.environ['LANGCHAIN_ENDPOINT'] = Settings.LANGCHAIN_ENDPOINT
                os.environ['LANGCHAIN_API_KEY'] = Settings.LANGSMITH_API_KEY
                
                from langsmith import Client
                self.langsmith_client = Client()
                logger.info("Langsmith tracing enabled successfully")
            else:
                logger.warning("Langsmith tracing not configured")
                self.langsmith_client = None
        except Exception as e:
            logger.error(f"Error configuring Langsmith: {e}")
            self.langsmith_client = None

    async def initialize(self):
        """
        Initialize the RAG bot by analyzing documents and creating vector store.
        """
        # Analyze documents
        self.analyzer.analyze_documents()
        
        # Load selected documents
        selected_docs = self.analyzer.selected_docs
        documents = await self.load_selected_documents(selected_docs)
        
        # Create vector store
        logger.info("Creating vector store")
        loop = asyncio.get_event_loop()
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=Settings.TEXT_CHUNK_SIZE,
            chunk_overlap=Settings.TEXT_CHUNK_OVERLAP,
            length_function=len,
        )
        texts = await loop.run_in_executor(None, text_splitter.split_documents, documents)
        embeddings = OpenAIEmbeddings()
        self.vector_store = await loop.run_in_executor(
            None, 
            lambda: FAISS.from_documents(texts, embeddings)
        )
        logger.info("Vector store creation complete")

    async def load_selected_documents(self, selected_docs: List[str]) -> List[Document]:
        """
        Load selected documents concurrently.
        
        Args:
            selected_docs (List[str]): Paths to selected documents
        
        Returns:
            List[Document]: Loaded documents
        """
        async def load_document(file_path: str) -> Optional[Document]:
            try:
                with open(file_path, 'r') as f:
                    content = f.read()
                    return Document(page_content=content, metadata={'source': file_path})
            except Exception as e:
                logger.error(f"Error loading document {file_path}: {e}")
                return None

        # Load documents concurrently
        documents = await asyncio.gather(
            *[load_document(doc) for doc in selected_docs]
        )
        
        # Filter out None values
        return [doc for doc in documents if doc is not None]

    async def ask(self, question: str) -> Dict[str, Any]:
        """
        Ask a question using the RAG system with concurrent processing.
        
        Args:
            question (str): Query to ask
        
        Returns:
            Dict: Answer and context details
        """
        # Select relevant documents
        relevant_docs = self.analyzer.select_relevant_documents(question)
        
        # Load and process documents
        documents = await self.load_selected_documents(relevant_docs)
        
        # Create retriever
        retriever = self.vector_store.as_retriever(search_kwargs={"k": Settings.RETRIEVAL_TOP_K})
        
        # Create QA chain
        qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=retriever,
            return_source_documents=True,
        )
        
        # Generate answer
        response = await asyncio.get_event_loop().run_in_executor(
            None, 
            lambda: qa_chain({"query": question})
        )
        
        return {
            "answer": response.get('result', ''),
            "relevant_docs": relevant_docs,
            "context": [
                {
                    "source": doc.metadata.get('source', 'Unknown'),
                    "content": doc.page_content
                } for doc in response.get('source_documents', [])
            ]
        }

    @log_and_handle_exception
    async def comprehensive_rag_evaluation(
        self, 
        test_queries: List[str], 
        ground_truth: Optional[List[Dict[str, Any]]] = None
    ) -> RAGEvaluationResults:
        """
        Perform a comprehensive evaluation of the RAG system with multiple metrics.
        
        Args:
            test_queries (List[str]): List of test queries
            ground_truth (List[Dict[str, Any]], optional): Ground truth data for evaluation
        
        Returns:
            RAGEvaluationResults: Comprehensive evaluation results
        """
        # Ensure vector store is initialized
        if not self.vector_store:
            await self.initialize()
        
        # Initialize evaluation results
        evaluation_results = RAGEvaluationResults()
        
        # Process each query
        for idx, query in enumerate(test_queries):
            # Retrieve documents
            retriever = self.vector_store.as_retriever(search_kwargs={"k": Settings.RETRIEVAL_TOP_K})
            retrieved_docs = await asyncio.get_event_loop().run_in_executor(
                None, 
                retriever.get_relevant_documents, 
                query
            )
            
            # Prepare query evaluation
            query_eval = PolicyEvaluationResult(query=query)
            
            # Evaluate retrieved documents
            if ground_truth and idx < len(ground_truth):
                gt_docs = ground_truth[idx].get('documents', [])
                
                # Retrieval Precision: Proportion of retrieved docs that are relevant
                retrieved_doc_paths = [doc.metadata.get('source', '') for doc in retrieved_docs]
                relevant_docs = [doc for doc in retrieved_doc_paths if doc in gt_docs]
                query_eval.metrics['retrieval_precision'] = (
                    len(relevant_docs) / len(retrieved_doc_paths) 
                    if retrieved_doc_paths else 0
                )
                
                # Retrieval Recall: Proportion of relevant docs retrieved
                query_eval.metrics['retrieval_recall'] = (
                    len(relevant_docs) / len(gt_docs) 
                    if gt_docs else 0
                )
            
            # Context Diversity Evaluation
            context_texts = [doc.page_content for doc in retrieved_docs]
            query_eval.metrics['context_diversity'] = self._calculate_context_diversity(context_texts)
            
            # Generate answer
            qa_chain = RetrievalQA.from_chain_type(
                llm=self.llm,
                chain_type="stuff",
                retriever=retriever,
                return_source_documents=True,
            )
            
            try:
                response = await asyncio.get_event_loop().run_in_executor(
                    None, 
                    lambda: qa_chain({"query": query})
                )
                
                # Assess answer relevance and factuality
                answer_eval = self._evaluate_answer_quality(
                    query, 
                    response.get('result', ''), 
                    retrieved_docs
                )
                
                # Merge answer evaluation metrics
                query_eval.metrics.update(answer_eval)
                
                # Store retrieved document details
                query_eval.retrieved_docs = [
                    {
                        'path': doc.metadata.get('source', 'Unknown'),
                        'content': doc.page_content[:200] + '...' if len(doc.page_content) > 200 else doc.page_content
                    } for doc in retrieved_docs
                ]
            except Exception as e:
                logger.error(f"Error evaluating query {query}: {e}")
            
            # Add query evaluation to results
            evaluation_results.add_query_evaluation(query_eval)
        
        # Calculate overall metrics
        evaluation_results.calculate_overall_metrics()
        
        return evaluation_results

    def _calculate_context_diversity(
        self, 
        context_texts: List[str], 
        threshold: float = 0.3
    ) -> float:
        """
        Calculate the diversity of retrieved context documents.
        
        Args:
            context_texts (List[str]): List of context document texts
            threshold (float, optional): Cosine similarity threshold
        
        Returns:
            float: Context diversity score (0-1)
        """
        from sklearn.feature_extraction.text import TfidfVectorizer
        from sklearn.metrics.pairwise import cosine_similarity
        
        if len(context_texts) <= 1:
            return 1.0
        
        # Use TF-IDF vectorization
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(context_texts)
        
        # Calculate pairwise cosine similarities
        similarities = cosine_similarity(tfidf_matrix)
        
        # Count unique documents based on similarity threshold
        unique_docs = 1  # First document is always unique
        for i in range(1, len(context_texts)):
            is_unique = all(
                similarities[i, j] < threshold 
                for j in range(i)
            )
            if is_unique:
                unique_docs += 1
        
        return unique_docs / len(context_texts)

    def _evaluate_answer_quality(
        self, 
        query: str, 
        answer: str, 
        retrieved_docs: List[Document]
    ) -> Dict[str, float]:
        """
        Evaluate the quality of the generated answer.
        
        Args:
            query (str): Original query
            answer (str): Generated answer
            retrieved_docs (List[Document]): Retrieved context documents
        
        Returns:
            Dict: Answer quality metrics
        """
        # Placeholder implementation - replace with more sophisticated evaluation
        return {
            'answer_relevance': 0.7,  # Assume moderate relevance
            'answer_factuality': 0.6   # Assume moderate factuality
        }
