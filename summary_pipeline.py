# ---------------- summary_pipeline.py ----------------
import os
from docx import Document
from pdf_utils import extract_pdf_text
from llm_utils import run_prompt


PROMPT_DIR = "prompts"




def load_prompt(name: str) -> str:
with open(os.path.join(PROMPT_DIR, name), "r", encoding="utf-8") as f:
return f.read()




def save_doc(text: str, path: str):
doc = Document()
doc.add_paragraph(text)
doc.save(path)




def process_pdfs(input_dir: str, output_dir: str):
interrogation_prompt = load_prompt("interrogation.txt")
integration_prompt = load_prompt("integration.txt")
meta_prompt = load_prompt("meta.txt")


summaries = []


for file in os.listdir(input_dir):
if not file.lower().endswith(".pdf"):
continue


pdf_path = os.path.join(input_dir, file)
text = extract_pdf_text(pdf_path)


interrogation = run_prompt(interrogation_prompt, text)
integration = run_prompt(integration_prompt, text)


base = os.path.splitext(file)[0]
save_doc(interrogation, os.path.join(output_dir, f"{base}_interrogation.docx"))
save_doc(integration, os.path.join(output_dir, f"{base}_integration.docx"))


summaries.append(interrogation + "\n" + integration)


# Meta-analysis
combined = "\n---\n".join(summaries)
meta = run_prompt(meta_prompt, combined, max_tokens=2000)
save_doc(meta, os.path.join(output_dir, "meta_analysis.docx"))