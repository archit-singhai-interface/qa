from typing import Literal
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.tools import StructuredTool
from langgraph.graph import StateGraph, MessagesState
from langgraph.prebuilt import ToolNode
import os
import json
import logging
from dotenv import load_dotenv
import traceback
from rank_bm25 import BM25Okapi
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re

# Download required NLTK data
# nltk.download('punkt')
# nltk.download('stopwords')

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Add this system prompt near the top of the file
SYSTEM_PROMPT = """You are an expert Amazon Seller Assistant with deep knowledge of Amazon's seller ecosystem. Your role is to:

1. Navigate and explain Amazon's seller documentation accurately
2. Provide actionable, step-by-step guidance for sellers
3. Cite specific documentation sections when answering
4. Consider the hierarchical context of documents (main sections and subsections)
5. Clarify complex FBA, shipping, and inventory management concepts
6. Proactively mention related topics that might be helpful

When searching documentation:
- Consider the document hierarchy and relationships between sections
- Weigh information from more specific/detailed documents higher
- Cross-reference related documents to provide comprehensive answers
- Always cite the specific document section you're referencing

Document sections you're most knowledgeable about:
- Get started with Fulfillment by Amazon (FBA)
- Inventory Management Tools
- Service and Delivery Management
- Seller Flex and Alternative Fulfillment"""

