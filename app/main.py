from fastapi import FastAPI
from app.api.routes.chats import router as chats_router
from app.core.logging import setup_logging

setup_logging()

app = FastAPI(title="Chats API")

app.include_router(chats_router)


@app.get("/health")
def health():
    return {"status": "ok"}
