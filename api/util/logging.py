import logging
import sys

from api.util.settings import app_settings

logger = logging.getLogger()


def init_logging():
    logger.setLevel(app_settings.logging_level)
    stream_handler = logging.StreamHandler(sys.stdout)
    log_formatter = logging.Formatter("[%(levelname)s]: %(message)s")
    stream_handler.setFormatter(log_formatter)
    logger.addHandler(stream_handler)
