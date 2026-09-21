# Gerador de Respostas com Gemini - Python + FastAPI

Projeto que fiz pra praticar integração com API de IA de forma mais séria, indo além de script solto: uma API que recebe uma pergunta e devolve a resposta gerada pelo Gemini (Google).

## O que ele faz

- Recebe um texto via rota POST
- Manda esse texto pra API do Gemini
- Devolve a resposta gerada pela IA, formatada

Não guarda histórico de conversa - cada chamada é independente, então é mais uma API de geração de respostas do que um chatbot.

## Stack

Python 3, FastAPI, Pydantic (validação de dados) e a API do Gemini (Google).

## Estrutura

```
gerador-respostas-gemini/
├── main.py            - rota da API e lógica de integração com o Gemini
├── requirements.txt
├── .env.exemplo
└── README.md
```

A chave da API fica numa variável de ambiente (`.env`), fora do código, por segurança.

## Rodando o projeto

```bash
git clone https://github.com/lheandro/gerador-respostas-gemini.git
cd gerador-respostas-gemini
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Cria um arquivo `.env` na raiz com sua chave:
```
GEMINI_API_KEY=sua_chave_aqui
```

Depois:
```bash
uvicorn main:app --reload
```

Acessa `http://127.0.0.1:8000/docs` pra testar a rota direto no navegador.

---
