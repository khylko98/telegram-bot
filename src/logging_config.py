import logging


def setup_logger():
    logging.basicConfig(
        format="%(asctime)s — %(levelname)s — %(message)s", 
        level=logging.INFO
    )
    logger = logging.getLogger(__name__)
    return logger
