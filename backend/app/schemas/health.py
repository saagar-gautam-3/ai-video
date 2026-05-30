"""Health check schemas"""
from pydantic import BaseModel


class HealthResponse(BaseModel):
    """Health status response"""
    status: str
    version: str
    database: str
    redis: str
