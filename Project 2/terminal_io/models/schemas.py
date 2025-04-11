from pydantic import BaseModel
from typing import Literal, Optional

class Query(BaseModel):
    text: str

AgentType = Literal["ai", "admissions", "general"]

class ClassificationResult(BaseModel):
    agent: AgentType
    debug_info: Optional[dict] = None