from fastapi import APIRouter, File, UploadFile, Form
from fastapi.responses import JSONResponse
from backend.utils.pdf_utils import extract_text_from_pdf
from backend.services.summarizer import summarize_text
from backend.services.quiz_generator import generate_quiz
from backend.services.chatbot import get_chat_response
import os
import uuid

router = APIRouter()

UPLOAD_DIR = "data/uploads"

# Ensure upload directory exists
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Route: Summarize PDF
@router.post("/summarize")
async def summarize_pdf(file: UploadFile = File(...)):
    try:
        file_path = os.path.join(UPLOAD_DIR, f"{uuid.uuid4()}.pdf")
        with open(file_path, "wb") as f:
            f.write(await file.read())

        extracted_text = extract_text_from_pdf(file_path)
        summary = summarize_text(extracted_text)

        return {"summary": summary}

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

# Route: Generate Quiz
@router.post("/generate-quiz")
async def quiz_from_pdf(file: UploadFile = File(...), num_questions: int = Form(5)):
    try:
        file_path = os.path.join(UPLOAD_DIR, f"{uuid.uuid4()}.pdf")
        with open(file_path, "wb") as f:
            f.write(await file.read())

        extracted_text = extract_text_from_pdf(file_path)
        quiz = generate_quiz(extracted_text, num_questions=num_questions)

        return {"quiz": quiz}

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
