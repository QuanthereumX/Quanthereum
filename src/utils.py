# utils.py - Utility functions for QuanthereumX
# Author: Przemek Buczek

import logging
import datetime

def get_current_timestamp():
    """Returns the current timestamp in ISO format."""
    return datetime.datetime.now().isoformat()

def log_message(level, message):
    """Logs a message with a specified logging level."""
    logging.log(level, f"[{get_current_timestamp()}] {message}")

def is_debug_mode():
    """Returns True if debug mode is enabled in config.py"""
    from config import DEBUG
    return DEBUG
