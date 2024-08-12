import cv2
import numpy as np

class examplePaintService:
    async def paint(
        background: np.ndarray, 
        mask: np.ndarray, 
        foreground: np.ndarray
    ):
        image = cv2.line(background, (0,0), (background.shape[1], background.shape[0]), (255,0,0), 5)
        return image
        