import sys
import os

# import variable path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), './')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from fastapi import FastAPI
from src.controller.es import router as esRouter
from src.controller.category import router as categoryRouter
from src.controller.product import router as productRouter
from src.controller.prompt_paint import router as promptPaintRouter
from src.controller.example_paint import router as examplePaintRouter

app = FastAPI(title="SmartRoom - 5guys API")

@app.get("/", tags=["Hi 👋"])
def greetFrom5guys():
    return {"greeting":"Hello from 5guys!"}

# <-- List of routers here -->
# ES router
app.include_router(router=esRouter, prefix="/search", tags=["Search"])

# Category router
app.include_router(router=categoryRouter, prefix="/category", tags=["Category"])

# Category router
app.include_router(router=productRouter, prefix="/product", tags=["Product"])

# Prompt Paint router
app.include_router(router=promptPaintRouter, prefix="/prompt_paint", tags=["Prompt Paint"])

# Example Paint router
app.include_router(router=examplePaintRouter, prefix="/example_paint", tags=["Example Paint"])