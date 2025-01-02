import React from "react";
import { Send } from "lucide-react";
import FeatureButton from "./FeatureButton";

const InputArea = ({
  input,
  setInput,
  handleSend,
  features,
  handleFeatureClick,
  showFeatures,
}) => (
  <div className="p-2 sm:p-4">
    <div className="max-w-3xl mx-auto">
      {showFeatures && (
        <div className="grid grid-cols-1 sm:grid-cols-2 gap-1 sm:gap-4 w-full max-w-2xl mb-4">
          {features.map((feature, index) => (
            <FeatureButton
              key={index}
              title={feature}
              onClick={handleFeatureClick}
            />
          ))}
        </div>
      )}
      <div className="flex items-center space-x-2">
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={(e) => e.key === "Enter" && handleSend()}
          placeholder="Message Interface QA Bot"
          className="flex-1 border border-gray-300 rounded-lg px-3 sm:px-4 py-2.5 sm:py-2.5 text-sm sm:text-base focus:outline-none focus:ring-2 focus:ring-[#2DEB5F]"
        />
        <button
          onClick={() => handleSend()}
          className="bg-[#2DEB5F] text-black rounded-md p-3 sm:p-[10px] hover:bg-[#14d146] focus:outline-none focus:ring-2 focus:ring-blue-500"
        >
          <Send size={16} className="sm:w-5 sm:h-5" />
        </button>
      </div>
      <div>
        <p className="text-xs text-gray-500 text-center mt-1">
          Refer to citations for detailed information
        </p>
      </div>
    </div>
  </div>
);

export default InputArea;
