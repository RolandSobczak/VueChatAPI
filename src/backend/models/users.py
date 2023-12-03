from fastapi_users.db import SQLAlchemyBaseUserTableUUID

from backend.db import Base
from sqlalchemy.orm import Mapped, mapped_column


class User(SQLAlchemyBaseUserTableUUID, Base):
    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
