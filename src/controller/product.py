from fastapi import APIRouter, Query
from service.product import productService
from interface.product import HeartedProductUpdate

ProductService = productService()
router = APIRouter()

@router.get("/{id}")
async def getProductById(id: str):
    userId = 1
    response = await ProductService.getProductFullDetail(id, userId)
    return response



@router.patch("/hearted/{id}")
def getProductById(id: str, updateHearted: HeartedProductUpdate):
    userId = 1
    return ProductService.setProductHeartedDetail(id, userId, updateHearted)