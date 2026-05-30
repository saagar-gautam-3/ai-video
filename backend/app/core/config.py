from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

# Get the backend root directory
BASE_DIR = Path(__file__).resolve().parent.parent.parent


class Settings(BaseSettings):
    """Application settings loaded from environment variables"""

    # Application Configuration
    APP_NAME: str = "AI Reel Generator"
    APP_ENV: str = "development"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True
    LOG_LEVEL: str = "INFO"
    SECRET_KEY: str = "supersecretkey_change_me_in_production"

    # API Prefix
    API_V1_PREFIX: str = "/api/v1"

    # Database
    DATABASE_URL: str = "postgresql://ai_user:ai_password@localhost:5432/ai_reel_generator"

    # Redis
    REDIS_URL: str = "redis://localhost:6379/0"

    # Server Configuration
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    RELOAD: bool = True

    model_config = SettingsConfigDict(
        env_file=str(BASE_DIR / ".env"),
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )


settings = Settings()
