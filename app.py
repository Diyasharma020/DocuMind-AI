import streamlit as st

from rag_engine import (
    extract_text_from_pdf,
    split_text_into_chunks,
    create_vector_store,
    retrieve_relevant_chunks,
    ask_gemini
)

st.set_page_config(
    page_title="DocuMind AI",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------- Session State --------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

if "chunks" not in st.session_state:
    st.session_state.chunks = None

if "processed" not in st.session_state:
    st.session_state.processed = False

# -------------------- Sidebar --------------------

with st.sidebar:

    st.title("🤖 DocuMind AI")

    st.markdown(
    """
    AI-powered document analytics built using
    - Gemini 2.5 Flash
    - LangChain
    - FAISS
    - HuggingFace Embeddings
    - Streamlit
    """
    )

    st.divider()

    uploaded_files = st.file_uploader(
        "Upload one or more PDFs",
        type=["pdf"],
        accept_multiple_files=True
    )

    if uploaded_files:

        if not st.session_state.processed:

            with st.spinner(
                "📄 Reading PDFs...\n\nCreating embeddings...\n\nBuilding vector database..."
            ):

                documents = extract_text_from_pdf(uploaded_files)

                chunks = split_text_into_chunks(documents)

                vector_store = create_vector_store(chunks)

                st.session_state.vector_store = vector_store
                st.session_state.chunks = chunks
                st.session_state.processed = True

            st.success("✅ Documents indexed successfully. You can now start chatting.")

    st.divider()

    if uploaded_files:

        st.metric(
            "Conversation",
            len(st.session_state.messages)
        )

    st.divider()

    if st.button("🗑 Clear Chat"):

        st.session_state.messages = []

        st.rerun()

# -------------------- Main Screen --------------------

st.title("🤖 DocuMind AI")

st.markdown(
"""
### Your Intelligent Document Assistant

Upload one or multiple PDF documents and ask questions using
**Retrieval-Augmented Generation (RAG)** powered by **Gemini AI**.
"""
)

# Show previous conversation

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.write(message["content"])

# Ask Question

if st.session_state.vector_store:

    question = st.chat_input("Ask something about your documents...")

    if question:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        with st.chat_message("user"):

            st.write(question)

        docs = retrieve_relevant_chunks(
            st.session_state.vector_store,
            question
        )

        with st.spinner("🤖 Gemini is analyzing your documents..."):

            answer = ask_gemini(
                question,
                docs,
                st.session_state.messages
            )

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

        with st.chat_message("assistant"):

            st.write(answer)

        with st.expander("🔍 Context Retrieved for Answer"):

            for i, doc in enumerate(docs):

                st.markdown(f"### Chunk {i+1}")

                st.write(doc.page_content)

                if hasattr(doc, "metadata"):

                    st.caption(
                        f"📄 {doc.metadata.get('source','Unknown')} | Page {doc.metadata.get('page','?')}"
                    )


else:

    st.info("👈 Upload one or more PDFs from the sidebar to begin.")
st.divider()

st.caption(
    "Built with ❤️ using Streamlit • Gemini • LangChain • FAISS"
)