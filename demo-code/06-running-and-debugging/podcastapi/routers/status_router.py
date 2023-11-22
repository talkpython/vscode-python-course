"""
Configures and exports an instance of APIRouter for the /status path
"""
from fastapi import Response, status
from fastapi.routing import APIRouter

status_router = APIRouter(prefix="/status", tags=["status"])


@status_router.get("")
def get_status(response: Response):
    '''Returns API status'''
    response.status_code = status.HTTP_200_OK
    return response
