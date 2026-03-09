from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3",
    temperature=0
)

def run_agent(question, context):
    prompt = f"""
Responda a pergunta do usuário de forma clara e direta.

Pergunta:
{question}

Informações encontradas na internet:
{context}

Resposta:
"""

    return llm.invoke(prompt).content