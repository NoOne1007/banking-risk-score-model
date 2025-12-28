import logging
import sys

def get_logger(name: str, level: str = "INFO") -> logging.Logger:
    """
    Create or return a configured logger.
    """

    logger = logging.getLogger(name)

    # Prevent duplicate handlers (VERY IMPORTANT)
    if logger.handlers:
        return logger

    logger.setLevel(level)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    logger.propagate = False

    return logger
