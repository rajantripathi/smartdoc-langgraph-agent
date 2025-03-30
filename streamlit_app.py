import os
import streamlit as st

from agent import get_llama_agent
from pdf_reader import load_pdf
from pdf_qa_tool import index_documents, search_pdf
from tool_selector import select_tool, run_tool
from tools import calculator_tool

# -------------------------
# ⚡ Safe Initial Load ⚡
# -------------------------

if 'agent' not in st.session_state:
    st.session_state.agent = None
if 'texts' not in st.session_state:
    st.session_state.texts = None
if 'embeddings' not in st.session_state:
    st.session_state.embeddings = None

# -------------------------
# ⚡ One-time setup ⚡
# -------------------------

if st.session_state.agent is None:
    st.info("⏳ Loading Agent and PDF... Please wait...")

    pdf_path = os.path.join("data", "sample.pdf")
    if not os.path.exists(pdf_path):
        st.error("❌ PDF not found! Please put your sample.pdf inside the /data folder.")
        st.stop()

    # Load PDF
    documents = load_pdf(pdf_path)

    # Index PDF
    texts, embeddings = index_documents(documents)

    # Load LLM Agent
    agent = get_llama_agent()

    # Save to session state
    st.session_state.agent = agent
    st.session_state.texts = texts
    st.session_state.embeddings = embeddings

    st.success("✅ Agent, PDF, and Tools Loaded Successfully!")

# -------------------------
# ⚡ Streamlit UI ⚡
# -------------------------

st.title("🤖 SmartDoc Agent")

query = st.text_input("Ask something:")

if query:
    # Tool Router
    tool = select_tool(query, st.session_state.texts, st.session_state.embeddings)

    if tool == "calculator":
        result = calculator_tool(query)
        st.write("🔧 Calculator Result:")
        st.success(result)

    elif tool == "pdf":
        result = search_pdf(query, st.session_state.texts, st.session_state.embeddings)
        st.write("📄 PDF Answer:")
        st.info(result)

    else:
        result = st.session_state.agent(query, max_new_tokens=100)
        st.write("💬 Agent Says:")
        st.success(result[0]['generated_text'])
