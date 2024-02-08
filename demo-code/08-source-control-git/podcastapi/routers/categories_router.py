"""
Configures and exports an instance of APIRouter for the /categories path
"""
from fastapi import status
from fastapi.responses import JSONResponse, Response
from fastapi.routing import APIRouter
from tinydb import Query

from podcastapi.custom_logging import logger
from podcastapi.data import podcast_table

categories_router = APIRouter(prefix="/categories", tags=["categories"])


@categories_router.get("")
def get_distinct_categories() -> Response:
    """Returns a distinct listing of all stories categories"""
    logger.info('Retrieving categories.')
    if len(podcast_table) < 1:
        logger.info('No categories found')
        return Response(status_code=status.HTTP_404_NOT_FOUND)

    retrieve_categories = [show['categories'] for show in podcast_table.all()]
    distinct_categories = [item for sub in retrieve_categories for item in sub]
    return JSONResponse(distinct_categories)


@categories_router.get("/{category}/shows")
def get_shows_for_category(category: str) -> Response:
    """Returns shows that match a given category"""
    logger.info('Retrieving show for category: %s', category)
    if len(podcast_table) < 1:
        return Response(status_code=status.HTTP_404_NOT_FOUND)

    def case_insensitive_match(cat):
        'Local filter function'
        return category.upper() in map(str.upper, cat)

    casts = Query()
    qry = casts.categories.test(case_insensitive_match)
    qry_results = podcast_table.search(qry)
    if len(qry_results) < 1:
        logger.info('No shows matching category (%s) found', category)
        return Response(status_code=status.HTTP_404_NOT_FOUND)

    titles = [doc["name"] for doc in qry_results]
    return JSONResponse(titles)
