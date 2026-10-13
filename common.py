import os
from typing import List, Dict, Any, Optional, Annotated, TypedDict
from dotenv import load_dotenv  # Load environment variables from .env file

# Pydantic for data modeling / validation
from pydantic import BaseModel, Field

# LangChain & LangGraph components
from langchain_nebius import ChatNebius  # Nebius LLM wrapper
from langchain_tavily import TavilySearch  # Tavily search tool integration
from langchain_core.prompts import ChatPromptTemplate  # For structuring prompts
from langgraph.graph import StateGraph, END  # Build a state machine graph
from langgraph.prebuilt import ToolNode, tools_condition  # Prebuilt nodes & conditions

# For pretty printing output
from rich.console import Console  # Console styling
from rich.markdown import Markdown  # Render markdown in terminal


import os
from anthropic import Anthropic

load_dotenv(override=True)


API_KEY = os.environ.get('ANTHROPIC_AUTH_TOKEN')
API_BASE = os.environ.get('ANTHROPIC_BASE_URL')
LLM_MODEL = os.environ.get('ANTHROPIC_DEFAULT_SONNET_MODEL')

print(f"API_BASE:{API_BASE}")
print(f"model:{LLM_MODEL}")
