from fastapi import APIRouter

from app.api.api_v1.endpoints import rate

api_router = APIRouter()
api_router.include_router(rate.router, prefix="/rates", tags=["rates"])
