from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from langchain_ollama import OllamaLLM

from routes import classify_router
from tools.classifier import ClassifierTool

import os

@asynccontextmanager
async def lifespan(app: FastAPI):
    llm = OllamaLLM(
        model="gemma3:4b",
        base_url=os.getenv("OLLAMA_HOST")
    )
    app.state.classifier = ClassifierTool(llm)
    yield
    if hasattr(app.state, 'classifier'):
        await app.state.classifier.cleanup()

app = FastAPI(title="Multi-Agent Chatbot API", lifespan=lifespan)
app.include_router(classify_router)

@app.get("/")
async def root():
    return {"message": "Hello World!"}

@app.post('/testing')
async def testing(request: Request):
    
    data = await request.json()
    
    return {"response": data}