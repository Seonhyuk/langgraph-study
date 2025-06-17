from agents.test_agent.test_state import AgentState
from agents.test_agent.llm import get_llm, get_prompt


def generate(state: AgentState) -> AgentState:
    llm = get_llm()
    prompt = get_prompt()

    context = state["context"]
    query = state["query"]

    rag_chain = prompt | llm

    response = rag_chain.invoke({"context": context, "question": query})

    return {"answer": response}
