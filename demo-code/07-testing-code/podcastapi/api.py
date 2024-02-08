"""
This module exports 'api'; the main FastAPI instance for the podcastapi package configured
with its various endpoint routers
"""
import uvicorn
from fastapi import FastAPI

from podcastapi.routers.categories_router import categories_router
from podcastapi.routers.shows_router import shows_router
from podcastapi.routers.status_router import status_router

api = FastAPI()

api.include_router(status_router)
api.include_router(shows_router)
api.include_router(categories_router)

if __name__ == '__main__':
    uvicorn.run(api)
