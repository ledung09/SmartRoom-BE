from fastapi import APIRouter, Query
from service.es import esService

EsService = esService()
router = APIRouter()

@router.get("")
def getProduct(query: str = Query(..., max_length=255)):
    response = EsService.getSearchResult(query)
    return response

@router.get("/autocomplete")
def getAutoCompleteProduct(query: str = Query(..., max_length=255)):
    response = EsService.getAutoCompleteSearchResult(query)
    return response