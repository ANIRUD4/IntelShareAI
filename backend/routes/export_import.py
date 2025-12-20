from fastapi import APIRouter

from backend.schemas.export_import import (
    ExportResponse,
    ImportRequest,
    ImportResponse
)
from backend.export_import import export_knowledge, import_knowledge

router = APIRouter(prefix="/knowledge")

@router.post("/export", response_model=ExportResponse)
def export():
    return export_knowledge()

@router.post("/import", response_model=ImportResponse)
def import_data(req: ImportRequest):
    return import_knowledge(req.file_path)
