from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from langchain_ollama import OllamaLLM

from routes import classify_router
from tools.classifier import ClassifierTool
from tools.dbpediaAPI import get_from_dbpedia_spotlight

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
    
    lorem_ipsum = """
Lorem ipsum dolor sit amet, consectetur a
dipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""
    
    return {"response": lorem_ipsum}

@app.post('/testing/dbpedia/spotlight')
async def testing(request: Request):
    # EXAMPLE OF HOW TO USE GET_FROM_DBPEDIA_SPOTLIGHT()
    
    data = await request.json()
    
    text = data['text']
    
    annotated_text = get_from_dbpedia_spotlight(text)
    
    return {"response": annotated_text}

@app.post("/chat")
async def chat(request: Request):
    
    data = await request.json()
    
    text = data['text']
    
    pass



# ---LIST-OF-METHODS-TO-USE------

# get_from_dbpedia_spotlight(text)
# returns the entire ressource.
# ressource is a list of dic