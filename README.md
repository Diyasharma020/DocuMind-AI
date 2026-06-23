# 📄 DocuMind AI

An AI-powered multi-document Retrieval-Augmented Generation (RAG) system that enables users to interact with PDF documents using natural language. The application performs semantic search over uploaded documents and generates context-aware responses using Google Gemini 2.5 Flash.

---

## ✨ Features

* 📂 Upload one or multiple PDF documents
* 💬 Chat with documents using natural language
* 🔍 Semantic search with FAISS Vector Database
* 🤖 Context-aware responses powered by Google Gemini 2.5 Flash
* 🧠 Hugging Face sentence embeddings
* 💭 Multi-turn conversational memory
* 📥 Download chat history
* 📑 View retrieved document chunks with page metadata
* ⚡ Interactive Streamlit interface

---

## 🛠 Tech Stack

* Python
* Streamlit
* Google Gemini API
* LangChain
* FAISS
* Hugging Face Embeddings
* PyPDF
* python-dotenv

---

## 🏗 Project Architecture

```text
PDF Upload(s)
      │
      ▼
Text Extraction (PyPDF)
      │
      ▼
Recursive Text Chunking
      │
      ▼
Hugging Face Embeddings
      │
      ▼
FAISS Vector Database
      │
      ▼
Semantic Retrieval
      │
      ▼
Google Gemini 2.5 Flash
      │
      ▼
Context-Aware Answer Generation
```

---

## 📂 Project Structure

```text
DocuMind/
│
├── app.py
├── rag_engine.py
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
└── venv/
```

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/Diyasharma020/DocuMind-AI.git
cd DocuMind-AI
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

**Windows**

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GOOGLE_API_KEY=YOUR_API_KEY_HERE
```

Run the application

```bash
streamlit run app.py
```

---

## 📸 Screenshots

<img width="1895" height="815" alt="Screenshot 2026-06-23 181839" src="https://github.com/user-attachments/assets/e6b268a7-1ea6-4b5d-ab5c-5c8863a521c4" />
<img width="1880" height="772" alt="Screenshot 2026-06-23 183133" src="https://github.com/user-attachments/assets/698902a9-e884-4dfa-bee5-5592167e9dfa" />
<img width="1912" height="812" alt="Screenshot 2026-06-23 183141" src="https://github.com/user-attachments/assets/f0cb54e2-1ab1-48aa-9f72-ca813f605f74" />


---

## 👩‍💻 Author

**Diya Sharma**
