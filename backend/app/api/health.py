"""Health check routes"""
import logging

from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.health import check_application_health
from app.db.session import get_db
from app.schemas.health import ApplicationHealth

logger = logging.getLogger(__name__)
router = APIRouter(tags=["Health"])


@router.get(
    "/health",
    response_model=ApplicationHealth,
    status_code=status.HTTP_200_OK,
)
async def health_check(session: AsyncSession = Depends(get_db)) -> ApplicationHealth:
    """
    Health check endpoint.
    
    Returns the status of the application, database, and Redis.
    """
    health_status = await check_application_health(session)
    return ApplicationHealth(**health_status)
