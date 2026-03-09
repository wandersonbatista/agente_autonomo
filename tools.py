from langchain.tools import tool
from duckduckgo_search import DDGS

@tool
def search_web(query: str) -> str:
    """Busca informações na web."""
    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=3)
        return str(list(results))