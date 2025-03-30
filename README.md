# SmartDoc LangGraph Agent

SmartDoc LangGraph Agent is a simple prototype demonstrating how to combine:
- **LLM Agent** (TinyLlama)
- **PDF Querying** using LangChain's vector store
- **Calculator Tool**
- **LangGraph** for orchestrating tool selection
- **Streamlit UI**

This agent can answer:
- PDF-based questions
- General LLM questions
- Simple arithmetic calculations

developed as part of a learning exercise.

---

## Features

✅ PDF Document Question Answering

✅ Calculator for Simple Math Queries

✅ General Purpose Question Answering

✅ Dynamic Routing via LangGraph

✅ Streamlit-based simple UI

✅ Compatible with HuggingFace Transformers

✅ CPU Friendly (runs on normal laptops)

---

## Requirements

- Python 3.10+
- Anaconda (recommended)
- git
- [Hugging Face Token](https://huggingface.co/settings/tokens) (required to download TinyLlama)

---

## Installation

```bash
# Clone this repo
https://github.com/rajantripathi/smartdoc-langgraph-agent.git
cd smartdoc-langgraph-agent

# Create virtual environment (Recommended)
conda env create -f environment.yml
conda activate agentenv

# Or install manually
pip install -r requirements.txt
```

---

## Usage

### 1️⃣ CLI Version
```bash
python run_langgraph.py
```

### 2️⃣ Streamlit UI
```bash
streamlit run streamlit_app.py
```

---

## Folder Structure
```
smartdoc-langgraph-agent/
├── agent.py
├── langgraph_agent.py
├── pdf_reader.py
├── pdf_qa_tool.py
├── tools.py
├── tool_selector.py
├── run_langgraph.py
├── streamlit_app.py
├── requirements.txt
├── environment.yml
├── data/
│   └── sample.pdf
└── .env.example
```

---

## Notes
- The project demonstrates how you can create simple agents using `LangGraph`
- You can swap TinyLlama with any small HF model easily
- This is a base for further experimentation

---

## Credits
Built by [Rajan Tripathi](https://github.com/rajantripathi) with support from LangGraph, LangChain, and HuggingFace libraries.

---

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
