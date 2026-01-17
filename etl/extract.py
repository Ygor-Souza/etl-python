import pandas as pd
from pathlib import Path
import requests
import json

BASE_DIR = Path(__file__).resolve().parent.parent
csv_path = BASE_DIR / 'data' / 'clientes.csv'

df = pd.read_csv(csv_path)
user_ids = df['UserID'].tolist()

print("IDs encontrados:", user_ids)

# recuperar usuário
def get_user(id):
    response = requests.get(f'http://127.0.0.1:8000/cliente/{id}')
    return response.json() if response.status_code == 200 else None

# criar lista de usuários válidos
users = [user for id in user_ids if (user := get_user(id)) is not None]

def fetch_users():
    df = pd.read_csv(csv_path)
    user_ids = df['UserID'].tolist()

    users = []

    for user_id in user_ids:
        response = requests.get(f'http://127.0.0.1:8000/cliente/{user_id}')
        if response.status_code == 200:
            users.append(response.json())

    return users

# imprimir em JSON legível
print(json.dumps(users, indent=3))
