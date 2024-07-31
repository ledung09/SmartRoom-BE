import sys
import os

# import variable path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), './')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from fastapi import FastAPI
from src.controller.category import router as categoryRouter

app = FastAPI(title="SmartRoom - 5guys API")

@app.get("/", tags=["Hi 👋"])
def greetFrom5guys():
    return {"greeting":"Hello from 5guys!"}

# <-- List of routers here -->
# Category router
app.include_router(router=categoryRouter, prefix="/category", tags=["Category"],)