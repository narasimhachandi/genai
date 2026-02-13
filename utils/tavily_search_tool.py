from tavily import TavilyClient
from dotenv import load_dotenv
import os
from langchain.tools import tool

load_dotenv()

client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def web_search(query: str, max_results: int = 5) -> str:
    """Search the web for recent information."""
    results = client.search(query=query, max_results=max_results)
    return str(results)