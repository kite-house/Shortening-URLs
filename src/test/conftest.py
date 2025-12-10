from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from typing import AsyncGenerator
from httpx import AsyncClient, ASGITransport
import pytest_asyncio

from src.app.main import app
from src.app.db.db import settings
from src.app.db.models import Base

engine = create_async_engine(url = settings.DB_URL)

async_session = async_sessionmaker(engine, autoflush=True, expire_on_commit=False)

@pytest_asyncio.fixture(scope = 'session', autouse = True)
async def setup_db():
    async with engine.begin() as conn:
        assert settings.MODE == 'TEST'
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

        yield

        await conn.run_sync(Base.metadata.drop_all)
        

@pytest_asyncio.fixture(scope="function")
async def session():
    async with async_session() as session:
        try:
            yield session
        finally:
            session.close()

@pytest_asyncio.fixture(scope = 'session')
async def ac() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(transport = ASGITransport(app=app), base_url = "http://test") as ac: 
        yield ac