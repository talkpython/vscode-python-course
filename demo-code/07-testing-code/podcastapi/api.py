"""
This module exports 'api'; the main FastAPI instance for the podcastapi package configured
with it's various endppoint routers
"""
from fastapi import FastAPI
from podcastapi.routers.status_router import status_router
from podcastapi.routers.shows_router import shows_router
from podcastapi.routers.categories_router import categories_router

api = FastAPI()

api.include_router(status_router)
api.include_router(shows_router)
api.include_router(categories_router)
