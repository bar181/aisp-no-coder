from fastapi import FastAPI
from app.dynamic_router import router

app = FastAPI(title="AISP PoC – Sprint 1")

@app.get("/healthz")
def health():
    return {"status": "OK"}

app.include_router(router, tags=["dynamic"])