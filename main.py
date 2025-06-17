from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()


def main():
    query = "오늘 날씨 알려줘"
    llm = ChatOpenAI(model="gpt-4.1-nano")

    result = llm.invoke(query)
    print(result)


if __name__ == "__main__":
    main()
