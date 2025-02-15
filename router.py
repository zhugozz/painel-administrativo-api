from fastapi import APIRouter
from business.router import router as business_router


api_router = APIRouter()

api_router.include_router(business_router,
                   prefix="/business")


@api_router.get("/health_check")
async def get_health_check():
    return "Server is running"