"""Pytest configuration and shared fixtures"""
import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

from app.main import app
from app.core.config import settings
from app.db.session import get_db
from app.db.redis import init_redis, close_redis


# Build test DB URL (same as app settings)
TEST_DATABASE_URL = settings.DATABASE_URL
if TEST_DATABASE_URL.startswith("postgresql://"):
    TEST_DATABASE_URL = TEST_DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://", 1)


@pytest_asyncio.fixture(scope="session")
async def async_client():
    """Create an async HTTP test client with initialized services"""
    await init_redis()
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test"
    ) as client:
        yield client
    await close_redis()


@pytest_asyncio.fixture
async def db_session():
    """Create a standalone test database session"""
    engine = create_async_engine(TEST_DATABASE_URL, echo=False, future=True)
    session_maker = async_sessionmaker(
        bind=engine,
        class_=AsyncSession,
        expire_on_commit=False
    )
    async with session_maker() as session:
        yield session
    await engine.dispose()
