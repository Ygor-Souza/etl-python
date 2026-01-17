#Aqui são feitos os imports da API e biblioteca do Gemini
# e do extract.py criado no projeto
import google.genai as genai
from google.genai import types
import extract

#Chave da API
API_KEY = ""

# Inicializa o client
client = genai.Client(api_key=API_KEY)

def gerar_mensagem(user: dict) -> str: 
    #recebe um usuario(dicionário) e retorna uma string
    
    
    #Pega os dados do usuário de forma segura
    nome = user.get("name", "cliente") 
    saldo = user.get("account", {}).get("balance", 0.0)

    #Da as instruções para a ia de como proceder na resposta
    prompt = (
        f"Escreva UMA mensagem curta (máx. 25 palavras), "
        f"profissional e amigável, para o cliente {nome}, "
        f"informando que seu saldo atual é R${saldo:.2f}."
    )

    #Chamada à API GEMINI
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=prompt
        )

        #Tratamento da respota
        texto = response.text.strip() #remove espaços extras
        return texto[:200]  # proteção extra contra resposta longa
    except Exception as e:
        return f"Erro ao gerar mensagem: {e}"
    #se acabar a quota, cair a internet ou a API falhar o programa não quebra


#ETAPA DE EXTRAÇÃO
users = extract.fetch_users() #Chama o fetch do extract.py com a busca dos usuários em json para lista

#Se não achar usuários faz o exit() 
if not users:
    print("Atenção: Nenhum usuário foi encontrado na extração.")
    exit()

#ETAPA DE TRANSFORMAÇÃO
#Vai percorrer cada cliente e gerar uma mensagem com a IA enrriquecendo o dado
for user in users:
    user["mensagem"] = gerar_mensagem(user)

#ETAPA DE CARGA / VISUALIZAÇÃO
#Confirma que funciounou
print(f"Sucesso! Mensagem do primeiro usuário:\n{users[0]['mensagem']}\n")

#Carrega no terminal
for user in users:
    print(f"Cliente: {user['name']} | Mensagem: {user['mensagem']}")

