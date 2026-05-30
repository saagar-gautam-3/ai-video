"""Health check endpoint"""
import logging
from datetime import datetime

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.redis import redis_health_check

logger = logging.getLogger(__name__)


async def check_database(session: AsyncSession) -> dict:
    """Check database connectivity"""
    try:
        await session.execute(text("SELECT 1"))
        return {
            "status": "healthy",
            "timestamp": datetime.utcnow().isoformat(),
        }
    except Exception as e:
        logger.error(f"Database health check failed: {str(e)}")
        return {
            "status": "unhealthy",
            "error": str(e),
            "timestamp": datetime.utcnow().isoformat(),
        }


async def check_redis() -> dict:
    """Check Redis connectivity"""
    try:
        is_healthy = await redis_health_check()
        if is_healthy:
            return {
                "status": "healthy",
                "timestamp": datetime.utcnow().isoformat(),
            }
        else:
            return {
                "status": "unhealthy",
                "error": "Redis ping failed",
                "timestamp": datetime.utcnow().isoformat(),
            }
    except Exception as e:
        logger.error(f"Redis health check error: {str(e)}")
        return {
            "status": "unhealthy",
            "error": str(e),
            "timestamp": datetime.utcnow().isoformat(),
        }


async def check_application_health(session: AsyncSession) -> dict:
    """Check overall application health"""
    db_health = await check_database(session)
    redis_health = await check_redis()
    
    overall_status = (
        "ok"
        if db_health["status"] == "healthy" and redis_health["status"] == "healthy"
        else "degraded"
    )
    
    return {
        "status": overall_status,
        "timestamp": datetime.utcnow().isoformat(),
        "database": db_health,
        "redis": redis_health,
    }
