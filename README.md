# 🎓 AI-Powered Personalized Study Assistant

An intelligent, real-time learning assistant designed to help students engage with study material through instant summaries, quiz generation, and an AI-powered chatbot. The system uses Groq LLMs, LangChain, FAISS, and Hugging Face embeddings to provide fast, accurate, and personalized learning support.

## 🚀 Features

- 📄 Upload any PDF document
- 📝 Generate a concise summary
- 🧠 Create multiple-choice quizzes
- 💬 Interact with an AI-powered tutor chatbot
- ⚡ Fast inference with Groq LLMs
- 🔍 Context-aware Q&A using Retrieval-Augmented Generation (RAG)

## 🧰 Tech Stack

- **Frontend**: Streamlit
- **Backend**: FastAPI
- **LLMs**: Groq API via LangChain
- **PDF Parsing**: PyMuPDF
- **Embeddings**: Hugging Face Transformers (all-MiniLM-L6-v2)
- **Vector Store**: FAISS
- **Environment Management**: python-dotenv

## 📁 Project Structure

- frontend/
  - app.py – Streamlit user interface
- backend/
  - main.py – FastAPI entrypoint
  - routes/
    - assistant.py – All API endpoints for upload, chat, summarize, and quiz
  - services/
    - summarizer.py – Handles summarization logic
    - quiz_generator.py – Generates multiple-choice quizzes
    - chatbot.py – Provides context-aware answers using RAG
  - utils/
    - pdf_utils.py – PDF text extraction
    - vector_store.py – Creates and loads FAISS vector index
- data/uploads/ – Temporary storage for uploaded files
- .env – Environment variables (e.g., GROQ API key)
- requirements.txt – Python package dependencies

## ⚙️ Getting Started

### ✅ Prerequisites

- Python 3.9 or higher
- Groq API key (https://console.groq.com/)
- Git installed

### 🧪 Installation

1. Clone the repository:
   
```bash
git clone https://github.com/yourusername/study-assistant.git
cd study-assistant
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

### 🔐 Set Up Environment Variables

Create a `.env` file in the root directory with the following content:

```ini
GROQ_API_KEY=your_groq_api_key_here
API_URL=http://127.0.0.1:8000/assistant
```

### ▶️ Running the Application

**Start the Backend Server**
```bash
uvicorn backend.main:app --reload
```

**Start the Streamlit Frontend**
```bash
streamlit run frontend/app.py
```

Then open your browser and go to: http://localhost:8501

## 💡 How It Works

1. Users upload a PDF via the Streamlit interface.
2. Text is extracted using PyMuPDF.
3. Text chunks are embedded using Hugging Face's all-MiniLM-L6-v2 model.
4. Vectors are stored using FAISS for fast retrieval.
5. LangChain uses Groq LLMs to summarize content or generate quizzes.
6. The chatbot uses Retrieval-Augmented Generation (RAG) to answer questions based on the uploaded content.

## 🧪 Example Use Cases

- Students preparing for exams with self-assessment
- Teachers quickly generating quizzes from lecture notes
- Learners summarizing long academic papers
- Researchers extracting key points from technical PDFs

## 📌 Future Enhancements

- 🎤 Voice-based interaction and audio output
- ☁️ Cloud-based PDF storage using AWS S3
- 📈 Personalized learning paths based on quiz performance
- 📂 Multi-format support: DOCX, PPTX, TXT

## 📚 Related Research

| Title | Authors | Year | Summary |
|-------|---------|------|---------|
| AI-Powered Personalized Learning Assistant | Reshma Lohar et al. | 2024 | Personalized tutoring using NLP and ML |
| Personalized Education and AI in US, China, India | Aditi Bhutoria et al. | 2022 | Systematic review of AI-based learning personalization |
| Designing an AI Chatbot for Student Assistance | Bhushan Tiwari et al. | 2022 | Chatbot for handling academic queries via NLP |
| Towards an Intelligent Assistant for Learners | T. Ramesh Kumar et al. | 2021 | ML-driven content recommendation and Q&A |
| Personalized Learning through AI | B. Gargrish & T. Bajaj | 2022 | Adaptive learning platforms with hybrid tutoring |

## 🧠 Acknowledgements

- Groq
- LangChain
- Hugging Face Transformers
- FAISS
- Streamlit
- FastAPI

## 📃 License

MIT License © 2025 Jatin Singh 