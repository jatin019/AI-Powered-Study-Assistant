from langchain_groq import ChatGroq
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

def generate_quiz(content: str, num_questions: int = 5):
    """
    Generates a multiple-choice quiz based on the provided content.
    """
    try:
        llm = ChatGroq(
            api_key=os.getenv("GROQ_API_KEY"),
            model="llama3-8b-8192",  # You can change this dynamically if needed
        )

        prompt_template = """
        You are a helpful AI that generates quizzes.

        Based on the following educational content, generate {num_questions} multiple-choice questions.
        Each question should have 4 options and indicate the correct answer clearly.

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

        return result.get("text") if isinstance(result, dict) else result

    except Exception as e:
        return f"Quiz generation failed: {e}"
