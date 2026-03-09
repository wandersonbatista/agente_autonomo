from typing import TypedDict, Optional

class AgentState(TypedDict):
    input: str
    plan: Optional[str]
    search_results: Optional[str]
    action_result: Optional[str]
    final_answer: Optional[str]