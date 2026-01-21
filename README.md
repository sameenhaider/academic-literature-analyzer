# 📚 Academic Literature Analyzer

A Python-based automation tool that analyzes **user-provided academic PDF papers** using Large Language Models (LLMs).  
It extracts text, generates structured summaries, and produces a meta-analysis across multiple research papers.

---

## 🚀 Features

- 📄 PDF text extraction  
- 🧠 Interrogation summaries (critical analysis)  
- 🔗 Integration summaries (conceptual linking)  
- 📊 Meta-analysis across multiple papers  
- 📝 Automatic DOCX report generation  

---

## 🛠️ Tech Stack

- **Python**
- **PyPDF2**
- **OpenAI API**
- **python-docx**
- **requests**
- **googlesearch**

---

## 📂 Project Structure

```text
academic-literature-analyzer/
│
├── main.py
├── interrogation.txt
├── integration.txt
├── meta.txt
├── input_pdfs/
│   └── (your academic PDFs here)
├── output_docs/
│   └── (generated DOCX reports)
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Configure OpenAI API key

**Windows (PowerShell):**
```powershell
setx OPENAI_API_KEY "your_api_key_here"
```

**Linux / macOS:**
```bash
export OPENAI_API_KEY="your_api_key_here"
```

---

## ▶️ Usage

### 1️⃣ Add PDFs  
Place academic papers inside the `input_pdfs/` folder.

### 2️⃣ Run the analyzer
```bash
python main.py
```

### 3️⃣ View results  
Generated DOCX reports will appear in the `output_docs/` folder.

---

## 📌 Output

- Individual paper summaries  
- Integrated cross-paper insights  
- Final meta-analysis document  

All outputs are saved in **DOCX format** for easy editing and sharing.

---

## ⚠️ Legal & Ethical Notice

This tool processes **only user-supplied documents**.  
It does **not** bypass paywalls or scrape restricted academic content.  
Users are responsible for ensuring compliance with copyright laws.

---

## 📄 License

This project is provided for **educational and research purposes only**..
