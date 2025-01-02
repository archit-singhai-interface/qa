import React from "react";
import Markdown from "react-markdown";

const AssistantMessage = ({
  content,
  sources,
  isStreaming,
  handleSourceClick,
}) => (
  <>
    <Markdown>{content}</Markdown>
    {sources && sources.length > 0 && !isStreaming && (
      <div className="mt-2">
        <span className="text-sm">
          Sources
          <br />
        </span>
        {sources.map((source, idx) => (
          <span key={idx}>
            <a
              href="#"
              onClick={() => handleSourceClick(source)}
              className="text-blue-600 hover:underline ml-2 text-sm"
            >
              {idx + 1}. {source.title}
            </a>
            <br />
          </span>
        ))}
      </div>
    )}
  </>
);

export default AssistantMessage;
