from pydantic import BaseModel
from typing import List

class InferenceRequest(BaseModel):
    embedding: List[float]

class InferenceCandidate(BaseModel):
    id: str
    label: str
    confidence: float

class InferenceResponse(BaseModel):
    message: str
    candidates: List[InferenceCandidate]
