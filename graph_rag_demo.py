import os
import sys
from typing import List, Dict, Set
import networkx as nx
from collections import defaultdict
import spacy
import numpy as np

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

# Initialize spaCy for NER and dependency parsing
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    os.system("python -m spacy download en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

class GraphRAG:
    def __init__(self):
        # Initialize Azure OpenAI
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
        
        # Initialize knowledge graph
        self.graph = nx.Graph()
        self.entity_docs = defaultdict(list)  # Maps entities to their document chunks
        
    def _extract_entities_and_relations(self, text: str) -> tuple[Set[str], List[tuple]]:
        """Extract entities and relations from text using spaCy"""
        doc = nlp(text)
        
        # Extract named entities and noun chunks
        entities = set()
        for ent in doc.ents:
            entities.add(ent.text.lower())
        for chunk in doc.noun_chunks:
            entities.add(chunk.text.lower())
            
        # Extract relations (simplified as co-occurrence in same sentence)
        relations = []
        for sent in doc.sents:
            sent_entities = set()
            for ent in sent.ents:
                sent_entities.add(ent.text.lower())
            for chunk in sent.noun_chunks:
                sent_entities.add(chunk.text.lower())
            
            # Create relations between all entities in the sentence
            sent_entities = list(sent_entities)
            for i in range(len(sent_entities)):
                for j in range(i + 1, len(sent_entities)):
                    relations.append((sent_entities[i], sent_entities[j]))
        
        return entities, relations

    def add_documents(self, documents: List[str]):
        """Process documents and build knowledge graph"""
        # Split documents into chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50,
            length_function=len,
        )
        doc_chunks = text_splitter.create_documents(documents)
        
        # Create vector store
        self.vector_store = FAISS.from_documents(doc_chunks, self.embeddings)
        
        # Build knowledge graph
        for chunk in doc_chunks:
            entities, relations = self._extract_entities_and_relations(chunk.page_content)
            
            # Add entities to graph
            for entity in entities:
                if entity not in self.graph:
                    self.graph.add_node(entity)
                self.entity_docs[entity].append(chunk)
            
            # Add relations to graph
            for rel in relations:
                self.graph.add_edge(rel[0], rel[1])
    
    def _get_related_entities(self, query: str, max_distance: int = 2) -> Set[str]:
        """Find entities in the graph related to the query entities"""
        query_entities, _ = self._extract_entities_and_relations(query)
        related_entities = set()
        
        for entity in query_entities:
            if entity in self.graph:
                # Get entities within max_distance steps
                for node in self.graph.nodes():
                    try:
                        distance = nx.shortest_path_length(self.graph, entity, node)
                        if distance <= max_distance:
                            related_entities.add(node)
                    except nx.NetworkXNoPath:
                        continue
        
        return related_entities

    def _enhance_retrieval(self, query: str, k: int = 3) -> List[Document]:
        """Enhance retrieval using both vector similarity and graph relationships"""
        # Get initial documents through vector similarity
        vector_docs = self.vector_store.similarity_search(query, k=k)
        
        # Get related entities from knowledge graph
        related_entities = self._get_related_entities(query)
        
        # Get documents containing related entities
        graph_docs = []
        for entity in related_entities:
            graph_docs.extend(self.entity_docs[entity])
        
        # Combine and deduplicate documents
        all_docs = vector_docs + graph_docs
        unique_docs = list({doc.page_content: doc for doc in all_docs}.values())
        
        # Return top k documents
        return unique_docs[:k]

    def query(self, query: str, k: int = 3) -> tuple[str, List[Document]]:
        """Query the graph-enhanced RAG system"""
        # Get enhanced retrieval results
        relevant_docs = self._enhance_retrieval(query, k)
        
        # Create QA chain
        qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            retriever=self.vector_store.as_retriever(search_kwargs={"k": k}),
            return_source_documents=True,
        )
        
        # Get answer
        result = qa_chain.invoke({"query": query})
        return result["result"], relevant_docs

# Example usage
if __name__ == "__main__":
    # Sample documents about a specific domain (e.g., computer science)
    documents = [
        """
        Python is a high-level programming language. Python supports object-oriented programming
        through classes and objects. Python was created by Guido van Rossum and was first released
        in 1991. Python's package manager pip helps in installing libraries.
        """,
        """
        Object-oriented programming (OOP) is a programming paradigm. OOP uses classes and objects
        to structure code. Classes are blueprints for objects, and objects are instances of classes.
        Java and Python both support object-oriented programming.
        """,
        """
        Guido van Rossum also developed the Python package manager pip. Pip makes it easy to
        install Python libraries and manage dependencies. Python's simplicity and readability
        were key goals for Guido van Rossum during its development.
        """
    ]
    
    # Initialize and build graph RAG
    graph_rag = GraphRAG()
    graph_rag.add_documents(documents)
    
    # Example queries
    queries = [
        "What is Python and who created it?",
        "How does object-oriented programming relate to Python?",
        "Tell me about pip and its relationship to Python.",
    ]
    
    # Run queries
    for query in queries:
        print("\nQuestion:", query)
        answer, sources = graph_rag.query(query)
        print("\nAnswer:", answer)
        print("\nSource Documents:")
        for i, doc in enumerate(sources, 1):
            print(f"\n{i}.", doc.page_content.strip())
        print("\n" + "="*80)
