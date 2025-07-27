import os
import datetime
import logging

import colorlog

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

formatter = colorlog.ColoredFormatter(
    "%(log_color)s%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    log_colors={
        "DEBUG": "blue",
        "INFO": "green",
        "WARNING": "yellow",
        "ERROR": "red",
        "CRITICAL": "red,bg_white",
    },
)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

current_date = datetime.datetime.now().strftime("%d-%m-%Y")
log_directory = os.path.join(os.getcwd(), "logs")
log_file = os.path.join(log_directory, f"logs_{current_date}.log")

file_handler = logging.FileHandler(log_file)
file_handler.setFormatter(logging.Formatter("%(asctime)s | %(levelname)s | %(message)s"))

# Add the StreamHandler to the logger
logger.addHandler(stream_handler)
logger.addHandler(file_handler)
