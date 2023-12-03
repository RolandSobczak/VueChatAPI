from __future__ import annotations

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from backend.settings import Settings

settings = Settings()


SQLALCHEMY_DATABASE_URL = (
    f"postgresql+psycopg2://{settings.POSTGRES_CONFIG['USER']}:{settings.POSTGRES_CONFIG['PASSWORD']}"
    f"@/{settings.POSTGRES_CONFIG['DB']}?host={settings.POSTGRES_CONFIG['HOST']}&port={settings.POSTGRES_CONFIG['PORT']}"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base = declarative_base()


class SessionManager:
    """Manage opened sessions.
    If session is already opened returns current session if not returns the newone.
    """

    _attributes: dict = {}
    _session = None
    _session_factory = SessionLocal

    def __init__(self):
        self.__dict__ = self._attributes

    def __del__(self):
        if self._session is not None:
            self._session.close()

    def open_new_session(self):
        self._session = self._session_factory()

    @property
    def session(self):
        if self._session is None:
            self.open_new_session()

        return self._session
