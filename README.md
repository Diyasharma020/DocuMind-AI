# 📄 DocuMind AI

An AI-powered document analytics system that enables users to chat with one or more PDF documents using Retrieval-Augmented Generation (RAG). The application performs semantic search over uploaded documents and generates context-aware responses using Google's Gemini API.

---

## ✨ Features

- 📂 Upload one or multiple PDF documents
- 💬 Chat with your documents using natural language
- 🔍 Semantic search using FAISS Vector Database
- 🤖 Context-aware responses powered by Gemini 2.5 Flash
- 🧠 Hugging Face sentence embeddings
- 💭 Multi-turn conversation history
- 📥 Download chat history
- 📑 View retrieved context chunks with page numbers
- ⚡ Interactive Streamlit interface

---

## 🛠 Tech Stack

- Python
- Streamlit
- Google Gemini API
- LangChain
- FAISS
- Hugging Face Embeddings
- PyPDF
- python-dotenv

---

## 🏗 Project Architecture

```text
PDF Upload
      │
      ▼
Extract Text (PyPDF)
      │
      ▼
Document Chunking
      │
      ▼
HuggingFace Embeddings
      │
      ▼
FAISS Vector Store
      │
      ▼
Similarity Search
      │
      ▼
Gemini 2.5 Flash
      │
      ▼
Answer Generation
```

---

## 🚀 Installation

Clone the repository

```bash
git clone <your-repository-link>
cd DocuMind
```

Create a virtual environment

```bash
python -m venv venv
```

Activate it

Windows

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

Example:

- Home Page
- Upload PDFs
- Chat Interface
- Retrieved Context

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

## 👩‍💻 Author

**Diya Sharma**

LinkedIn: https://www.linkedin.com/in/diya-sharma12
