from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base

from config.config import config

DATABASE_URL = config.database.asyncpg_url

async_engine = create_async_engine(DATABASE_URL)
async_session = async_sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)

Base = declarative_base()