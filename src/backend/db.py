from __future__ import annotations
import asyncio

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from backend.settings import Settings

settings = Settings()


SQLALCHEMY_DATABASE_URL = (
    f"postgresql+asyncpg://{settings.POSTGRES_CONFIG['USER']}:{settings.POSTGRES_CONFIG['PASSWORD']}"
    f"@/{settings.POSTGRES_CONFIG['DB']}?host={settings.POSTGRES_CONFIG['HOST']}&port={settings.POSTGRES_CONFIG['PORT']}"
)

engine = create_async_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

Base = declarative_base()


class SessionManager:
    """Manage opened sessions.
    If session is already opened returns current session if not returns the newone.
    """

    _attributes: dict = {}
    _session: AsyncSession = None
    _session_factory = SessionLocal

    def __init__(self):
        self.__dict__ = self._attributes

    # def __del__(self):
    #     if self._session is not None:
    #         asyncio.run(self._session.close())

    def open_new_session(self):
        self._session = self._session_factory()

    @property
    def session(self) -> AsyncSession:
        if self._session is None:
            self.open_new_session()

        return self._session
