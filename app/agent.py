from itertools import tee
from typing import Literal, List

from pygments import lex
from langchain_openai import ChatOpenAI, AzureChatOpenAI, AzureOpenAIEmbeddings
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage, ToolMessage
from langchain_core.tools import StructuredTool
from langgraph.graph import StateGraph, MessagesState, START, END
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.memory import MemorySaver
#from langgraph.graph import StateGraph, MessagesState, START, END
import os
import json
import logging
from dotenv import load_dotenv
import traceback
from rank_bm25 import BM25Okapi
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import pinecone
from langchain_openai import OpenAIEmbeddings
from langchain_openai import AzureChatOpenAI
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone, ServerlessSpec
import numpy as np
from langchain.text_splitter import RecursiveCharacterTextSplitter
#from langchain_azure_openai import AzureOpenAIEmbeddings
from langchain_openai import AzureOpenAIEmbeddings
import time
from langchain.schema import Document
from uuid import uuid4
from langchain_text_splitters import MarkdownHeaderTextSplitter


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
        """Initialize agent with document path and setup semantic search"""
        try:
            self.docs_path = docs_path
            
            # Create proper SystemMessage
            self.system_message = SystemMessage(content="""You are a helpful assistant for Amazon sellers. 
            You can search through Amazon seller documentation to provide accurate answers.
            Use the semantic_search tool when you need to find specific information in the documentation.
            Always be clear and precise in your responses, and cite relevant documentation when possible.""")
            
            # Initialize Pinecone
            self.pc = Pinecone(
                api_key="pcsk_6SJkto_GoSyMgvYbNj9xXi1BRyF8MtX1NVgWtAEwRPrVYhG76Pkh1YhWvU8o66X5kqz69c"
            )
            
            # Setup Pinecone index
            index_name = "amazon-seller-docs"
            
            # Check if index exists
            existing_indexes = [index_info["name"] for index_info in self.pc.list_indexes()]
            
            if index_name not in existing_indexes:
                logger.info(f"Creating new index: {index_name}")
                self.pc.create_index(
                    name=index_name,
                    dimension=3072,
                    metric="cosine",
                    spec=ServerlessSpec(
                        cloud="aws",
                        region="us-east-1"
                    )
                )
            
            # Get the index
            self.index = self.pc.Index(index_name)
            
            # Initialize embeddings
            self.embeddings = AzureOpenAIEmbeddings(
                deployment=os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT_NAME"),
                api_key=os.getenv("AZURE_OPENAI_EMBEDDING_API_KEY"),
                azure_endpoint=os.getenv("AZURE_OPENAI_EMBEDDING_ENDPOINT"),
                api_version="2023-05-15"
            )
            
            # Initialize vector store
            self.vectorstore = PineconeVectorStore(
                index=self.index,
                embedding=self.embeddings,
                text_key="text"
            )
            
            # Define tools
            self.tools = [
                StructuredTool.from_function(
                    func=self.semantic_search,
                    name="semantic_search",
                    description="Search documentation using semantic similarity"
                )
            ]
            
            # Initialize model with tools
            self.model = AzureChatOpenAI(
                model="gpt-4o-mini",
                temperature=0.2,
                api_key=os.getenv("AZURE_OPENAI_API_KEY"),
                azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
                api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
                azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
            ).bind_tools(self.tools)

            # self.model = ChatOpenAI(
            #     model="gpt-4",
            #     temperature=0.2
            # ).bind_tools(self.tools)
            
            # Build graph
            self.graph = self._build_graph()
            
        except Exception as e:
            logger.error(f"Error initializing agent: {str(e)}")
            raise

    def _build_graph(self):
        """Build graph with proper tool handling"""
        try:
            workflow = StateGraph(MessagesState)
            
            # Add model node
            workflow.add_node("agent", self.call_model)
            workflow.add_node("tools", ToolNode(self.tools))
            
            # Add edges with conditional routing
            workflow.add_edge(START, "agent")
            workflow.add_conditional_edges(
                "agent",
                self._should_continue,
                {
                    "tools": "tools",
                    "__end__": END
                }
            )
            workflow.add_edge("tools", "agent")
            
            # Compile without checkpointer
            return workflow.compile()
                
        except Exception as e:
            logger.error(f"Error building graph: {str(e)}")
            raise

    def _should_continue(self, state: MessagesState) -> Literal["tools", "__end__"]:
        """Determine if we should continue processing"""
        messages = state['messages']
        last_message = messages[-1]
        
        # If there are tool calls, continue
        if hasattr(last_message, 'tool_calls') and last_message.tool_calls:
            return "tools"
        return "__end__"

    def _call_model_filtered(self, state: MessagesState):
        """Call model with filtered message history"""
        # Filter messages before sending to model
        filtered_messages = self._filter_messages(state['messages'])
        
        # Get model response
        response = self.model.invoke(filtered_messages)
        
        # If the response has tool calls, we need to include them in the message history
        if hasattr(response, 'tool_calls') and response.tool_calls:
            messages = []
            
            # Add tool messages for each tool call
            for tool_call in response.tool_calls:
                tool = next((t for t in self.tools if t.name == tool_call.name), None)
                if tool:
                    try:
                        args = json.loads(tool_call.arguments)
                        result = tool.invoke(args)
                        
                        from langchain_core.messages import ToolMessage
                        tool_message = ToolMessage(
                            content=str(result),
                            tool_call_id=tool_call.id,
                            name=tool_call.name
                        )
                        messages.append(tool_message)
                    except Exception as e:
                        logger.error(f"Error executing tool {tool_call.name}: {str(e)}")
                        messages.append(
                            ToolMessage(
                                content=f"Error: {str(e)}",
                                tool_call_id=tool_call.id,
                                name=tool_call.name
                            )
                        )
            return {"messages": state["messages"] + messages}
        
        return {"messages": state["messages"] + [response]}

    async def think_and_respond(self, query: str) -> dict:
        """Process query without state management"""
        try:
            # Initialize state
            initial_state = {
                "messages": [
                    self.system_message,
                    HumanMessage(content=query)
                ]
            }
            
            # Run graph without config
            result = await self.graph.ainvoke(initial_state)
            
            # Process responses
            responses = result["messages"]
            final_response = next((msg.content for msg in reversed(responses) 
                                 if isinstance(msg, AIMessage)), 
                                "No response generated")
            
            return {
                "text": final_response,
                "answer": final_response,
                "sources": [
                    str(getattr(msg, 'tool_calls', []))
                    for msg in responses 
                    if hasattr(msg, 'tool_calls')
                ],
                "content": [
                    msg.content for msg in responses 
                    if isinstance(msg, ToolMessage)
                ],
                "context": [
                    {"thought": msg.content}
                    for msg in responses 
                    if isinstance(msg, AIMessage)
                ]
            }
                
        except Exception as e:
            logger.error(f"[think_and_respond] Error: {str(e)}")
            logger.error(traceback.format_exc())
            raise

    def _index_documents(self):
        """Index documents in Pinecone with header-based splitting"""
        try:
            texts = []
            metadatas = []
            
            # Define headers to split on
            headers_to_split_on = [
                ("#", "Header 1"),
                ("##", "Header 2"), 
                ("###", "Header 3"),
                ("####", "Header 4")
            ]
            
            # Initialize markdown splitter with strip_headers=False to keep headers in content
            markdown_splitter = MarkdownHeaderTextSplitter(
                headers_to_split_on=headers_to_split_on,
                strip_headers=False  # This keeps headers in the content
            )
            
            # Process each document
            for doc_path, doc_info in self.doc_summaries['documents'].items():
                try:
                    fixed_path = doc_path.replace('amazon_help_pages_us_prod/amazon_help_pages_us_prod/', 'amazon_help_pages_us_prod/')
                    full_path = os.path.join(self.docs_path, fixed_path)
                    
                    if not os.path.exists(full_path):
                        alt_path = os.path.join(self.docs_path, doc_path.split('amazon_help_pages_us_prod/')[-1])
                        if os.path.exists(alt_path):
                            full_path = alt_path
                        else:
                            continue
                            
                    with open(full_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        
                        # Split document by headers while keeping headers in content
                        splits = markdown_splitter.split_text(content)
                        
                        for split in splits:
                            texts.append(split.page_content)
                            metadata = {
                                'source': doc_path,
                                'name': doc_info['name']
                            }
                            # Add header metadata
                            metadata.update(split.metadata)
                            metadatas.append(metadata)
                            
                except Exception as e:
                    logger.error(f"Error processing {doc_path}: {str(e)}")
                    continue
            
            if not texts:
                logger.warning("No documents were processed successfully")
                return
                
            # Create Document objects and process in batches
            batch_size = 10  # Process 10 documents at a time
            for i in range(0, len(texts), batch_size):
                batch_texts = texts[i:i + batch_size]
                batch_metadatas = metadatas[i:i + batch_size]
                
                documents = [
                    Document(page_content=text, metadata=metadata)
                    for text, metadata in zip(batch_texts, batch_metadatas)
                ]
                
                # Generate UUIDs for batch
                uuids = [str(uuid4()) for _ in range(len(documents))]
                
                try:
                    # Add batch to Pinecone
                    self.vectorstore.add_documents(
                        documents=documents,
                        ids=uuids
                    )
                    
                    logger.info(f"Successfully indexed batch of {len(documents)} documents")
                    
                    # Sleep between batches to respect rate limits
                    time.sleep(1)  # Wait 1 second between batches
                    
                except Exception as e:
                    if "429" in str(e):  # Rate limit error
                        wait_time = 60  # Wait 1 minute if rate limited
                        logger.warning(f"Rate limit hit. Waiting {wait_time} seconds...")
                        time.sleep(wait_time)
                        # Retry the batch
                        self.vectorstore.add_documents(
                            documents=documents,
                            ids=uuids
                        )
                    else:
                        raise
            
            logger.info(f"Successfully indexed all {len(texts)} text chunks in Pinecone")
            
        except Exception as e:
            logger.error(f"Error indexing documents: {str(e)}")
            raise

    def _filter_messages(self, messages: List[dict], max_messages: int = 5) -> List[dict]:
        """Filter messages to keep conversation history manageable"""
        # Always keep system message if present
        system_messages = [msg for msg in messages if isinstance(msg, SystemMessage)]
        
        # Get non-system messages
        other_messages = [msg for msg in messages if not isinstance(msg, SystemMessage)]
        
        # Keep only the last N messages
        recent_messages = other_messages[-max_messages:] if other_messages else []
        
        # Combine system messages with recent messages
        filtered = system_messages + recent_messages
        
        # Log the filtering
        logger.debug(f"Filtered {len(messages)} messages down to {len(filtered)}")
        
        return filtered

    def semantic_search(self, query: str) -> str:
        """Perform semantic search on Amazon Seller documentation."""
        try:
            logger.debug(f"Starting semantic search for query: {query}")
            
            results = self.vectorstore.similarity_search_with_score(
                query,
                k=5
            )
            
            if not results:
                return "No relevant documentation found."
            
            response = "Here are the most relevant sections:\n\n"
            for doc, score in results:
                response += f"Relevance Score: {score:.2f}\n"
                response += f"Source: {doc.metadata.get('source', 'Unknown')}\n"
                response += f"Content:\n{doc.page_content}\n\n"
                response += "-" * 50 + "\n\n"
            
            return response
                
        except Exception as e:
            logger.error(f"Semantic search error: {str(e)}")
            logger.error(traceback.format_exc())
            return f"Error performing semantic search: {str(e)}"

    def search_docs(self, query: str) -> str:
        """Search documentation using BM25 ranking."""
        try:
            # Tokenize query
            query_tokens = word_tokenize(query.lower())
            query_tokens = [token for token in query_tokens 
                          if token not in stopwords.words('english')]
            
            # Get BM25 scores
            scores = self.bm25.get_scores(query_tokens)
            top_n = 3
            top_indices = np.argsort(scores)[-top_n:][::-1]
            
            response = "Here are the most relevant sections (BM25 search):\n\n"
            for idx in top_indices:
                if scores[idx] > 0:
                    metadata = self.doc_metadata[idx]
                    response += f"Score: {scores[idx]:.2f}\n"
                    response += f"Source: {metadata['name']}\n"
                    response += f"Content:\n{metadata['content']}\n\n"
                    response += "-" * 50 + "\n\n"
            
            return response if response else "No relevant documentation found."
                
        except Exception as e:
            logger.error(f"BM25 search error: {str(e)}")
            return f"Error performing BM25 search: {str(e)}"

    def call_model(self, state: MessagesState):
        """Call model with filtered message history"""
        try:
            filtered_messages = self._filter_messages(state["messages"])
            response = self.model.invoke(filtered_messages)
            
            if hasattr(response, 'tool_calls') and response.tool_calls:
                messages = []
                messages.append(response)  # Add the assistant's response with tool calls
                
                # Execute tools and collect results
                for tool_call in response.tool_calls:
                    try:
                        # Extract tool information
                        if isinstance(tool_call, dict):
                            tool_name = tool_call.get('name')
                            tool_id = tool_call.get('id')
                            raw_args = tool_call.get('arguments', {})
                        else:
                            tool_name = tool_call.name
                            tool_id = tool_call.id
                            raw_args = tool_call.arguments or {}
                        
                        # Find matching tool
                        tool = next((t for t in self.tools if t.name == tool_name), None)
                        if not tool:
                            continue
                        
                        # Process arguments
                        try:
                            if isinstance(raw_args, str):
                                try:
                                    args = json.loads(raw_args)
                                except json.JSONDecodeError:
                                    args = {"query": raw_args}
                            else:
                                args = raw_args
                        except Exception:
                            args = {"query": str(raw_args)}
                        
                        # Ensure args is a valid dictionary with query
                        if not isinstance(args, dict):
                            args = {"query": str(args)}
                        if "query" not in args or not args["query"]:
                            args = {"query": "general information about " + tool_name}
                        
                        # Log the tool execution
                        logger.debug(f"Executing {tool_name} with args: {args}")
                        
                        # Execute tool
                        result = tool.invoke(args)
                        
                        # Create tool message
                        tool_message = ToolMessage(
                            content=str(result),
                            tool_call_id=tool_id,
                            name=tool_name
                        )
                        messages.append(tool_message)
                        
                    except Exception as e:
                        logger.error(f"Error in tool execution: {str(e)}")
                        logger.error(f"Tool call details: {tool_call}")
                        tool_message = ToolMessage(
                            content=f"Error executing {tool_name}: {str(e)}",
                            tool_call_id=tool_id,
                            name=tool_name
                        )
                        messages.append(tool_message)
                
                # Get final response
                if messages:
                    final_messages = filtered_messages + messages
                    final_messages.append(HumanMessage(content="Based on the search results above, please provide a comprehensive answer."))
                    final_response = self.model.invoke(final_messages)
                    messages.append(final_response)
                
                return {"messages": state["messages"] + messages}
            
            return {"messages": state["messages"] + [response]}
            
        except Exception as e:
            logger.error(f"Error in call_model: {str(e)}")
            logger.error(traceback.format_exc())
            raise