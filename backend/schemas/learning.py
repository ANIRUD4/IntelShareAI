from pydantic import BaseModel
from typing import List

class LearningRequest(BaseModel):
    embedding: List[float]
    explanation: str
    label: str

class LearningResponse(BaseModel):
    status: str
