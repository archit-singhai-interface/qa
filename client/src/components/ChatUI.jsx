/**
 * @citation @[rag.py]
 * This component interacts with the RAGBot.ask() method in rag.py
 * 
 * RAG (Retrieval-Augmented Generation) Query Flow:
 * 1. Frontend sends a text query to the backend
 * 2. @[rag.py] processes the query through the following steps:
 *    - Select relevant documents
 *    - Retrieve context
 *    - Generate an answer using LLM
 * 
 * Expected Response Structure from @[rag.py]:
 * {
 *   answer: string,           // Main response text
 *   sources: string[],        // Source document paths
 *   content: string[],        // Extracted content snippets
 *   context: object[],        // Detailed context information
 *   relevant_docs: string[]   // Relevant document paths
 * }
 * 
 * Key Integration Points:
 * - Handles asynchronous RAG query
 * - Manages streaming of AI-generated responses
 * - Displays sources and context from backend
 */

import React, { useState } from "react";
import { Loader, Bot } from "lucide-react";
import axios from "axios";
import Navbar from "./Navbar";
import Sidebar from "./Sidebar";
import InputArea from "./InputArea";
import Message from "./Message";

// TODO: Make the UI Responsive

const EmptyState = () => (
  <div className="h-full flex flex-col justify-center items-center space-y-4 sm:space-y-6">
    <h1 className="md:text-2xl font-bold text-gray-700 text-center px-4">
      How can I help you today?
    </h1>
  </div>
);

const MessageList = ({ messages, isStreaming, handleSourceClick }) => (
  <div className="max-w-3xl mx-auto space-y-2 sm:space-y-4">
    {messages.map((message, index) => (
      <Message
        key={index}
        message={message}
        isStreaming={isStreaming}
        handleSourceClick={handleSourceClick}
      />
    ))}
  </div>
);

const LoadingIndicator = () => (
  <div className="max-w-3xl mx-auto">
    <div className="flex justify-start">
      <Bot size={45} className="m-2 text-[#2DEB5F] bg-black p-2 rounded" />
      <div className="max-w-[80%] sm:max-w-xs md:max-w-md lg:max-w-lg xl:max-w-xl rounded-lg p-2 sm:p-4 mb-5 m-1 bg-white text-black border border-black-600 flex items-center">
        <Loader className="animate-spin text-[#2DEB5F]" size={16} />
        <span className="ml-2 text-sm sm:text-lg">Thinking...</span>
      </div>
    </div>
  </div>
);

const ChatUI = () => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [sidebarContent, setSidebarContent] = useState("");
  const [isSidebarOpen, setIsSidebarOpen] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [sources, setSources] = useState([]);
  const [isStreaming, setIsStreaming] = useState(false);

  const simulateStreaming = (message) => {
    let i = 0;
    const interval = setInterval(() => {
      if (i < message.length) {
        setMessages((prev) => {
          const lastMessage = prev[prev.length - 1];
          const updatedMessages = prev.slice(0, -1);
          return [
            ...updatedMessages,
            { ...lastMessage, content: message.slice(0, i + 1) },
          ];
        });
        i++;
      } else {
        clearInterval(interval);
        setIsStreaming(false);
      }
    }, 5);
  };

  const handleSend = async (message = input) => {
    // @citation @[rag.py]: RAGBot.ask() method integration
    // This method handles the Retrieval-Augmented Generation (RAG) query
    // Follows the query processing flow defined in @[rag.py]

    if (!message.trim()) return;

    // Prepare UI for new message
    setMessages((prev) => [...prev, { role: "user", content: message }]);
    setInput("");
    setIsLoading(true);
    setIsStreaming(true);

    try {
      // @citation @[rag.py]: Invoke RAG query endpoint
      // Sends user query to backend for processing
      const response = await axios.post(
        `${import.meta.env.VITE_API_ENDPOINT}ask`,
        { text: message }
      );

      // @citation @[rag.py]: Process RAG response
      // Defensive parsing of sources and content from backend
      const updatedSources = (response.data.sources || []).map((source, index) => ({
        title: source,
        content: (response.data.content || [])[index] || '',
      }));

      // @citation @[rag.py]: Update sources from retrieved documents
      setSources((prev) => [...prev, ...updatedSources]);

      setTimeout(() => {
        // @citation @[rag.py]: Prepare message with RAG context
        setMessages((prev) => [
          ...prev,
          { 
            role: "assistant", 
            content: response.data.answer || response.data.text || '',
            sources: updatedSources,
            context: response.data.context || [],  // Context from @[rag.py]
            relevant_docs: response.data.relevant_docs || []  // Relevant documents
          },
        ]);
        
        // @citation @[rag.py]: Stream AI-generated response
        simulateStreaming(response.data.answer || response.data.text || '');
      }, 1000);
    } catch (error) {
      // @citation @[rag.py]: Error handling for RAG query
      console.error("Error processing RAG query from @[rag.py]:", error);
      
      // Fallback error message
      setMessages((prev) => [
        ...prev,
        { 
          role: "assistant", 
          content: "Sorry, I couldn't process your request. Please try again.",
        },
      ]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleFeatureClick = (title) => handleSend(title);

  const handleLinkClick = (content) => {
    setSidebarContent(content);
    setIsSidebarOpen(true);
  };

  const handleSourceClick = (source) => {
    if (source) {
      handleLinkClick(`<h1>${source.title}</h1>${source.content}`);
    }
  };

  const features = [
    "How can I track the SCRR rate on my account?",
    "How can self ship refund be done",
  ];

  return (
    <>
      <Navbar />
      <div className="flex flex-col md:flex-row h-[90vh] bg-white text-gray-800">
        <div
          className={`flex-1 flex flex-col ${
            isSidebarOpen ? "hidden md:flex" : "flex"
          }`}
        >
          <div className="flex-1 overflow-y-auto p-2 sm:p-4">
            {messages.length === 0 ? (
              <EmptyState />
            ) : (
              <MessageList
                messages={messages}
                isStreaming={isStreaming}
                handleSourceClick={handleSourceClick}
              />
            )}
            {isLoading && <LoadingIndicator />}
          </div>
          <InputArea
            input={input}
            setInput={setInput}
            handleSend={handleSend}
            features={features}
            handleFeatureClick={handleFeatureClick}
            showFeatures={messages.length === 0}
          />
        </div>
        <Sidebar
          isOpen={isSidebarOpen}
          content={sidebarContent}
          onClose={() => setIsSidebarOpen(false)}
        />
      </div>
    </>
  );
};

export default ChatUI;
