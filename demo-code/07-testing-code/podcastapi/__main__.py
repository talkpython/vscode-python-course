"""
Command-line entrypoint for podcastapi package
"""
from argparse import ArgumentParser

import uvicorn

from podcastapi.api import api
from podcastapi.custom_logging import logger
from podcastapi.data import import_sample_data


def get_parser() -> ArgumentParser:
    """Returns the confiured ArgumentParser for this module"""
    parser = ArgumentParser()
    parser.add_argument(
        "-g", "--generate", dest="generate", action="store_true", required=False
    )

    return parser


def main():
    """Entry point function. Loads FastAPI instance in uvicorn and instantiates tinydb"""
    args = get_parser().parse_args()

    if args.generate:
        logger.debug('Generating sample data.')
        import_sample_data()

    logger.debug('Starting uvicorn server..')
    uvicorn.run(api)


if __name__ == "__main__":
    main()
