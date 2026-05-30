"""API router initialization"""
from fastapi import APIRouter

from app.api import health

api_router = APIRouter(prefix="/api/v1")

# Include routers
api_router.include_router(health.router)
