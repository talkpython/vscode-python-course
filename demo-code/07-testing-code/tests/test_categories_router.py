"""
Unit tests for the routes exposed by shows router
"""

import json

from fastapi import status
from pytest_mock import MockerFixture
from podcastapi.routers.categories_router import (
    get_distinct_categories,
    get_shows_for_category,
)


def test_get_distinct_categories_for_response(mocker: MockerFixture):
    """Test the response properties of get_distinct_categories"""

    mock_table = mocker.patch(
        "podcastapi.routers.categories_router.podcast_table", autospec=True
    )
    mock_table.__len__.return_value = 5
    mock_table.all.return_value = [
        {"categories": ["Technology"]},
        {"categories": ["Sports", "Health"]},
        {"categories": ["Technology"]},
        {"categories": ["Sports", "Health"]},
    ]

    response = get_distinct_categories()
    payload = json.loads(response.body.decode("utf-8"))

    assert response.status_code == status.HTTP_200_OK
    assert len(payload) == 3
    assert "Technology" in payload
    assert "Sports" in payload
    assert "Health" in payload


def test_get_distinct_categories_returns_404_for_empty_table(mocker: MockerFixture):
    """Test the response get_distinct_categories returns 404 if no data found"""

    mock_table = mocker.patch(
        "podcastapi.routers.categories_router.podcast_table", autospec=True
    )
    mock_table.__len__.return_value = 0
    response = get_distinct_categories()
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_get_shows_for_category_response_successful(mocker: MockerFixture):
    """get_shows_for_category returns successful response when data found"""

    mock_table = mocker.patch(
        "podcastapi.routers.categories_router.podcast_table", autospec=True
    )
    mock_table.__len__.return_value = 3
    mock_table.search.return_value = [
        {"name": "Sports Zone", "categories": ["Sports", "Health"]},
        {"name": "True Crime Stories", "categories": ["Crime", "Mystery"]},
        {"name": "Comedy Hour", "categories": ["Comedy"]},
    ]

    response = get_shows_for_category("")
    assert response.status_code == status.HTTP_200_OK
    mock_table.search.assert_called_once()


def test_get_shows_for_category_response_fails(mocker: MockerFixture):
    """get_shows_for_category returns error response when data missing"""

    mock_table = mocker.patch(
        "podcastapi.routers.categories_router.podcast_table", autospec=True
    )
    mock_table.__len__.return_value = 3
    mock_table.search.return_value = []

    response = get_shows_for_category("")

    mock_table.search.assert_called_once()
    assert response.status_code == status.HTTP_404_NOT_FOUND
