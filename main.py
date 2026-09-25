import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from google import genai
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

api_key = os.getenv("GEMINI_API_KEY")

if api_key:
   client = genai.Client(api_key=api_key)
else:
   client = None

class Pergunta(BaseModel):
   prompt: str

@app.get("/")
async def home():
   return {"message": "Olá"}

@app.get("/status")
async def status():
   return {"status": "Operational"}

@app.post("/perguntar")

async def generate_response(questao: Pergunta):
   if not api_key:
       raise HTTPException(
           status_code=500,
           detail="A chave da API do Gemini não foi configurada."
       )

   try:
       response = client.models.generate_content(
           model="gemini-3.6-flash",
           contents=questao.prompt
       )
   except Exception as erro:
       raise HTTPException(
           status_code=502,
           detail=f"Falha ao acessar a API do Gemini: {erro}"
       ) from erro

   return {"response": response.text}


