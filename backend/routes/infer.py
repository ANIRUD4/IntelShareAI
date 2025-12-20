from fastapi import APIRouter

from backend.schemas.inference import (
    InferenceRequest,
    InferenceResponse,
    InferenceCandidate
)
from backend.storage_manager import load_all_units

router = APIRouter(prefix="/infer")

@router.post("/", response_model=InferenceResponse)
def infer_object(req: InferenceRequest):
    units = load_all_units()

    candidates = [
        InferenceCandidate(
            id=u["id"],
            label=u["label"],
            confidence=u["confidence"]
        )
        for u in units
    ]

    return InferenceResponse(
        message="I think it might be one of these. Please confirm.",
        candidates=candidates
    )
