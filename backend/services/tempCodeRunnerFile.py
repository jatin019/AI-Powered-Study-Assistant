from langchain_groq import Groq  # <-- new correct import
from langchain.chains.summarize import load_summarize_chain
from langchain.docstore.document import Document
from dotenv import load_dotenv
import os

load_dotenv()

def summarize_text(content: str):
    try:
        llm = Groq(
            api_key=os.getenv("GROQ_API_KEY"),
            model="mixtral-8x7b-32768",
        )
        docs = [Document(page_content=content)]
        chain = load_summarize_chain(llm, chain_type="stuff")
        summary = chain.run(docs)
        return summary
    except Exception as e:
        return f"Summarization failed: {e}"
