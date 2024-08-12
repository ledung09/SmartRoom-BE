from fastapi import APIRouter
import numpy as np
from service.example_paint import examplePaintService
from pydantic import BaseModel

ExamplePaint = examplePaintService() 
router = APIRouter()

class ExamplePaintRequest(BaseModel):
    background: np.ndarray
    mask: np.ndarray
    foreground: np.ndarray
    class Config:
        arbitrary_types_allowed = True

@router.post("/")
async def examplePaint(request: ExamplePaintRequest):    
    response = {
        "image": ExamplePaint.paint(request.background, request.mask, request.foreground)
    }
    
    return response
