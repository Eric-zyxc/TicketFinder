import os
from dotenv import load_dotenv
from dataclasses import dataclass
from functools import lru_cache

load_dotenv()


@dataclass(frozen=True)
class Settings:
    DATABASE_URL: str | None
    RAPIDAPI_KEY: str | None

@lru_cache(maxsize=1)
def get_settings() -> Settings:

    return Settings(
        DATABASE_URL = os.getenv("DATABASE_URL"),
        RAPIDAPI_KEY= os.getenv("RAPIDAPI_KEY"),
    )
    
settings = get_settings()