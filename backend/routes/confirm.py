from fastapi import APIRouter, HTTPException


from backend.schemas.confirmation import (
    ConfirmationRequest,
    ConfirmationResponse
)
from backend.storage_manager import load_all_units, save_knowledge_unit

router = APIRouter(prefix="/confirm")

@router.post("/", response_model=ConfirmationResponse)
def confirm_knowledge(req: ConfirmationRequest):
    units = load_all_units()

    for unit in units:
        if unit["id"] == req.knowledge_unit_id:

            # Case 1: Human confirms the prediction
            if req.confirmed:
                unit["confidence"] = min(unit.get("confidence", 1.0) + 0.1, 1.0)

            # Case 2: Human rejects and corrects
            else:
                if not req.corrected_label:
                    raise HTTPException(
                        status_code=400,
                        detail="Corrected label required when confirmation is false"
                    )
                unit["label"] = req.corrected_label
                unit["confidence"] = 1.0  # reset confidence after correction

            save_knowledge_unit(unit)
            return ConfirmationResponse(status="updated")

    # If knowledge unit not found
    raise HTTPException(
        status_code=404,
        detail="Knowledge unit not found"
    )
