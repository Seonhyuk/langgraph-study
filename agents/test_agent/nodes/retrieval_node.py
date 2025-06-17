from agents.test_agent.test_state import AgentState
from agents.retrieval.income_retriever import retriever


def retrieve(state: AgentState) -> AgentState:
    query = state["query"]
    docs = retriever.invoke(query)
    return {"context": docs}
