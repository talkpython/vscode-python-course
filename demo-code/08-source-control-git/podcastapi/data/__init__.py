"""
Exports configured instances of TinyDB, TinyDb.Table, and the import_sample_data function
"""
import json

from tinydb import TinyDB
from podcastapi.logging import logger


TABLE_NAME = "podcasts"
db = TinyDB("podcastdb.json")
podcast_table = db.table(TABLE_NAME)


def import_sample_data():
    """Loads podcast sample data from local sampledata.json file"""
    if len(podcast_table) < 1:
        with open("sampledata.json", encoding="utf-8") as sampledata:
            logger.info("Loading sample data")
            data = json.load(sampledata)

            podcast_table.insert_multiple(data)
    else:
        logger.info("Sample data already loaded.")
