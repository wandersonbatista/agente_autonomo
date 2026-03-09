from graph import app

while True:
    user_input = input("\nVocê: ")

    if user_input.lower() == "sair":
        break

    result = app.invoke({"input": user_input})

    print("\nAgente:", result["final_answer"])