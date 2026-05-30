"""Main entry point for the FastAPI application"""
import uvicorn

from app.core.config import settings
from app.main import app

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=settings.RELOAD,
        log_level=settings.LOG_LEVEL.lower(),
    )
