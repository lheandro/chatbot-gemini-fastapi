import os
from fastapi import FastAPI
from pydantic import BaseModel
from google import genai
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

class Pergunta(BaseModel):
    prompt: str

@app.post("/Perguntar")

async def generate_response(questao: Pergunta):
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=questao.prompt
    )
    return {"response": response.text}


