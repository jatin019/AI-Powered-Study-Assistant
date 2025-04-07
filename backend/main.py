# backend/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routes import assistant

app = FastAPI(
    title="AI Study Assistant API",
    description="Provides summarization, quiz generation, and chatbot functionality from PDF files.",
    version="1.0.0"
)

# CORS settings — adjust for your frontend domain if needed
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can change this to your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include your assistant routes
app.include_router(assistant.router, prefix="/assistant")

# Root route (optional)
@app.get("/")
def root():
    return {"message": "Welcome to the AI Study Assistant API"}
