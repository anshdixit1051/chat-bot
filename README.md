# LangGraph Chatbot

A progressive LangGraph + Streamlit chatbot. Each feature is built on top of the previous one and lives in its own backend/frontend pair, so you can run any stage on its own.

## Versions

| Stage | Backend | Frontend | What it adds |
|---|---|---|---|
| Basic | `langgraph_backend.py` | `streamlit_frontend.py` | Chatbot with in-memory conversation memory |
| Streaming | `langgraph_backend.py` | `streamlit_frontend_streaming.py` | Token-by-token streaming responses |
| Threading | `langgraph_backend.py` | `streamlit_frontend_threading.py` | Multiple chat threads, New chat button |
| Database | `langgraph_database_backend.py` | `streamlit_frontend_database.py` | Persistent chat history (SQLite) |
| Tools | `langgraph_tool_backend.py` | `streamlit_frontend_tool.py` | Tool calling |
| RAG | `langraph_rag_backend.py` | `streamlit_rag_frontend.py` | Chat with your documents |
| MCP | `langgraph_mcp_backend.py` | `streamlit_frontend_mcp.py` | MCP server integration |

## Setup

```
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Create a `.env` file (see `.env.example`):

```
API_KEY=your_api_key_here
BASE_URL=
```

## Run

Run the stage you want:

```
streamlit run streamlit_frontend.py
streamlit run streamlit_frontend_streaming.py
streamlit run streamlit_frontend_threading.py
streamlit run streamlit_frontend_database.py
streamlit run streamlit_frontend_tool.py
streamlit run streamlit_rag_frontend.py
streamlit run streamlit_frontend_mcp.py
```

## Project Structure

```
├── langgraph_backend.py            # basic graph
├── langgraph_database_backend.py   # SQLite persistence
├── langgraph_tool_backend.py       # tool calling
├── langraph_rag_backend.py         # RAG
├── langgraph_mcp_backend.py        # MCP
├── streamlit_frontend.py
├── streamlit_frontend_streaming.py
├── streamlit_frontend_threading.py
├── streamlit_frontend_database.py
├── streamlit_frontend_tool.py
├── streamlit_rag_frontend.py
├── streamlit_frontend_mcp.py
├── requirements.txt
├── .env.example
└── README.md
```

## Tech Stack

Python, LangGraph, LangChain, Streamlit, SQLite, (add your vector store, e.g. Chroma/FAISS), MCP

## Changelog

### Day 1
- Basic chatbot with memory
