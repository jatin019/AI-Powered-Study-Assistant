# 🎓NeuroMentor AI-Education-app

A smart, real-time study companion built to enhance student learning through instant content summaries, automated quiz creation, and an interactive AI tutor chatbot. The system leverages Groq-powered LLMs, LangChain, FAISS, and Hugging Face embeddings to deliver fast, accurate, and tailored learning experiences.

---

## 🚀 Key Features

- 📄 Upload and process PDF study materials  
- 📝 Generate clear and concise summaries instantly  
- 🧠 Automatically create interactive multiple-choice quizzes  
- 💬 Chat with an AI tutor for contextual doubt resolution  
- ⚡ Ultra-fast inference using Groq LLMs  
- 🔍 Context-aware question answering via Retrieval-Augmented Generation (RAG)  

---

## 🧰 Technology Stack

- **Frontend**: Streamlit  
- **Backend**: FastAPI  
- **LLMs**: Groq API integrated with LangChain  
- **PDF Processing**: PyMuPDF  
- **Embeddings**: Hugging Face Transformers (`all-MiniLM-L6-v2`)  
- **Vector Database**: FAISS  
- **Environment Configuration**: python-dotenv  

---

## 📁 Project Layout

```
frontend/
 └── app.py            # Streamlit-based user interface

backend/
 ├── main.py           # FastAPI application entry point
 ├── routes/
 │    └── assistant.py # API endpoints for chat, summary, quiz, and upload
 ├── services/
 │    ├── summarizer.py      # Summary generation logic
 │    ├── quiz_generator.py # MCQ quiz creation
 │    └── chatbot.py        # RAG-based chatbot logic
 ├── utils/
 │    ├── pdf_utils.py      # PDF text extraction utilities
 │    └── vector_store.py   # FAISS index creation and loading

data/uploads/           # Temporary PDF storage
.env                    # Environment variables
requirements.txt        # Project dependencies
```

---

## ⚙️ Getting Started

### ✅ Requirements

- Python 3.9 or newer  
- Groq API Key (https://console.groq.com/)  
- Git  

---

### 🧪 Installation Steps

1. Clone the repository:
```bash
git clone https://github.com/jatin019/AI-Powered-Study-Assistant.git
cd study-assistant
```

2. Set up a virtual environment:
```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

---

### 🔐 Environment Configuration

Create a `.env` file in the root directory:

```ini
GROQ_API_KEY=your_groq_api_key_here
API_URL=http://127.0.0.1:8000/assistant
```

---

### ▶️ Running the Application

**Launch the Backend**
```bash
uvicorn backend.main:app --reload
```

**Start the Frontend**
```bash
streamlit run frontend/app.py
```

Open your browser at:  
👉 http://localhost:8501

---

## 💡 System Workflow

1. Users upload a PDF via the Streamlit interface.  
2. Text is extracted using PyMuPDF.  
3. Content is chunked and embedded using Hugging Face models.  
4. FAISS stores vectors for efficient similarity search.  
5. LangChain coordinates Groq LLMs for summarization and quiz generation.  
6. The chatbot answers queries using Retrieval-Augmented Generation (RAG).  

---

## 🧪 Practical Use Cases

- Exam preparation through self-assessment quizzes  
- Summarizing long academic documents  
- AI-based tutoring for concept clarification  
- Research paper review and knowledge extraction  

---

## 📌 Planned Enhancements

- 🎤 Voice-based interaction and audio responses  
- ☁️ Cloud storage integration (AWS S3)  
- 📈 Personalized learning paths based on performance  
- 📂 Support for DOCX, PPTX, and TXT formats  

---

## 🧠 Acknowledgements

- Groq  
- LangChain  
- Hugging Face  
- FAISS  
- Streamlit  
- FastAPI  

---

## 📜 License

Licensed and maintained by **© AbhinavYadavwebd**
