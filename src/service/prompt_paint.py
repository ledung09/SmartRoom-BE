import numpy as np
import cv2

class promptPaintService:
    async def paint(
        image: np.ndarray, 
        prompt: str
    ):
        image = cv2.line(image, (image.shape[1], 0), (0, image.shape[0]), (255,0,0), 5)
        return image