import os
from dotenv import load_dotenv
from dataclasses import dataclass
from functools import lru_cache

load_dotenv()


@dataclass(frozen=True)
class Settings:
    ACCESS_TOKEN_EXPIRE_MINUTES: int | None
    SECRET_KEY: str | None
    DATABASE_URL: str | None
    AUTH_ALGORITHM: str | None


@lru_cache(maxsize=1)
def get_settings() -> Settings:

    return Settings(
        DATABASE_URL=os.getenv("DATABASE_URL"),
        SECRET_KEY=os.getenv("SECRET_KEY"),
        ACCESS_TOKEN_EXPIRE_MINUTES=int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")),
        AUTH_ALGORITHM=int(os.getenv("AUTH_ALGORITHM")),
    )


settings = get_settings()
