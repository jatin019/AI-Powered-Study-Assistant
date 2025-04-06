from backend.utils.pdf_utils import extract_text_from_pdf

pdf_path = "data/uploads/sample.pdf"  # Replace with your actual test PDF path

extracted_text = extract_text_from_pdf(pdf_path)

print("\nExtracted Text Preview:\n")
print(extracted_text)  # Print the first 1000 characters
