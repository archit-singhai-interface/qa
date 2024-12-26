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

# Download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

class AmazonSellerAgent:
    def __init__(self, docs_path: str):
        try:
            self.docs_path = docs_path
            
            # Load document summaries
            summaries_path = os.path.join(docs_path, "document_summaries.json")
            with open(summaries_path, 'r') as f:
                self.doc_summaries = json.load(f)
            
            # Load and process all documents
            self.doc_contents = []
            self.doc_metadata = []
            stop_words = set(stopwords.words('english'))
            
            for doc_path, doc_info in self.doc_summaries['documents'].items():
                try:
                    with open(doc_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        
                        # Split into paragraphs and process each
                        paragraphs = [p.strip() for p in content.split('\n\n') if p.strip()]
                        
                        for paragraph in paragraphs:
                            # Tokenize and remove stopwords
                            tokens = word_tokenize(paragraph.lower())
                            tokens = [token for token in tokens if token not in stop_words]
                            
                            if tokens:  # Only add non-empty paragraphs
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
            
            # Create search_docs function
            def search_docs(query: str) -> str:
                """Search Amazon Seller documentation using BM25 ranking."""
                try:
                    logger.info(f"[search_docs] Starting search with query: {query}")
                    
                    # Tokenize and process query
                    query_tokens = word_tokenize(query.lower())
                    query_tokens = [token for token in query_tokens 
                                  if token not in stop_words]
                    
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
            
            # Create the tool using from_function
            self.tools = [
                StructuredTool.from_function(
                    func=search_docs,
                    name="search_docs",
                    description="Search Amazon Seller documentation using BM25 ranking for accurate results."
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
            
        except Exception as e:
            logger.error(f"Error initializing agent: {str(e)}")
            logger.error(traceback.format_exc())
            raise

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

    async def think_and_respond(self, query: str) -> dict:
        """Process the query and generate a response using the agent."""
        try:
            initial_state = {
                "messages": [
                    SystemMessage(content="You are a helpful assistant for Amazon Sellers."),
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