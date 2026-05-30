"""Redis connection pool management and health monitoring"""
import logging
from typing import Optional

import redis.asyncio as redis

from app.core.config import settings

logger = logging.getLogger(__name__)

# Connection pool instance
_redis_pool: Optional[redis.ConnectionPool] = None
redis_client: Optional[redis.Redis] = None


async def init_redis() -> None:
    """Initialize Redis connection pool and verify connectivity"""
    global _redis_pool, redis_client
    try:
        logger.info(f"Initializing Redis connection pool to {settings.REDIS_URL}")
        _redis_pool = redis.ConnectionPool.from_url(
            settings.REDIS_URL,
            decode_responses=True,
            max_connections=20,
        )
        redis_client = redis.Redis(connection_pool=_redis_pool)
        # Test the connection
        await redis_client.ping()
        logger.info("Redis connection established successfully.")
    except Exception as e:
        logger.critical(f"Redis initialization failed: {str(e)}")
        raise


async def close_redis() -> None:
    """Clean up and close Redis connection pool on shutdown"""
    global _redis_pool, redis_client
    if redis_client:
        await redis_client.close()
        redis_client = None
    if _redis_pool:
        await _redis_pool.disconnect()
        _redis_pool = None
    logger.info("Redis connection closed successfully.")


async def get_redis() -> redis.Redis:
    """Dependency injection helper to retrieve active Redis client"""
    if redis_client is None:
        logger.error("Attempted to access Redis before client initialization.")
        raise RuntimeError("Redis client is not initialized.")
    return redis_client


async def redis_health_check() -> bool:
    """Validate Redis server connectivity and response latency"""
    if redis_client is None:
        return False
    try:
        await redis_client.ping()
        return True
    except Exception as e:
        logger.error(f"Redis health check failed: {str(e)}")
        return False
