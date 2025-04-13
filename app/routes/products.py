import httpx
from fastapi import APIRouter


router = APIRouter(tags=["products"])

@router.get("/products")
async def get_products():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://dummyjson.com/products")
    return response.json()
