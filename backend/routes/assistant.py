# backend/routes/assistant.py
from fastapi import APIRouter, File, UploadFile, Form
from fastapi.responses import JSONResponse
from backend.utils.pdf_utils import extract_text_from_pdf
from backend.services.chatbot import get_chat_response
from backend.utils.vector_store import create_vector_store_from_pdf
import os
import uuid

router = APIRouter()

UPLOAD_DIR = "data/uploads"

# Ensure upload directory exists
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Keep track of whether a document has been processed
processed_file_path = None

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    """Handles file upload and immediately creates the vector store."""
    global processed_file_path
    try:
        file_path = os.path.join(UPLOAD_DIR, f"{uuid.uuid4()}.pdf")
        with open(file_path, "wb") as f:
            f.write(await file.read())

        extracted_text = extract_text_from_pdf(file_path)
        create_vector_store_from_pdf(extracted_text)  # Create the vector store
        processed_file_path = file_path  # Store the path of the processed file

        return JSONResponse(status_code=200, content={"message": "Document uploaded and processed for chat."})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

# Route: Chatbot Q&A
@router.post("/chat")
async def chat_with_pdf(query: str = Form(...)):
    try:
        response = get_chat_response(query)
        return {"response": response}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

# Route: Summarize PDF (modified to only summarize, assuming processing happened on upload)
@router.post("/summarize")
async def summarize_pdf(file: UploadFile = File(...)):
    try:
        file_path = os.path.join(UPLOAD_DIR, f"{uuid.uuid4()}.pdf")
        with open(file_path, "wb") as f:
            f.write(await file.read())
        extracted_text = extract_text_from_pdf(file_path)
        from backend.services.summarizer import summarize_text  # Import here to avoid circular dependency if any
        summary = summarize_text(extracted_text)
        return {"summary": summary}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

# Route: Generate Quiz (modified to only generate quiz, assuming processing happened on upload)
@router.post("/generate-quiz")
async def quiz_from_pdf(file: UploadFile = File(...), num_questions: int = Form(5)):
    try:
        file_path = os.path.join(UPLOAD_DIR, f"{uuid.uuid4()}.pdf")
        with open(file_path, "wb") as f:
            f.write(await file.read())
        extracted_text = extract_text_from_pdf(file_path)
        from backend.services.quiz_generator import generate_quiz # Import here
        quiz = generate_quiz(extracted_text, num_questions=num_questions)
        return {"quiz": quiz}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})