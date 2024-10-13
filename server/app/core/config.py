# server/app/core/config.py

import os
from pydantic import BaseSettings, AnyHttpUrl, validator
from typing import List, Optional
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Settings(BaseSettings):
    PROJECT_NAME: str = "Instagram & TikTok Downloader"
    PROJECT_DESCRIPTION: str = "API to download images and videos from Instagram Reels, Posts, TikTok Videos, Snapchat Stories, and X.com."
    PROJECT_VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"

    # CORS Settings
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = [
        "http://localhost:3000",  # React frontend
    ]

    # Add other settings like API keys if necessary
    # INSTAGRAM_API_KEY: Optional[str] = None
    # TIKTOK_API_KEY: Optional[str] = None
    # etc.

    class Config:
        case_sensitive = True

settings = Settings()
