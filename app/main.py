from fastapi import FastAPI
from .config import get_settings

settings = get_settings()
app = FastAPI(title=settings.app.name)


@app.get("/")
async def root():
    return {"message": f"Welcome to {settings.app_name} backend!"}
