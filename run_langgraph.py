from langgraph_agent import compiled_graph

print("✅ SmartDoc LangGraph Agent Ready ✅")

while True:
    query = input("\nAsk your question (or type 'exit' to quit): ")
    if query.lower() in ["exit", "quit"]:
        print("👋 Exiting...")
        break

    state = {"query": query, "output": ""}
    result = compiled_graph.invoke(state)
    print("🟣 Answer:", result["output"])
