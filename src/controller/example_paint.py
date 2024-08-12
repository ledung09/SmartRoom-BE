from fastAPI import APIRouter
import numpy as np
from service.example_paint import examplePaintService

ExamplePaint = examplePaintService() 
router = APIRouter()


@router.post("/")
async def examplePaint(background: np.ndarray, mask: np.ndarray, foreground: np.ndarray):    
    response = {
        "image": ExamplePaint.paint(background, mask, foreground)
    }
    
    return response
