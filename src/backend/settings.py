from environs import Env
from pydantic_settings import BaseSettings

env: Env = Env()


class Settings(BaseSettings):
    POSTGRES_CONFIG: dict = {
        "USER": env("POSTGRES_USER"),
        "PASSWORD": env("POSTGRES_PASSWORD"),
        "HOST": env("POSTGRES_HOST"),
        "PORT": env("POSTGRES_PORT", default="5432"),
        "DB": env("POSTGRES_DB"),
    }
