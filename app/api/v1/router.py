from fastapi import APIRouter

from .endpoints import country

api_router = APIRouter()

api_router.include_router(country.router, prefix="/country", tags=["Country"])
