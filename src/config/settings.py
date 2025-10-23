import os
from typing import List
from pydantic import BaseModel
from dotenv import load_dotenv

# Load .env file if it exists
load_dotenv()

class Settings(BaseModel):
    """Application settings"""
    # API settings
    API_HOST: str = os.getenv("API_HOST", "0.0.0.0")
    API_PORT: int = int(os.getenv("API_PORT", "8000"))
    API_DEBUG: bool = os.getenv("API_DEBUG", "false").lower() == "true"
    API_RELOAD: bool = os.getenv("API_RELOAD", "true").lower() == "true"
    API_WORKERS: int = int(os.getenv("API_WORKERS", "1"))

    # App info
    APP_NAME: str = "Generic API"
    APP_VERSION: str = "1.0.0"
    APP_DESCRIPTION: str = "A simple and generic API for basic operations"
    
    # Environment
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")

    # CORS
    ALLOWED_ORIGINS: List[str] = os.getenv("ALLOWED_ORIGINS", "*").split(",")

    # Logging
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "info")


# Create settings instance
settings = Settings()
