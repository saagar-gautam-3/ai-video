"""V1 Health Check endpoint"""
import logging
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.db.session import get_db
from app.db.database import check_db_health
from app.db.redis import redis_health_check
from app.schemas.health import HealthResponse

logger = logging.getLogger(__name__)
router = APIRouter()


@router.get(
    "/health",
    response_model=HealthResponse,
    summary="Perform a system health check",
    description="Validates overall application status alongside PostgreSQL and Redis connections."
)
async def health_check(db: AsyncSession = Depends(get_db)) -> HealthResponse:
    # Check Database connection
    is_db_healthy = await check_db_health(db)
    db_status = "connected" if is_db_healthy else "disconnected"

    # Check Redis connection
    is_redis_healthy = await redis_health_check()
    redis_status = "connected" if is_redis_healthy else "disconnected"

    # Determine overall application status
    # If core services are offline, application status is degraded
    app_status = "ok"
    if not is_db_healthy or not is_redis_healthy:
        app_status = "degraded"

    return HealthResponse(
        status=app_status,
        version=settings.APP_VERSION,
        database=db_status,
        redis=redis_status
    )
