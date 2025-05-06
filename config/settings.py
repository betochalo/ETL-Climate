"""Configuration settings for the project."""
from functools import lru_cache
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """Settings for the project."""
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    FERNET_KEY: str

    AIRFLOW_UID: int

    AIRFLOW__API_AUTH__JWT_SECRET: str

    OPEN_WEATHER_MAP_API_KEY: str

    class Config:
        """Configuration for the settings."""
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True

@lru_cache
def get_settings():
    """Get settings."""
    return Settings()

settings = get_settings()
