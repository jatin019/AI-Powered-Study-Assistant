from backend.utils.pdf_utils import extract_text_from_pdf
from backend.services.summarizer import summarize_text

pdf_path = "data/uploads/sample.pdf"  # Replace with your actual test PDF path

# Step 1: Extract text
text = extract_text_from_pdf(pdf_path)
print("\n✅ Extracted Text:\n")  # Optional: print preview
#print(text)
# Step 2: Summarize
summary = summarize_text(text)
print("\n📄 Summary:\n", summary)
