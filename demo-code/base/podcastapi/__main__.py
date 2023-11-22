"""
Command-line entrypoint for podcastapi package
"""
from argparse import ArgumentParser

import uvicorn

from podcastapi.api import api
from podcastapi.data import import_sample_data


def get_parser() -> ArgumentParser:
    """Returns the confiured ArgumentParser for this module"""
    parser = ArgumentParser()
    parser.add_argument(
        "-g", "--generate", dest="generate", action="store_true", required=False
    )

    return parser


def main():
    '''Entry point function. Loads FastAPI instance in uvicorn and instantiates tinydb'''
    args = get_parser().parse_args()

    if args.generate:
        import_sample_data()

    uvicorn.run(api)


if __name__ == "__main__":
    main()
