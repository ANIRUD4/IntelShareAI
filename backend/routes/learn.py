from fastapi import APIRouter
from uuid import uuid4
from datetime import datetime

from backend.schemas.learning import LearningRequest, LearningResponse
from backend.schemas.knowledge_unit import KnowledgeUnit
from backend.storage_manager import save_knowledge_unit

router = APIRouter(prefix="/learn")

@router.post("/commit", response_model=LearningResponse)
def commit_learning(req: LearningRequest):
    unit = KnowledgeUnit(
        id=str(uuid4()),
        label=req.label,
        embedding=req.embedding,
        confidence=1.0,  # initial confidence
        explanation=req.explanation,
        created_at=datetime.utcnow()
    )

    save_knowledge_unit(unit.model_dump())

    return LearningResponse(status="stored")
