# ---------------- pdf_utils.py ----------------
from PyPDF2 import PdfReader




def extract_pdf_text(pdf_path: str) -> str:
text = ""
reader = PdfReader(pdf_path)
for page in reader.pages:
page_text = page.extract_text()
if page_text:
text += page_text
return text