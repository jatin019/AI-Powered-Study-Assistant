from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document
import pickle
import os

# Save the vector store
def save_vector_store(vector_store, path="backend/utils/faiss_store.pkl"):
    with open(path, "wb") as f:
        pickle.dump(vector_store, f)

# Create FAISS vector store from extracted text
def create_vector_store_from_pdf(extracted_text: str, save_path="backend/utils/faiss_store.pkl"):
    try:
        # Step 1: Split the text
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        texts = text_splitter.split_text(extracted_text)
        documents = [Document(page_content=text) for text in texts]

        # Step 2: Create embeddings
        embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

        # Step 3: Build FAISS index
        vector_store = FAISS.from_documents(documents, embeddings)

        # Step 4: Save it
        save_vector_store(vector_store, save_path)
        return True
    except Exception as e:
        print(f"❌ Error creating vector store: {e}")
        return False
