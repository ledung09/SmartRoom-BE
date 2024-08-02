from fastapi import APIRouter, Query
from service.product import productService

ProductService = productService()
router = APIRouter()

@router.get("/{id}")
async def getProductById(id: str):
    response = await ProductService.getProductFullDetail(id)
    return response