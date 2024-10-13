# server/app/api/v1/endpoints/tiktok.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from app.services import tiktok_service

router = APIRouter()

class TikTokDownloadRequest(BaseModel):
    url: str
    format: Optional[str] = "mp4"  # or other supported formats

class TikTokDownloadResponse(BaseModel):
    download_url: str
    message: str

@router.post("/download", response_model=TikTokDownloadResponse)
async def download_tiktok_content(request: TikTokDownloadRequest):
    try:
        download_url = tiktok_service.download_content(request.url, request.format)
        return TikTokDownloadResponse(
            download_url=download_url,
            message="Download successful."
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