class AmazonSellerAgent:
    def __init__(self, docs_path: str, chunk_size: int = 1000, chunk_overlap: int = 200):
        try:
            self.docs_path = docs_path
            
            # Load document summaries
            summaries_path = os.path.join(docs_path, "document_summaries.json")
            with open(summaries_path, 'r') as f:
                self.doc_summaries = json.load(f)
            
            # Load and process all documents
            self.doc_contents = []
            self.doc_metadata = []
            self.stop_words = set(stopwords.words('english'))
            
            for doc_path, doc_info in self.doc_summaries['documents'].items():
                try:
                    with open(doc_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        paragraphs = [p.strip() for p in content.split('\n\n') if p.strip()]
                        
                        for paragraph in paragraphs:
                            tokens = word_tokenize(paragraph.lower())
                            tokens = [token for token in tokens if token not in self.stop_words]
                            
                            if tokens:
                                self.doc_contents.append(tokens)
                                self.doc_metadata.append({
                                    'content': paragraph,
                                    'name': doc_info['name'],
                                    'path': doc_path
                                })
                                
                except Exception as e:
                    logger.error(f"Error loading {doc_path}: {str(e)}")
            
            # Initialize BM25
            self.bm25 = BM25Okapi(self.doc_contents)
            logger.info(f"Initialized BM25 with {len(self.doc_contents)} paragraphs")
            
            # Create the tools
            self.tools = [
                StructuredTool.from_function(
                    func=self.search_docs,
                    name="search_docs",
                    description="Search Amazon Seller documentation using BM25 ranking for accurate results.  use search terms like SAFE-T, FBA, shipping, inventory management, etc."
                ),
                StructuredTool.from_function(
                    func=self.hierarchical_search,
                    name="hierarchical_search",
                    description="Search documentation considering the hierarchical structure and relationships between documents."
                ),
                StructuredTool.from_function(
                    func=self.get_related_topics,
                    name="get_related_topics",
                    description="Find related topics and documents based on the current context."
                )
            ]
            
            # Initialize model with tools
            self.model = ChatOpenAI(
                model="gpt-4o-mini",
                temperature=0
            ).bind_tools(self.tools)
            
            # Initialize graph
            self.graph = self._build_graph()
            logger.info("Graph built successfully")
            
            # Add term mapping dictionary
            self.term_mapping = {
                "safe t": "SAFE-T",
                "safe-t": "SAFE-T",
                "safet": "SAFE-T",
                "safe_t": "SAFE-T",
                # Add other term mappings as needed
                "fba": "FBA",
                "mli": "MLI",
                "multi location inventory": "Multi-Location Inventory",
            }
            
        except Exception as e:
            logger.error(f"Error initializing agent: {str(e)}")
            logger.error(traceback.format_exc())
            raise

    def _normalize_query(self, query: str) -> str:
        """Normalize query terms using the mapping dictionary."""
        normalized = query.lower()
        for term, replacement in self.term_mapping.items():
            # Use word boundaries to avoid partial replacements
            normalized = re.sub(r'\b' + re.escape(term) + r'\b', replacement, normalized)
        return normalized

    def search_docs(self, query: str) -> str:
        """Search Amazon Seller documentation using BM25 ranking."""
        try:
            logger.info(f"[search_docs] Starting search with query: {query}")
            
            # Normalize the query
            normalized_query = self._normalize_query(query)
            logger.info(f"[search_docs] Normalized query: {normalized_query}")
            
            # Tokenize and process query
            query_tokens = word_tokenize(normalized_query)
            query_tokens = [token for token in query_tokens 
                          if token not in self.stop_words]
            
            # Get BM25 scores
            scores = self.bm25.get_scores(query_tokens)
            
            # Get top matches with scores above threshold
            threshold = 0.5
            matches = []
            
            for idx, score in enumerate(scores):
                if score > threshold:
                    matches.append({
                        'content': self.doc_metadata[idx]['content'],
                        'name': self.doc_metadata[idx]['name'],
                        'path': self.doc_metadata[idx]['path'],
                        'score': score
                    })
            
            # Sort by score
            matches.sort(key=lambda x: x['score'], reverse=True)
            
            if matches:
                response = "Here are the most relevant sections:\n\n"
                
                # Group matches by document
                doc_matches = {}
                for match in matches[:10]:  # Consider top 10 matches
                    if match['name'] not in doc_matches:
                        doc_matches[match['name']] = []
                    doc_matches[match['name']].append(match)
                
                # Output grouped results
                for doc_name, doc_sections in doc_matches.items():
                    response += f"From document: {doc_name}\n"
                    response += f"Source: {doc_sections[0]['path']}\n\n"
                    
                    for idx, section in enumerate(doc_sections, 1):
                        response += (f"Section {idx} (score: {section['score']:.2f}):\n"
                                   f"{section['content']}\n\n")
                    
                    response += "="*50 + "\n\n"
                
                return response
            return "No relevant information found in the documentation."
            
        except Exception as e:
            logger.error(f"[search_docs] Error: {str(e)}")
            logger.error(traceback.format_exc())
            return "Error searching documentation."

    def _build_graph(self):
        # Create tool node
        tool_node = ToolNode(self.tools)
        
        # Create workflow
        workflow = StateGraph(MessagesState)
        
        # Add nodes
        workflow.add_node("agent", self._call_model)
        workflow.add_node("tools", tool_node)
        
        # Add edges
        workflow.add_edge("__start__", "agent")
        workflow.add_conditional_edges(
            "agent",
            self._should_continue,
        )
        workflow.add_edge("tools", "agent")
        
        return workflow.compile()

    def _should_continue(self, state: MessagesState) -> Literal["tools", "__end__"]:
        messages = state['messages']
        last_message = messages[-1]
        if last_message.tool_calls:
            return "tools"
        return "__end__"

    def _call_model(self, state: MessagesState):
        messages = state['messages']
        response = self.model.invoke(messages)
        return {"messages": [response]}

    def _search_single_doc(self, query: str, doc_path: str) -> list:
        """Search within a specific document."""
        try:
            doc_tokens = []
            doc_metadata = []
            
            with open(doc_path, 'r', encoding='utf-8') as f:
                content = f.read()
                paragraphs = [p.strip() for p in content.split('\n\n') if p.strip()]
                
                for paragraph in paragraphs:
                    tokens = word_tokenize(paragraph.lower())
                    tokens = [token for token in tokens 
                             if token not in stopwords.words('english')]
                    
                    if tokens:
                        doc_tokens.append(tokens)
                        doc_metadata.append({
                            'content': paragraph,
                            'name': os.path.basename(doc_path),
                            'path': doc_path
                        })

            doc_bm25 = BM25Okapi(doc_tokens)
            query_tokens = word_tokenize(query.lower())
            query_tokens = [token for token in query_tokens 
                           if token not in stopwords.words('english')]
            scores = doc_bm25.get_scores(query_tokens)
            
            matches = []
            for idx, score in enumerate(scores):
                if score > 0.5:
                    matches.append({
                        **doc_metadata[idx],
                        'score': score
                    })
            
            return matches

        except Exception as e:
            logger.error(f"[_search_single_doc] Error: {str(e)}")
            return []

    def hierarchical_search(self, query: str) -> str:
        """Search documentation considering hierarchy and document relationships."""
        try:
            sections = {}
            for doc_path in self.doc_summaries['documents']:
                parts = doc_path.split('/')
                section = parts[-2]
                if section not in sections:
                    sections[section] = []
                sections[section].append(doc_path)

            results = []
            for section, docs in sections.items():
                section_scores = []
                for doc_path in docs:
                    doc_info = self.doc_summaries['documents'][doc_path]
                    doc_results = self._search_single_doc(query, doc_path)
                    if doc_results:
                        section_scores.extend(doc_results)
                
                if section_scores:
                    results.append({
                        'section': section,
                        'matches': sorted(section_scores, key=lambda x: x['score'], reverse=True)[:3]
                    })

            response = "Here are the relevant sections by topic area:\n\n"
            for section_result in results:
                response += f"## {section_result['section']}\n\n"
                for match in section_result['matches']:
                    response += f"From: {match['name']}\n"
                    response += f"Context: {match['content']}\n"
                    response += f"Relevance: {match['score']:.2f}\n\n"

            return response

        except Exception as e:
            logger.error(f"[hierarchical_search] Error: {str(e)}")
            return "Error performing hierarchical search."

    def get_related_topics(self, current_topic: str) -> str:
        """Find related topics based on document relationships and content similarity."""
        try:
            section_scores = {}
            scores = self.bm25.get_scores(word_tokenize(current_topic.lower()))
            
            for idx, score in enumerate(scores):
                if score > 0.3:
                    doc_path = self.doc_metadata[idx]['path']
                    section = doc_path.split('/')[-2]
                    
                    if section not in section_scores:
                        section_scores[section] = []
                    
                    section_scores[section].append({
                        'content': self.doc_metadata[idx]['content'],
                        'name': self.doc_metadata[idx]['name'],
                        'score': score
                    })

            response = "Related topics you might find helpful:\n\n"
            for section, matches in section_scores.items():
                response += f"In {section}:\n"
                for match in sorted(matches, key=lambda x: x['score'], reverse=True)[:2]:
                    response += f"- {match['name']}: {match['content'][:200]}...\n"
                response += "\n"

            return response

        except Exception as e:
            logger.error(f"[get_related_topics] Error: {str(e)}")
            return "Error finding related topics."

    async def think_and_respond(self, query: str) -> dict:
        """Process the query and generate a response using the agent."""
        try:
            initial_state = {
                "messages": [
                    SystemMessage(content=SYSTEM_PROMPT),
                    HumanMessage(content=query)
                ]
            }
            
            final_state = self.graph.invoke(
                initial_state,
                config={
                    "configurable": {
                        "thread_id": hash(query)
                    }
                }
            )
            
            responses = final_state["messages"]
            final_response = next((msg.content for msg in reversed(responses) 
                                 if msg.type in ["ai", "assistant"]), 
                                "No response generated")
            
            return {
                "text": final_response,
                "answer": final_response,
                "sources": [
                    str(getattr(msg, 'tool_calls', []))
                    for msg in responses 
                    if hasattr(msg, 'tool_calls') and getattr(msg, 'tool_calls', None)
                ],
                "content": [
                    msg.content for msg in responses if msg.type == "tool"
                ],
                "context": [
                    {"thought": msg.content}
                    for msg in responses if msg.type in ["ai", "assistant"]
                ]
            }
                
        except Exception as e:
            logger.error(f"[think_and_respond] Error: {str(e)}")
            logger.error(traceback.format_exc())
            raise