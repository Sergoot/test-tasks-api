from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker


from app.core import settings


async_engine = create_async_engine(
    settings.SQLALCHEMY_DATABES_URL, pool_pre_ping=True
)

async_session = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=async_engine,
    class_=AsyncSession
)