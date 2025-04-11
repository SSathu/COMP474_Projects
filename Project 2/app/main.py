from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from langchain_ollama import OllamaLLM
from .models import Query

from .routes import classify_router, chat_router
from .tools import ClassifierTool

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
app.include_router(chat_router)

@app.get("/")
async def root():
    return {"message": "Chatbot is online."}

"""
@app.post('/testing/dbpedia/spotlight')
async def testing(request: Request):
    # EXAMPLE OF HOW TO USE GET_FROM_DBPEDIA_SPOTLIGHT()
    
    data = await request.json()
    
    text = data['text']
    
    annotated_text = get_from_dbpedia_spotlight(text)
    
    return {"response": annotated_text}
"""

# ---LIST-OF-METHODS-TO-USE------

# get_from_dbpedia_spotlight(text)
# returns the entire ressource.
# ressource is a list of dic
