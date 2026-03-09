from langchain.tools import tool
from ddgs  import DDGS

def search_web(query: str) -> str:
    results_text = []

    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=3)

        for r in results:
            results_text.append(r["body"])

    return "\n".join(results_text)