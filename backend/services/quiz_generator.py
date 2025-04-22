from langchain_groq import ChatGroq
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os
import re  # Add this import

load_dotenv()



def generate_quiz(content: str, num_questions: int = 10):
    """
    Generates a formatted multiple-choice quiz from given content.
    """
    try:
        llm = ChatGroq(
            api_key=os.getenv("GROQ_API_KEY"),
            model="llama3-8b-8192",
        )

        prompt_template = """
You are an intelligent and professional AI quiz generator.

Based on the educational content provided below, create 10 well-structured and meaningful multiple-choice questions.
Each question should have 4 distinct options (labeled A to D), and clearly mention the correct answer in this format:
"Correct Answer: <Your Answer>"

Follow this structure:
Question 1: <question>
A) Option A
B) Option B
C) Option C
D) Option D

Correct Answer: <Correct Option Letter>) <Option Text>

Repeat the above for each question.

CONTENT:
{content}

QUIZ:
"""

        prompt = PromptTemplate(
            template=prompt_template,
            input_variables=["content", "num_questions"]
        )

        chain = LLMChain(llm=llm, prompt=prompt)
        result = chain.invoke({"content": content, "num_questions": num_questions})

        return result["text"]  # ✅ THIS LINE is essential

    except Exception as e:
        return f"❌ Quiz generation failed: {e}"
