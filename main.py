from tools import search_web
from agent import run_agent

while True:
    question = input("\nVocê: ")

    if question.lower() in ["sair", "exit"]:
        break

    context = search_web(question)
    answer = run_agent(question, context)

    print(f"\nAgente: {answer}")