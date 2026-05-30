"""Tests for the health check endpoint and database/redis connectivity"""
import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_health_endpoint_returns_200(async_client: AsyncClient):
    """Health endpoint should respond with HTTP 200"""
    response = await async_client.get("/api/v1/health")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_health_response_structure(async_client: AsyncClient):
    """Health endpoint response should contain all required fields"""
    response = await async_client.get("/api/v1/health")
    data = response.json()

    assert "status" in data
    assert "version" in data
    assert "database" in data
    assert "redis" in data


@pytest.mark.asyncio
async def test_health_status_ok(async_client: AsyncClient):
    """Health endpoint should return 'ok' when all services are up"""
    response = await async_client.get("/api/v1/health")
    data = response.json()

    assert data["status"] == "ok"


@pytest.mark.asyncio
async def test_health_database_connected(async_client: AsyncClient):
    """Health endpoint should confirm the database is connected"""
    response = await async_client.get("/api/v1/health")
    data = response.json()

    assert data["database"] == "connected"


@pytest.mark.asyncio
async def test_health_redis_connected(async_client: AsyncClient):
    """Health endpoint should confirm Redis is connected"""
    response = await async_client.get("/api/v1/health")
    data = response.json()

    assert data["redis"] == "connected"


@pytest.mark.asyncio
async def test_health_version_format(async_client: AsyncClient):
    """Health endpoint version field should be a non-empty string"""
    response = await async_client.get("/api/v1/health")
    data = response.json()

    assert isinstance(data["version"], str)
    assert len(data["version"]) > 0


@pytest.mark.asyncio
async def test_database_connection_directly(db_session):
    """Direct database session should be able to execute a simple query"""
    from sqlalchemy import text
    result = await db_session.execute(text("SELECT 1"))
    row = result.scalar()
    assert row == 1


@pytest.mark.asyncio
async def test_root_endpoint(async_client: AsyncClient):
    """Root endpoint should return app metadata"""
    response = await async_client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "app" in data
    assert "version" in data
    assert "status" in data
