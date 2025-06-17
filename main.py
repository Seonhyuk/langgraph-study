from agents.test_agent.test_graph_builder import graph


def main():
    query = "연봉 5천만원 직장인의 소득세는?"

    initial_state = {"query": query}

    result = graph.invoke(initial_state)
    print(result)


if __name__ == "__main__":
    main()
