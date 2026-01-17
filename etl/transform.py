import google.genai as genai
from google.genai import types
import extract

API_KEY = ""

client = genai.Client(api_key=API_KEY)

def gerar_mensagem(user: dict) -> str | None:
    nome = user.get("nome", "Cliente")
    saldo = user.get("account", {}).get("balance", 0.0)

    prompt = (
        f"Escreva APENAS uma mensagem curta e profissional, "
        f"com no máximo 2 linhas. "
        f"Use EXATAMENTE o nome '{nome}' e NÃO use placeholders. "
        f"Informe que o saldo atual é R${saldo:.2f}."
    )

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=prompt
        )
        return response.text.strip()

    except Exception as e:
        print(f"[IA] Falha ao gerar mensagem para cliente {user.get('id')}: {e}")
        return None


#EXTRAÇÃO
users = extract.fetch_users()

for user in users:
    mensagem = gerar_mensagem(user)

    if mensagem and "[Nome do Cliente]" not in mensagem:
        user["mensagem"] = mensagem
    else:
        user["mensagem"] = None

#TRANSFORMAÇÃO
for user in users:
    user["mensagem"] = gerar_mensagem(user)


for user in users:
    print(
        f"Cliente: {user.get('name', 'cliente')} | "
        f"Mensagem: {user['mensagem']}"
    )
