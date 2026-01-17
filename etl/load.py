import requests
from transform import users

API_URL = "http://127.0.0.1:8000"

def carregar_mensagem_no_cliente(user:dict):
  cliente_id = user["id"]
  mensagem = user.get("mensagem")

  if not mensagem:
    print(f"Cliente {cliente_id} sem mensagem. Ignorado.")
    return
  
  #busca cliente atual
  response = requests.get(f"{API_URL}/cliente/{cliente_id}")

  if response.status_code != 200:
    print(f"Cliente {cliente_id} não encontrado na API.")
    return
  
  cliente = response.json()

  #Adiciona a mensagem em news
  cliente["news"].append(mensagem)

  #Atualiza o cliente via PUT

  put_response = requests.put(
    f"{API_URL}/cliente/{cliente_id}",
    json=cliente
  )

  if put_response.status_code == 200:
    print(f"Mensagem carregada com sucesso para o cliente {cliente['name']}")
  else:
    print(f"Erro ao atualizar cliente {cliente_id}: {put_response.text}")


for user in users:
    carregar_mensagem_no_cliente(user)
