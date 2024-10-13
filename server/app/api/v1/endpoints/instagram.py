# server/app/api/v1/endpoints/instagram.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from app.services import instagram_service

router = APIRouter()

class InstagramDownloadRequest(BaseModel):
    url: str
    format: Optional[str] = "mp4"  # or "jpg" depending on content type

class InstagramDownloadResponse(BaseModel):
    download_url: str
    message: str

@router.post("/download", response_model=InstagramDownloadResponse)
async def download_instagram_content(request: InstagramDownloadRequest):
    try:
        download_url = instagram_service.download_content(request.url, request.format)
        return InstagramDownloadResponse(
            download_url=download_url,
            message="Download successful."
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
