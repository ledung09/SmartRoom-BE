from fastapi import APIRouter, Query
from service.product import productService

ProductService = productService()
router = APIRouter()

@router.get("/{id}")
async def getProductById(id: str):
    userId = 1
    response = await ProductService.getProductFullDetail(id, userId)
    return response

@router.patch("/hearted/{id}")
def getProductById(id: str):
    userId = 1
    return ProductService.setProductHeartedDetail(id, userId)