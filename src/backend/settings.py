from environs import Env
from pydantic_settings import BaseSettings

env: Env = Env()


class Settings(BaseSettings):
    SECRET_KEY: str = env("SECRET_KEY")

    POSTGRES_CONFIG: dict = {
        "USER": env("POSTGRES_USER"),
        "PASSWORD": env("POSTGRES_PASSWORD"),
        "HOST": env("POSTGRES_HOST"),
        "PORT": env("POSTGRES_PORT", default="5432"),
        "DB": env("POSTGRES_DB"),
    }
