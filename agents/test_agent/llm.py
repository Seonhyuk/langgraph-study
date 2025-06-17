from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain import hub

load_dotenv()

prompt = hub.pull("rlm/rag-prompt")
llm = ChatOpenAI(model="gpt-4.1")


def get_llm():
    return llm


def get_prompt():
    return prompt
