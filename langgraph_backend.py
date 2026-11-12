import os
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import InMemorySaver
from langchain_core.messages import BaseMessage
import warnings
warnings.filterwarnings("ignore", category=PendingDeprecationWarning)

load_dotenv()

api_key = os.getenv("API_KEY")
base_url = os.getenv("BASE_URL") or None
if not api_key:
    raise SystemExit("API_KEY not found. Check your .env file.")


def make_model(name: str, **kwargs):
    return ChatAnthropic(
        model=name,
        api_key=api_key,
        base_url=base_url,
        max_tokens=1000,
        **kwargs,
    )


# Simple one-line prompt
prompt = PromptTemplate.from_template("{question}")

# Main model (Opus), plus backups used automatically if it fails
model = make_model("claude-opus-5-5", max_retries=2).with_fallbacks([
    make_model("claude-sonnet-5-5"),
    make_model("claude-haiku-5-5"),
])

class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

def chat_node(state: ChatState):
    messages = state['messages']
    response = model.invoke(messages)
    return {"messages": [response]}

# Checkpointer
checkpointer = InMemorySaver()

graph = StateGraph(ChatState)
graph.add_node("chat_node", chat_node)
graph.add_edge(START, "chat_node")
graph.add_edge("chat_node", END)

chatbot = graph.compile(checkpointer=checkpointer)
