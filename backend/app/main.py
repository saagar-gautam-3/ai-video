"""FastAPI application factory"""
import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import api_router
from app.core.config import settings, setup_logging
from app.core.exceptions import ApplicationException, application_exception_handler, general_exception_handler
from app.db.redis import init_redis, close_redis
from app.db.session import init_db, close_db

# Setup logging
setup_logging()
logger = logging.getLogger(__name__)


def create_app() -> FastAPI:
    """Create and configure FastAPI application"""
    
    app = FastAPI(
        title=settings.APP_NAME,
        debug=settings.DEBUG,
        version="0.1.0",
    )
    
    # CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Customize for production
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # Exception handlers
    app.add_exception_handler(ApplicationException, application_exception_handler)
    app.add_exception_handler(Exception, general_exception_handler)
    
    # Include API routes
    app.include_router(api_router)
    
    # Startup event
    @app.on_event("startup")
    async def startup_event() -> None:
        """Initialize connections on startup"""
        logger.info(f"Starting {settings.APP_NAME} - Environment: {settings.APP_ENV}")
        await init_db()
        await init_redis()
    
    # Shutdown event
    @app.on_event("shutdown")
    async def shutdown_event() -> None:
        """Close connections on shutdown"""
        logger.info(f"Shutting down {settings.APP_NAME}")
        await close_redis()
        await close_db()
    
    return app


# Create application instance
app = create_app()
