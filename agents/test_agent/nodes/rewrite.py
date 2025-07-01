from agents.test_agent.test_state import AgentState
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from agents.test_agent.llm import get_llm

dictionary = ["사람과 관련된 표현 -> 거주자"]

rewrite_prompt = PromptTemplate.from_template(
    f"""
사용자의 질문을 보고, 우리의 사전을 참고해서 사용자의 질문을 변경해주세요.
사전: {dictionary}
질문: {{query}}
"""
)


def rewrite(state: AgentState):
    llm = get_llm()
    query = state["query"]
    rewrite_chain = rewrite_prompt | llm | StrOutputParser()
    response = rewrite_chain.invoke({"query": query})

    return {"query": response}
