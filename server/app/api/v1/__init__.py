# Example: server/app/api/v1/__init__.py

from fastapi import APIRouter
from app.api.v1.endpoints import instagram, tiktok, snapchat, xcom

api_router = APIRouter()
api_router.include_router(instagram.router, prefix="/instagram", tags=["Instagram"])
api_router.include_router(tiktok.router, prefix="/tiktok", tags=["TikTok"])
api_router.include_router(snapchat.router, prefix="/snapchat", tags=["Snapchat"])
api_router.include_router(xcom.router, prefix="/xcom", tags=["X.com"])
