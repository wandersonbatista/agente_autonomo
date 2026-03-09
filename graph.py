from langgraph.graph import StateGraph, END
from state import AgentState
from tools import search_web
from llm import llm

# -------------------
# PLANEJADOR
# -------------------
def planner(state: AgentState):
    prompt = f"""
    Você é um agente autônomo.
    A tarefa é: {state['input']}

    Decida se deve:
    - search (para buscar informações)
    - execute (para executar ação local)

    Responda apenas com: search ou execute
    """

    response = llm.invoke(prompt)
    decision = response.content.strip().lower()

    return {"plan": decision}

# -------------------
# BUSCA
# -------------------
def search_node(state: AgentState):
    result = search_web.invoke(state["input"])
    return {"search_results": result}

# -------------------
# EXECUÇÃO (simples)
# -------------------
def execute_node(state: AgentState):
    return {"action_result": "Ação executada com sucesso."}

# -------------------
# FINAL
# -------------------
def final_node(state: AgentState):
    if state.get("search_results"):
        return {"final_answer": state["search_results"]}
    else:
        return {"final_answer": state["action_result"]}

# -------------------
# CONSTRUÇÃO DO GRAFO
# -------------------
workflow = StateGraph(AgentState)

workflow.add_node("planner", planner)
workflow.add_node("search", search_node)
workflow.add_node("execute", execute_node)
workflow.add_node("final", final_node)

workflow.set_entry_point("planner")

workflow.add_conditional_edges(
    "planner",
    lambda state: state["plan"],
    {
        "search": "search",
        "execute": "execute",
    },
)

workflow.add_edge("search", "final")
workflow.add_edge("execute", "final")
workflow.add_edge("final", END)

app = workflow.compile()