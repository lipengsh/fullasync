from fastapi import APIRouter
from api.api_v1.endpoints import rates

api_router = APIRouter()
api_router.include_router(rates.router, prefix="/rates", tags=["rates"])
