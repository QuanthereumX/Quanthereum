# logger.py - Logging system for QuanthereumX
# Author: Przemek Buczek

import logging
import os

# Define log file path
LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "quanthereumx.log")

# Ensure log directory exists
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def get_logger(name="QuanthereumX"):
    """Returns a configured logger instance."""
    return logging.getLogger(name)

# Example usage
if __name__ == "__main__":
    logger = get_logger()
    logger.info("Logger initialized successfully!")
