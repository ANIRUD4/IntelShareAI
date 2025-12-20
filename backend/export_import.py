import pickle
from pathlib import Path

from backend.storage_manager import load_all_units, save_knowledge_unit

EXPORT_DIR = Path("data/exports")
EXPORT_DIR.mkdir(parents=True, exist_ok=True)

def export_knowledge(file_name: str = "knowledge.pkl"):
    units = load_all_units()
    file_path = EXPORT_DIR / file_name

    with open(file_path, "wb") as f:
        pickle.dump(units, f)

    return {
        "status": "exported",
        "count": len(units),
        "file_path": str(file_path)
    }

def import_knowledge(file_path: str):
    with open(file_path, "rb") as f:
        units = pickle.load(f)

    for unit in units:
        save_knowledge_unit(unit)

    return {
        "status": "imported",
        "imported_count": len(units)
    }
