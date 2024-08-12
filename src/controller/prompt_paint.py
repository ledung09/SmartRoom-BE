from fastAPI import APIRouter
import numpy as np
from service.prompt_paint import promptPaintService

PromptPaint = promptPaintService()
router = APIRouter()

@router.post("/")
async def promptPaint(prompt: str, image: np.ndarray):    
    response = {
        "image": PromptPaint.paint(image, prompt)
    }
    
    return response

