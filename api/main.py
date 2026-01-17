from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title= "API Bancária")

class Account(BaseModel):
  id: int
  number: str
  agency: str
  balance: float
  limit: float

class Card(BaseModel):
  id: int
  number: str
  limit: float

class Client(BaseModel):
  id: int
  name: str
  account: Account
  card: Card
  features: list[str] = []
  news: List[str] = []

clientes_db: List[Client] = []


# http://127.0.0.1:8000/rota


@app.post("/cliente")
def criar_cliente(cliente: Client):

  for c in clientes_db:
    if c.id == cliente.id:
      raise HTTPException(status_code=400, detail="Cliente já existe")
  
  clientes_db.append(cliente)
  return {"mensagem": "Cliente criado com sucesso", "cliente": cliente}

@app.get("/clientes")
def listar_clientes():
  return clientes_db


@app.get("/cliente/{cliente_id}")
def obter_cliente(cliente_id: int):
  for cliente in clientes_db:
    if cliente.id == cliente_id:
      return cliente
    
  raise HTTPException(status_code=404, detail="Cliente não encontrado")

@app.delete("/cliente/{cliente_id}")
def deletar_cliente(cliente_id: int):
  for index, cliente in enumerate(clientes_db):
    if cliente.id == cliente_id:
      clientes_db.pop(index)
      return {"mensagem": "Cliente removido com sucesso"}
  
  raise HTTPException(status_code=4004, detail="Cliente não encontrado")

@app.put("/cliente/{cliente_id}")
def atualizar_cliente(cliente_id: int, cliente_atualizado: Client):

  for index, cliente in enumerate(clientes_db):
    if cliente.id == cliente_id:

      cliente_atualizado.id = cliente_id

      clientes_db[index] = cliente_atualizado

      return{
        "mensagem": "Cliente atualizado com sucesso",
        "cliente": cliente_atualizado
      }
    
  raise HTTPException(status_code=404, detail="Cliente não encontrado")

# uvicorn main:app --reload - rodar a api
