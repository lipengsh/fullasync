from fastapi import APIRouter
from api.endpoints import rates

api_router = APIRouter()
api_router.include_router(rates.router, prefix="/rates", tags=["rates"])
