"""Redis connection management"""
import logging
from typing import Optional

import redis.asyncio as redis

from app.core.config import settings

logger = logging.getLogger(__name__)

redis_client: Optional[redis.Redis] = None


async def init_redis() -> None:
    """Initialize Redis connection"""
    global redis_client
    try:
        redis_client = await redis.from_url(settings.REDIS_URL, decode_responses=True)
        # Test connection
        await redis_client.ping()
        logger.info("Redis connection established")
    except Exception as e:
        logger.error(f"Failed to connect to Redis: {str(e)}")
        raise


async def close_redis() -> None:
    """Close Redis connection"""
    global redis_client
    if redis_client:
        await redis_client.close()
        logger.info("Redis connection closed")


async def get_redis() -> redis.Redis:
    """Get Redis client instance"""
    if redis_client is None:
        raise RuntimeError("Redis not initialized")
    return redis_client


async def redis_health_check() -> bool:
    """Check Redis health"""
    try:
        client = await get_redis()
        await client.ping()
        return True
    except Exception as e:
        logger.error(f"Redis health check failed: {str(e)}")
        return False
