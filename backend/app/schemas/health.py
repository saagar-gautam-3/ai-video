"""Health check schemas"""
from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class HealthStatus(BaseModel):
    """Health status response"""
    status: str
    timestamp: datetime


class DatabaseHealth(BaseModel):
    """Database health status"""
    status: str
    error: Optional[str] = None
    timestamp: datetime


class RedisHealth(BaseModel):
    """Redis health status"""
    status: str
    error: Optional[str] = None
    timestamp: datetime


class ApplicationHealth(BaseModel):
    """Overall application health status"""
    status: str
    timestamp: datetime
    database: DatabaseHealth
    redis: RedisHealth
