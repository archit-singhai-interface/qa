import React from "react";
import { Bot, User } from "lucide-react";
import AssistantMessage from "./AssistantMessage";

const Message = ({ message, isStreaming, handleSourceClick }) => (
  <div
    className={`flex ${
      message.role === "user" ? "justify-end" : "justify-start"
    }`}
  >
    {message.role === "assistant" && (
      <Bot size={45} className="m-2 text-[#2DEB5F] bg-black p-2 rounded" />
    )}
    <div
      className={`max-w-[80%] sm:max-w-xs md:max-w-md lg:max-w-lg xl:max-w-xl rounded-lg p-2 sm:p-4 mb-5 m-1 ${
        message.role === "user"
          ? "bg-white text-black border border-green-600"
          : "bg-white text-black border border-black-600"
      }`}
    >
      <div className="text-sm sm:text-lg">
        {message.role === "assistant" ? (
          <AssistantMessage
            content={message.content}
            sources={message.sources}
            isStreaming={isStreaming}
            handleSourceClick={handleSourceClick}
          />
        ) : (
          message.content
        )}
      </div>
    </div>
    {message.role === "user" && (
      <User size={45} className="m-2 bg-[#2DEB5F] p-2 rounded" />
    )}
  </div>
);

export default Message;
