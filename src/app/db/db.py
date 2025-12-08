from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
import os

DATABASE_USER = os.environ.get('DATABASE_USER')
DATABASE_PASS = os.environ.get('DATABASE_PASS')
DATABASE_HOST = os.environ.get('DATABASE_HOST')
DATABASE_PORT = os.environ.get('DATABASE_PORT')
DATABASE_NAME = os.environ.get('DATABASE_NAME')


engine = create_async_engine(
    url = f"mysql+aiomysql://{DATABASE_USER}:{DATABASE_PASS}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
)

async_session = async_sessionmaker(engine, expire_on_commit=False)
