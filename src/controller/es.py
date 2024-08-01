from fastapi import APIRouter, Query
from service.es import esService

EsService = esService()
router = APIRouter()

@router.get("")
def getCategory(query: str = Query(..., max_length=255)):
    response = EsService.getSearchResult(query)
    return response