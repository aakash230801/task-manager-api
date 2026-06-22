from fastapi import FastAPI

from app.api.routers.user_router import router as user_router
from app.core.database import engine, Base

# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="job-tracker-api",
    version="1.0.0"
)

app.include_router(user_router, prefix="/api")

@app.get("/")
def health():
    return {
        "status": "Running"
    }