import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    """
    Extracts and returns full text from a given PDF file.
    """
    text = ""
    try:
        with fitz.open(pdf_path) as doc:
            for page in doc:
                text += page.get_text()
        return text
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return ""
