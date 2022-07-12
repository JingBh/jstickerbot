import logging

from . import config

logging_level = logging.DEBUG if config.is_debug else logging.INFO

logging.basicConfig(
    format='[%(levelname)s] (%(module)s) %(message)s',
    level=logging_level
)
