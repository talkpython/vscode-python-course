"""
Configures and exports an instance of APIRouter for the /status path
"""
from fastapi import status
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter

status_router = APIRouter(prefix="/status", tags=["status"])


@status_router.get("")
def get_status():
    """Returns API status"""
    payload = {"status": "healthy"}
    headers = {"X-COURSE": "VScode for Python"}
    response = JSONResponse(payload, status_code=status.HTTP_200_OK, headers=headers)
    return response
