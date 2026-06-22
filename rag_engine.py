import os

from dotenv import load_dotenv
import google.generativeai as genai

from pypdf import PdfReader

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# -------------------- GEMINI SETUP --------------------

load_dotenv()

genai.configure(
    api_key=os.getenv("GOOGLE_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

# -------------------- PDF READING --------------------

def extract_text_from_pdf(uploaded_files):

    documents = []

    for pdf in uploaded_files:

        reader = PdfReader(pdf)

        for page_number, page in enumerate(reader.pages):

            text = page.extract_text()

            if text:

                documents.append(

                    Document(

                        page_content=text,

                        metadata={

                            "source": pdf.name,

                            "page": page_number + 1

                        }

                    )

                )

    return documents

# -------------------- CHUNKING --------------------

def split_text_into_chunks(documents):

    splitter = RecursiveCharacterTextSplitter(

        chunk_size=500,

        chunk_overlap=50

    )

    chunks = splitter.split_documents(documents)

    return chunks

# -------------------- VECTOR DATABASE --------------------

def create_vector_store(chunks):

    embeddings = HuggingFaceEmbeddings(

        model_name="sentence-transformers/all-MiniLM-L6-v2"

    )

    vector_store = FAISS.from_documents(

        chunks,

        embeddings

    )

    return vector_store

# -------------------- RETRIEVAL --------------------

def retrieve_relevant_chunks(vector_store, question):

    docs = vector_store.similarity_search(

        question,

        k=10

    )

    return docs

# -------------------- GEMINI --------------------

def ask_gemini(question, docs, chat_history):

    context = ""

    for doc in docs:

        context += (
            f"\nDocument: {doc.metadata.get('source','Unknown')}"
            f"\nPage: {doc.metadata.get('page','?')}"
            f"\nContent:\n{doc.page_content}\n"
        )

    history = ""

    for msg in chat_history:

        history += f"{msg['role']}: {msg['content']}\n"

    prompt = f"""
You are DocuMind.

You answer questions ONLY using the provided document context.

The context may contain information from multiple PDF documents.

If the user asks to compare, summarize or combine documents,
use information from ALL relevant documents.

Conversation History:
{history}

Document Context:
{context}

Question:
{question}

Rules:

- Do not make up information.

- If the answer is not available, reply:
"I couldn't find this information in the uploaded document(s)."

- Mention document names naturally if relevant.

- Keep answers clear and concise.

- Use bullet points whenever appropriate.
"""

    response = model.generate_content(prompt)

    return response.text