import os

import logging
from logging.handlers import RotatingFileHandler

log_dir = "logs"

try:
    os.makedirs(log_dir, exist_ok=True)
except Exception as e:
    logging.basicConfig()
    logging.error(f"Failed to create log dir: {e}")

logger = logging.getLogger("backend")
logger.setLevel(logging.INFO)

formatter = logging.Formatter("{asctime} - {name} - {levelname} - {message}",
                              datefmt="%d-%m-%Y %H:%M:%S",
                              style="{")

try:
    file_handler = RotatingFileHandler(filename=os.path.join(log_dir, "app.log"),
                                       maxBytes=10 * 1024 * 1024,
                                       backupCount=10,
                                       encoding="utf-8")

    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)
    logger.addHandler(file_handler)
except Exception as e:
    logger.error(f"Failed to init file handler: {e}")

try:
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    stream_handler.setLevel(logging.INFO)
    logger.addHandler(stream_handler)
except Exception as e:
    logger.error(f"Failed to init stream handler: {e}")

def get_logger():
    return logger