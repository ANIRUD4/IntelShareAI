# backend/main.py
from fastapi import FastAPI
from backend.routes import learn, infer, confirm, export_import

app = FastAPI(title="IntelShare")

app.include_router(learn.router)
app.include_router(infer.router)
app.include_router(confirm.router)
app.include_router(export_import.router)

@app.get("/")
def health():
    return {"status": "IntelShare running"}
