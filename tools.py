def calculator_tool(query: str):
    """
    A simple calculator tool.
    Usage: calculator_tool("2 + 2")
    """
    try:
        result = eval(query)
        return f"The result is {result}"
    except Exception as e:
        return f"Error in calculation: {str(e)}"
