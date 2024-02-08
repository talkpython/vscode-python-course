"""
Custom logging configuration
"""

import logging
from copy import copy

from uvicorn.logging import ColourizedFormatter


class _CustomFormatter(ColourizedFormatter):
    """
    Custom colorized log formatter 
    """

    def formatMessage(self, record: logging.LogRecord) -> str:
        recordcopy = copy(record)
        levelname = self.color_level_name(recordcopy.levelname, recordcopy.levelno)
        recordcopy.__dict__["levelclr"] = levelname
        return super().formatMessage(recordcopy)


logger = logging.getLogger("podcastapi")
logger.setLevel(logging.DEBUG)

_formatter = _CustomFormatter('%(levelclr)s: %(name)s %(module)s %(funcName)s %(message)s',
                              datefmt='%d-%b-%y %H:%M:%S %z', use_colors=True)

_ch = logging.StreamHandler()
_ch.setFormatter(_formatter)

logger.addHandler(_ch)
