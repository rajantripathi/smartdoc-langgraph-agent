# langgraph_agent.py (SIMPLIFIED FIX)

from langgraph.graph import END, StateGraph
from agent import get_llama_agent
from pdf_reader import load_pdf
from pdf_qa_tool import search_pdf, index_documents
from tools import calculator_tool
from typing import TypedDict, Dict, Any

print("🔄 Loading Agent and Indexing PDF ...")

pdf_path = "data/sample.pdf"
documents = load_pdf(pdf_path)
texts, embeddings = index_documents(documents)
agent = get_llama_agent()

print("✅ Agent & PDF Ready inside LangGraph")

# Define State
class AgentState(TypedDict):
    query: str
    output: str

# Build Graph
graph = StateGraph(AgentState)

# -------------------------------
def router_node(state: Dict[str, Any]) -> Dict[str, Any]:
    """
    Route to appropriate node based on the query content
    Returns dict with "next" key indicating which node to go to
    """
    query = state["query"].lower()
    
    if any(op in query for op in ["+", "-", "*", "/", "calculate", "sum", "product", "total", "divide"]):
        return {"next": "calculator"}
    elif any(kw in query for kw in ["pdf", "document", "section", "content", "mention", "retina"]):
        return {"next": "pdf_qa"}
    else:
        return {"next": "llm"}

# -------------------------------
def calculator_node(state: Dict[str, Any]) -> Dict[str, Any]:
    """Handle calculation queries"""
    query = state["query"]
    result = calculator_tool(query)
    return {"output": result}

# -------------------------------
def pdf_qa_node(state: Dict[str, Any]) -> Dict[str, Any]:
    """Handle PDF document queries"""
    query = state["query"]
    result = search_pdf(query, texts, embeddings)
    return {"output": result}

# -------------------------------
def llm_node(state: Dict[str, Any]) -> Dict[str, Any]:
    """Handle general LLM queries"""
    query = state["query"]
    result = agent(query, max_new_tokens=100)
    return {"output": result[0]['generated_text']}

# Build Nodes
graph.add_node("router", router_node)
graph.add_node("calculator", calculator_node)
graph.add_node("pdf_qa", pdf_qa_node)
graph.add_node("llm", llm_node)

# Set entry point
graph.set_entry_point("router")

# Define the conditional edge structure - use a common pattern
# This routes based on the "next" key in the state returned by router_node
graph.add_conditional_edges(
    "router",
    lambda state: state["next"],
    {
        "calculator": "calculator",
        "pdf_qa": "pdf_qa",
        "llm": "llm"
    }
)

# Connect all tools to END
graph.add_edge("calculator", END)
graph.add_edge("pdf_qa", END)
graph.add_edge("llm", END)

compiled_graph = graph.compile()

print("✅ SmartDoc LangGraph Agent Ready ✅")