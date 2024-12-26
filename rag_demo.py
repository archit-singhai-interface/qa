import os
from dotenv import load_dotenv
from langchain_openai import AzureOpenAIEmbeddings, AzureOpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

# Load environment variables
load_dotenv()

# Initialize Azure OpenAI models
embeddings = AzureOpenAIEmbeddings(
    model="gpt-4os",
    api_key=os.getenv("AZURE_OPENAI_EMBEDDING_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_EMBEDDING_ENDPOINT"),
    api_version=os.getenv("AZURE_OPENAI_EMBEDDING_API_VERSION"),
)

llm = AzureOpenAI(
    deployment_name=os.getenv("AZURE_OPENAI_ENGINE"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    temperature=0.5,
    max_tokens=512,
)

# Sample text for demonstration
documents = [
    """
    Artificial Intelligence (AI) is the simulation of human intelligence by machines. 
    Machine Learning is a subset of AI that enables systems to learn from data.
    Deep Learning is a type of Machine Learning that uses neural networks with multiple layers.
    Natural Language Processing (NLP) is a branch of AI that helps machines understand human language.
    Computer Vision is the field of AI that enables machines to interpret visual information.
    """,
    """
    Retrieval Augmented Generation (RAG) combines the power of large language models with external knowledge retrieval.
    RAG helps improve accuracy and provides source attribution for generated responses.
    It works by first retrieving relevant documents from a knowledge base, then using them as context for generation.
    This approach helps reduce hallucinations and keeps responses grounded in factual information.
    """
]

# Split text into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50,
    length_function=len,
)
chunks = text_splitter.create_documents(documents)

# Create vector store
vector_store = FAISS.from_documents(chunks, embeddings)

# Create RAG chain
template = """Use the following pieces of context to answer the question at the end. 
If you don't know the answer, just say that you don't know, don't try to make up an answer.

Context: {context}

Question: {question}

Answer: """

PROMPT = PromptTemplate(
    template=template,
    input_variables=["context", "question"]
)

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vector_store.as_retriever(search_kwargs={"k": 2}),
    chain_type_kwargs={"prompt": PROMPT},
    return_source_documents=True,
)

# Function to ask questions
def ask_question(question: str):
    result = qa_chain({"query": question})
    print("\nQuestion:", question)
    print("\nAnswer:", result["result"])
    print("\nSource Documents:")
    for i, doc in enumerate(result["source_documents"], 1):
        print(f"\n{i}.", doc.page_content.strip())

# Example usage
if __name__ == "__main__":
    questions = [
        "What is artificial intelligence?",
        "How does RAG work?",
        "What are the benefits of using RAG?",
    ]
    
    for question in questions:
        ask_question(question)
        print("\n" + "="*80 + "\n")
