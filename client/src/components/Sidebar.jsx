import React from "react";
import { X } from "lucide-react";

const SidebarContent = ({ content }) => (
  <div dangerouslySetInnerHTML={{ __html: content }} />
);

const Sidebar = ({ isOpen, content, onClose }) => (
  <div
    className={`fixed inset-y-0 right-0 w-full md:w-1/3 bg-white z-10 overflow-y-auto shadow-2xl transition-transform duration-300 ease-in-out ${
      isOpen ? "translate-x-0" : "translate-x-full"
    }`}
  >
    <div className="p-2 sm:p-4">
      <button
        onClick={onClose}
        className="absolute top-2 right-2 text-black bg-[#2DEB5F] p-3 m-3 rounded-[15%]"
      >
        <X size={16} className="sm:w-5 sm:h-5" />
      </button>
      <div className="p-5">
        <SidebarContent content={content} />
      </div>
    </div>
  </div>
);

export default Sidebar;
