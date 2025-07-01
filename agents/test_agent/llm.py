from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain import hub

load_dotenv()

generate_prompt = hub.pull("rlm/rag-prompt")
relevance_doc_prompt = hub.pull("langchain-ai/rag-document-relevance")

llm = ChatOpenAI(model="gpt-4.1")


def get_llm():
    return llm


