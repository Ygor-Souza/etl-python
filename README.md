Desafio de Projeto Bootcamp Santander

📊Projeto ETL Bancário com FastAPI e Gemini AI

Este projeto implementa um papeline ETL completo integrado a uma API REST em FASTAPI
e enriquecido com IA generativa (Google Gemini) para criação de mensagens personalizadas
aos clientes.


O objetivo é simular um cenário real de dados bancários,
onde informações de clientes são extraídas, transformadas com 
inteligência artificial e carregadas em uma API.


🏗️Arquitetura do Projeto

      etl-santander-python/
      │
      ├── api/
      │   └── main.py          # API FastAPI (clientes, contas, cartões, news)
      │
      ├── etl/
      │   ├── extract.py       # Extração dos dados (mock / JSON / API)
      │   ├── transform.py    # Enriquecimento com IA (Gemini)
      │   └── load.py         # Carga das mensagens na API via HTTP
      │
      ├── requirements.txt
      └── README.md



🪜Fluxo ETL

  1️⃣ Extract

      Busca dados de clientes (nome, conta, saldo, etc.)

      Retorna uma lista de dicionários (list[dict])

  2️⃣ Transform

      Utiliza o modelo gemini-2.5-flash-lite

      Gera mensagens curtas, profissionais e amigáveis

      Exemplo:

      “Olá João Costa! Seu saldo atual é R$1.800,00. Agradecemos sua confiança!”

  3️⃣ Load

      Consome a API FastAPI

      Busca o cliente existente
      
      Adiciona a mensagem no campo news
      
      Atualiza o cliente via PUT



🚀 API FastAPI

  Modelos:
  
      -Account
      -Card
      -Client

  Endpoints disponíveis:
      
      -Post /cliente
      -Get /clientes - Lista todos os clientes
      -Get /cliente/{id} - Lista apenas um cliente por id
      -Put /cliente/{id} - Atualiza cliente (inclui news)
      -Delete /cliente{id} - Remove cliente



▶️ Como executar o projeto
  
        1- Instalar dependências
              pip install -r requirements.txt
        
        2- Subir a API
              uvicorn main:app --reload
        
        3- API disponível em:
              http://127.0.0.1:8000
        
        4- Executar ETL
              python transform.py
              python load.py




🤖 Inteligência Artificial

      Modelo utilizado: gemini-2.5-flash-lite
      
      Escolhido por:
      
      Funcionar no free tier
      
      Baixa latência
      
      Respostas curtas e estáveis
      
      A IA é usada exclusivamente na etapa de transformação, mantendo separação de responsabilidades.
