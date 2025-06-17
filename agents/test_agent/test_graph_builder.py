from langgraph.graph import StateGraph, START, END
from agents.test_agent.test_state import AgentState
from agents.test_agent.nodes.retrieval_node import retrieve
from agents.test_agent.nodes.generate_node import generate

graph_builder = StateGraph(AgentState)

graph_builder.add_node("retrieve", retrieve)
graph_builder.add_node("generate", generate)

graph_builder.add_edge(START, "retrieve")
graph_builder.add_edge("retrieve", "generate")
graph_builder.add_edge("generate", END)

graph = graph_builder.compile()
