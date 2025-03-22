from fastapi import FastAPI
from app.config import get_settings

from app.router import auth
from app.router import geo
from app.database import Base, engine

settings = get_settings()
app = FastAPI(title=settings.app.name)
Base.metadata.create_all(bind=engine)

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(geo.router, prefix="/geo", tags=["Geo"])


@app.get("/")
async def root():
    return {"message": f"Welcome to {settings.app.name} backend!"}
