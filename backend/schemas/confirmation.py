from pydantic import BaseModel

class ConfirmationRequest(BaseModel):
    knowledge_unit_id: str
    confirmed: bool
    corrected_label: str | None = None

class ConfirmationResponse(BaseModel):
    status: str
