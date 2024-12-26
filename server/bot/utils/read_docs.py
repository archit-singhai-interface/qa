import os
import glob
from langchain.schema import Document
from PyPDF2 import PdfReader


def load_pdfs(pdf_folder):
    """
    Load PDFs from a folder and return a list of Document objects
    :param pdf_folder: Folder containing PDFs
    :return: List of Document objects
    """
    documents = []
    for pdf_file in glob.glob(os.path.join(pdf_folder, "*.pdf")):
        reader = PdfReader(pdf_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        documents.append(
            Document(
                page_content=text,
                metadata={
                    "source": pdf_file.replace(pdf_folder + "/", "").replace(".pdf", "")
                },
            )
        )
    return documents


def load_markdowns(markdown_folder):
    """
    Load markdown files from a folder and return a list of Document objects
    :param markdown_folder: Folder containing markdown files
    :return: List of Document objects
    """
    documents = []
    for markdown_file in glob.glob(os.path.join(markdown_folder, "*.md")):
        with open(markdown_file, "r") as file:
            text = file.read()
        documents.append(
            Document(
                page_content=text,
                metadata={
                    "source": markdown_file.replace(markdown_folder + "/", "").replace(
                        ".md", ""
                    )
                },
            )
        )
    return documents
