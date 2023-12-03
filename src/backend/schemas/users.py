import uuid

from pydantic import BaseModel
from fastapi_users import schemas


class UserRead(schemas.BaseUser[uuid.UUID]):
    id: int


class UserCreate(schemas.CreateUpdateDictModel):
    email: schemas.EmailStr
    password: str


class UserUpdate(schemas.BaseUserUpdate):
    pass