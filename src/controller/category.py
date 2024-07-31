from fastapi import APIRouter
from service.category import categoryService

CategoryService = categoryService()
router = APIRouter()

@router.get("")
def getCategory():
    response = CategoryService.getCategoryList()
    return response