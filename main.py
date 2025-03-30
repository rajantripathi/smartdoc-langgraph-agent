import os
from agent import get_llama_agent
from pdf_reader import load_pdf
from tools import calculator_tool
from pdf_qa_tool import index_documents, search_pdf

# Load PDF
pdf_path = os.path.join("data", "sample.pdf")
if not os.path.exists(pdf_path):
    print("❌ PDF file not found!")
    exit()

documents = load_pdf(pdf_path)
print(f"✅ Loaded {len(documents)} documents.")

# Index PDF
texts, embeddings = index_documents(documents)
print("✅ PDF indexed for QA.")

# Load Llama Agent
agent = get_llama_agent()

# Main Loop
while True:
    query = input("Ask your question (use 'calc:' for calculator, 'pdf:' for PDF QA, 'exit' to quit): ")

    if query.lower() in ["exit", "quit"]:
        print("Exiting agent.")
        break

    if query.lower().startswith("calc:"):
        expression = query[5:]
        print(calculator_tool(expression))

    elif query.lower().startswith("pdf:"):
        question = query[4:]
        answer = search_pdf(question, texts, embeddings)
        print("📄 PDF Answer:", answer)

    else:
        output = agent(query, max_new_tokens=100)
        print("💬 Agent:", output[0]['generated_text'])
