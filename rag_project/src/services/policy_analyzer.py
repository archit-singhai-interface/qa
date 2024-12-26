import os
import json
import logging
from concurrent.futures import ThreadPoolExecutor
from typing import List, Optional

from langchain_community.chat_models import ChatOpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter

from ..config.settings import Settings
from ..utils.logging_config import setup_logging

logger = setup_logging(__name__)

class PolicyAnalyzer:
    """
    Analyzes policy documents, creates summaries, and manages document metadata.
    """
    def __init__(self, policies_dir: Optional[str] = None):
        """
        Initialize PolicyAnalyzer with policies directory.
        
        Args:
            policies_dir (str, optional): Path to policy documents directory
        """
        self.policies_dir = policies_dir or Settings.POLICIES_DIR
        self.summaries = {}
        self.selected_docs = []
        self.summaries_file = os.path.join(
            os.path.dirname(self.policies_dir), 
            "document_summaries.json"
        )
        self.executor = ThreadPoolExecutor(max_workers=10)
        logger.info(f"Initialized PolicyAnalyzer with directory: {self.policies_dir}")

    def load_stored_summaries(self):
        """
        Load previously stored document summaries.
        
        Returns:
            dict: Loaded summaries or empty dict
        """
        try:
            if os.path.exists(self.summaries_file):
                with open(self.summaries_file, 'r') as f:
                    self.summaries = json.load(f)
                logger.info(f"Loaded {len(self.summaries)} stored summaries")
            return self.summaries
        except Exception as e:
            logger.error(f"Error loading summaries: {e}")
            return {}

    def store_summaries(self):
        """
        Store document summaries to JSON file.
        """
        try:
            os.makedirs(os.path.dirname(self.summaries_file), exist_ok=True)
            with open(self.summaries_file, 'w') as f:
                json.dump(self.summaries, f, indent=2)
            logger.info(f"Stored {len(self.summaries)} document summaries")
        except Exception as e:
            logger.error(f"Error storing summaries: {e}")

    def get_document_summary(self, file_path: str, max_lines: int = 5) -> str:
        """
        Extract summary from a markdown document.
        
        Args:
            file_path (str): Path to the document
            max_lines (int, optional): Maximum number of lines to summarize
        
        Returns:
            str: Document summary
        """
        try:
            with open(file_path, 'r') as f:
                lines = f.readlines()[:max_lines]
                summary = ''.join(lines).strip()
            return summary
        except Exception as e:
            logger.error(f"Error getting summary for {file_path}: {e}")
            return ""

    def analyze_documents(self) -> List[str]:
        """
        Analyze all markdown documents in the policies directory.
        
        Returns:
            List[str]: List of analyzed document paths
        """
        markdown_files = [
            os.path.join(root, file)
            for root, _, files in os.walk(self.policies_dir)
            for file in files if file.endswith('.md')
        ]
        
        logger.info(f"Found {len(markdown_files)} markdown files")
        
        # Analyze documents concurrently
        for file_path in markdown_files:
            summary = self.get_document_summary(file_path)
            self.summaries[file_path] = summary
        
        self.store_summaries()
        logger.info(f"Completed analysis of {len(markdown_files)} documents")
        
        return markdown_files

    def analyze_document_relevance(
        self, 
        file_path: str, 
        summary: str, 
        query: str, 
        llm: Optional[ChatOpenAI] = None
    ) -> float:
        """
        Analyze the relevance of a single document to a query.
        
        Args:
            file_path (str): Path to the document
            summary (str): Document summary
            query (str): Query to evaluate relevance against
            llm (ChatOpenAI, optional): Language model for relevance assessment
        
        Returns:
            float: Relevance score (0-1)
        """
        if not llm:
            llm = ChatOpenAI(temperature=0.1)
        
        try:
            # Implement relevance scoring logic
            # This is a placeholder - you might want to use more sophisticated methods
            return 0.5  # Default relevance
        except Exception as e:
            logger.error(f"Error analyzing document relevance: {e}")
            return 0.0

    def select_relevant_documents(self, query: str) -> List[str]:
        """
        Select relevant documents based on query and summaries.
        
        Args:
            query (str): Query to find relevant documents for
        
        Returns:
            List[str]: Paths of relevant documents
        """
        llm = ChatOpenAI(temperature=0.1)
        
        # Score document relevance
        relevance_scores = {
            doc_path: self.analyze_document_relevance(doc_path, summary, query, llm)
            for doc_path, summary in self.summaries.items()
        }
        
        # Sort and select top documents
        self.selected_docs = sorted(
            relevance_scores, 
            key=relevance_scores.get, 
            reverse=True
        )[:5]  # Select top 5 most relevant documents
        
        logger.info(f"Selected {len(self.selected_docs)} relevant documents")
        return self.selected_docs
