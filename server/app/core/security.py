# server/app/core/security.py

from fastapi.security import OAuth2PasswordBearer
from app.core.config import settings

# Placeholder for OAuth2 if authentication is needed in the future
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
