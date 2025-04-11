from fastapi import APIRouter
from ..models import Query
from .classifier import clean_text
import asyncio

router = APIRouter(prefix="/api/v1")

@router.post("/chat")
async def chat(query: Query):
   response_obj = await clean_text(query)
   return response_obj.body