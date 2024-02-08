"""
Unit tests for the routes exposed by status router
"""

import json

import pytest
from fastapi.testclient import TestClient

from podcastapi.api import api
from podcastapi.routers.status_router import get_status

client = TestClient(api)


@pytest.mark.test_client
def test_status_route():
    """Test root route"""
    response = client.get("/status")
    assert response.status_code == 200


def test_status_response():
    """Test the response properties are correctly set"""
    response = get_status()
    assert response.status_code == 200
    assert "X-COURSE" in response.headers

    payload = json.loads(response.body.decode("utf-8"))
    assert "status" in payload
