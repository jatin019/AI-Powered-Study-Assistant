from langchain_groq import ChatGroq
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
import os
import pickle

load_dotenv()

# Load FAISS index from the pickle file
def load_vector_store(pickle_path="backend/utils/faiss_store.pkl"):
    try:
        with open(pickle_path, "rb") as f:
            return pickle.load(f)
    except Exception as e:
        print(f"❌ Error loading vector store: {e}")
        return None

# Build chatbot using LangChain's RetrievalQA
def get_chat_response(query: str):
    try:
        vector_store = load_vector_store()
        if not vector_store:
            return "Vector store not found. Please upload and process a document first."

        llm = ChatGroq(
            api_key=os.getenv("GROQ_API_KEY"),
            model="llama3-70b-8192"  # or "llama-3-8b-8192", etc.
        )

        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            retriever=vector_store.as_retriever(),
            chain_type="stuff"
        )

        result = qa_chain.run(query)
        return result
    except Exception as e:
        return f"❌ Chatbot error: {e}"
    

