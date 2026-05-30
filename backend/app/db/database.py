"""Database lifecycle and health validation utilities"""
import logging
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import engine

logger = logging.getLogger(__name__)


async def init_db() -> None:
    """Validate database connection on startup"""
    try:
        async with engine.connect() as conn:
            await conn.execute(text("SELECT 1"))
        logger.info("Database connection verified successfully.")
    except Exception as e:
        logger.critical(f"Database initialization failed: {str(e)}")
        raise


async def close_db() -> None:
    """Clean up and dispose of database engine pools on shutdown"""
    try:
        await engine.dispose()
        logger.info("Database connection pool disposed successfully.")
    except Exception as e:
        logger.error(f"Error disposing database connections: {str(e)}")


async def check_db_health(session: AsyncSession) -> bool:
    """Verify postgresql database connectivity"""
    try:
        await session.execute(text("SELECT 1"))
        return True
    except Exception as e:
        logger.error(f"Database health check query failed: {str(e)}")
        return False
