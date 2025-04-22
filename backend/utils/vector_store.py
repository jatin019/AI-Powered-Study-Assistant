from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document
import pickle
import os
import hashlib


# Generate a unique hash from the PDF text
def get_text_hash(text: str):
    return hashlib.md5(text.encode('utf-8')).hexdigest()


# Save the vector store
def save_vector_store(vector_store, path: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as f:
        pickle.dump(vector_store, f)


# Create FAISS vector store from extracted text
def create_vector_store_from_pdf(extracted_text: str, base_dir="backend/utils/"):
    try:
        # Generate a hash of the content to identify it uniquely
        file_hash = get_text_hash(extracted_text)
        save_path = os.path.join(base_dir, f"faiss_store_{file_hash}.pkl")

        # Check if vector store already exists
        if os.path.exists(save_path):
            print(f"✅ Vector store already exists for this file: {save_path}. Skipping creation.")
            return False  # No need to regenerate

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
        print(f"✅ New vector store saved at: {save_path}")
        return True

    except Exception as e:
        print(f"❌ Error creating vector store: {str(e)}")
        import traceback
        traceback.print_exc()
        return False
