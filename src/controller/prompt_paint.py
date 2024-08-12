from fastapi import APIRouter
import numpy as np
from service.prompt_paint import promptPaintService
from pydantic import BaseModel

PromptPaint = promptPaintService()
router = APIRouter()

class PromptPaintRequest(BaseModel):
    prompt: str
    image: np.ndarray
    class Config:
        arbitrary_types_allowed = True

@router.post("/")
async def promptPaint(request: PromptPaintRequest):    
    response = {
        "image": PromptPaint.paint(request.image, request.prompt)
    }
    
    return response

