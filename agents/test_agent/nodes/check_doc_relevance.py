from agents.test_agent.llm import relevance_doc_prompt, get_llm
from agents.test_agent.test_state import AgentState
from typing import Literal


def check_doc_relevance(state: AgentState) -> Literal["generate", "rewrite"]:
    llm = get_llm()
    context = state["context"]
    query = state["query"]
    doc_relevance_chain = relevance_doc_prompt | llm

    response = doc_relevance_chain.invoke({"question": query, "documents": context})

    if response["Score"] == 1:
        return "generate"

    return "rewrite"
