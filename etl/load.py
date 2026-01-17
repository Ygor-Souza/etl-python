import requests
from transform import users

API_URL = "http://127.0.0.1:8000"


def carregar_mensagem_no_cliente(user: dict):
    cliente_id = user.get("id")
    mensagem = user.get("mensagem")

    if not cliente_id:
        print("Usuário sem ID. Ignorado.")
        return

    if not mensagem:
        print(f"Cliente {cliente_id} sem mensagem. Ignorado.")
        return

    # Busca cliente atual na API
    response = requests.get(f"{API_URL}/cliente/{cliente_id}")

    if response.status_code != 200:
        print(f"Cliente {cliente_id} não encontrado na API.")
        return

    cliente = response.json()

    # Evita duplicar mensagens
    if mensagem in cliente.get("news", []):
        print(f"Mensagem já existe para o cliente {cliente['name']}.")
        return

    # Adiciona a mensagem ao campo news
    cliente["news"].append(mensagem)

    # Atualiza o cliente via PUT
    put_response = requests.put(
        f"{API_URL}/cliente/{cliente_id}",
        json=cliente
    )

    if put_response.status_code == 200:
        print(
        f"Mensagem carregada com sucesso para o cliente "
        f"{cliente.get('name', 'cliente')}"
)

    else:
        print(
            f"Erro ao atualizar cliente {cliente_id}: "
            f"{put_response.status_code} - {put_response.text}"
        )


# ===== EXECUÇÃO DO LOAD =====
if __name__ == "__main__":
    for user in users:
        carregar_mensagem_no_cliente(user)
