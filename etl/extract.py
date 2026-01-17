import pandas as pd
from pathlib import Path
import requests
import json


BASE_DIR = Path(__file__).resolve().parent.parent
csv_path = BASE_DIR / 'data' / 'clientes.csv'

df = pd.read_csv(csv_path)
user_ids = df['UserID'].tolist()

# recuperar usuário
def get_user(id):
  response = requests.get(f'http://127.0.0.1:8000/cliente/{id}')
  return response.json() if response.status_code == 200 else None

def fetch_users():
  df = pd.read_csv(csv_path)
  user_ids = df['UserID'].tolist()
  users = [user for id in user_ids if (user := get_user(id)) is not None]
  return users

users = [user for id in user_ids if(user := get_user(id)) is not None] # percorre cada id e para cada id faz uma chamada na função get_user
print(json.dumps(users, indent=3))


