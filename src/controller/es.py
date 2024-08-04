from fastapi import APIRouter, Query, HTTPException
from service.es import esService

EsService = esService()
router = APIRouter()

@router.get("")
def getProduct(
    offset: int,
    limit: int = 1,
    categoryId: int = None,
    priceSort: int = None,
    soldSort: int = None,
    query: str = None
):
    if categoryId is not None and categoryId <= 0:
        raise HTTPException(status_code=400, detail="Invalid categoryId")

    if priceSort not in [1, -1, None] or soldSort not in [1, -1, None]:
        raise HTTPException(status_code=400, detail="Invalid sort value")

    response = EsService.getSearchResult(
        query=query, 
        categoryId=categoryId, 
        priceSort=priceSort, 
        soldSort=soldSort,
        limit=limit,
        offset=offset,
        )
    return response

@router.get("/autocomplete")
def getAutoCompleteProduct(query: str = Query(..., max_length=255)):
    response = EsService.getAutoCompleteSearchResult(query)
    return response