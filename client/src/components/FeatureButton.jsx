import React from "react";

const FeatureButton = ({ title, onClick }) => (
  <button
    className="bg-gray-200 text-gray-800 p-4 md:p-2 rounded-lg text-left hover:bg-gray-300 focus:outline-none focus:ring-2 focus:ring-gray-300 shadow-sm w-full h-full flex items-center justify-center"
    onClick={() => onClick(title)}
  >
    <h3 className="font-bold text-sm sm:text-base md:text-lg text-center">
      {title}
    </h3>
  </button>
);

export default FeatureButton;
