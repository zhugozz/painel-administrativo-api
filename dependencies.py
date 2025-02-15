from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession

# Project Directory
from database import Session

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    """
    Dependency function to provide an asynchronous database session.
    
    :return: An instance of AsyncSession
    """
    session: AsyncSession = Session()
    
    try:
        yield session
    finally:
        await session.close()