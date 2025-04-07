from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from langchain.docstore.document import Document
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

def summarize_text(content: str):
    try:
        llm = ChatGroq(
            api_key=os.getenv("GROQ_API_KEY"),
            model="llama-3.3-70b-versatile",
        )
        
        # Create a detailed summary prompt template
        prompt_template = """
        Write a short and to the point summary of the following text. 
        Include all key points, methodologies, and important information.
        
        
        TEXT: {text}
        
        DETAILED SUMMARY:
        """
        
        prompt = PromptTemplate(template=prompt_template, input_variables=["text"])
        
        # Create the document
        docs = [Document(page_content=content)]
        
        # Create the chain with the custom prompt using "stuff" chain type for shorter documents
        chain = load_summarize_chain(
            llm,
            chain_type="stuff",
            prompt=prompt,
        )
        
        # Invoke the chain
        result = chain.invoke(docs)
        
        # Extract just the summary text from the result
        if isinstance(result, dict) and "output_text" in result:
            return result["output_text"]
        return result
    except Exception as e:
        return f"Summarization failed: {e}"