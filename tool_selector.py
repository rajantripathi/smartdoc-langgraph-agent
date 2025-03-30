from tools import calculator_tool
from pdf_qa_tool import search_pdf

def select_tool(query, texts, embeddings):
    query_lower = query.lower()

    # Detect calculator intent
    if any(op in query_lower for op in ["+", "-", "*", "/", "calculate", "sum", "total", "difference", "product", "multiply", "divide"]):
        return "calculator"

    # Detect PDF-related intent
    elif any(kw in query_lower for kw in ["pdf", "document", "section", "content", "in the pdf", "in the document", "what does the pdf say", "mention"]):
        return "pdf"

    # Default to LLM
    else:
        return "llm"

def run_tool(tool_name, query, texts, embeddings):
    if tool_name == "calculator":
        return calculator_tool(query)
    elif tool_name == "pdf":
        return search_pdf(query, texts, embeddings)
    else:
        return None
