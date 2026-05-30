"""FastAPI application factory and lifecycle entrypoint"""
from contextlib import asynccontextmanager
import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.router import api_router
from app.core.config import settings
from app.core.logging import setup_logging
from app.db.database import init_db, close_db
from app.db.redis import init_redis, close_redis
from app.exceptions.handlers import register_exception_handlers
from app.middleware.logging_middleware import RequestLoggingMiddleware

# Configure logging at startup
setup_logging()
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifecycle context manager to manage application startup and shutdown events"""
    logger.info("Starting up FastAPI application...")
    try:
        # Initialize DB and verify connection
        await init_db()
        # Initialize Redis connection pool
        await init_redis()
        logger.info("All services initialized successfully.")
    except Exception as e:
        logger.critical(f"Service initialization failed during startup: {str(e)}", exc_info=True)
        raise e
        
    yield
    
    logger.info("Shutting down FastAPI application...")
    # Clean up connections
    await close_redis()
    await close_db()
    logger.info("All connections closed. Shutdown complete.")


def create_app() -> FastAPI:
    """FastAPI application factory"""
    app = FastAPI(
        title=settings.APP_NAME,
        debug=settings.DEBUG,
        version=settings.APP_VERSION,
        lifespan=lifespan,
    )

    # CORS Middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Restrict origins in production config
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Request Performance and Audit Logging Middleware
    app.add_middleware(RequestLoggingMiddleware)

    # Register Exception Handlers (centralized validation, database, and internal errors)
    register_exception_handlers(app)

    # Mount versioned API routes
    app.include_router(api_router, prefix=settings.API_V1_PREFIX)

    @app.get("/", tags=["Root"])
    async def root_redirect():
        """Root endpoint returning basic application meta"""
        return {
            "app": settings.APP_NAME,
            "version": settings.APP_VERSION,
            "status": "online",
            "docs_url": "/docs"
        }

    return app


# Create the application instance
app = create_app()
