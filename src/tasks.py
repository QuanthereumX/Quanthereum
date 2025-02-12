# tasks.py - Background tasks for QuanthereumX
# Author: Przemek Buczek

import time
import threading
from logger import get_logger

logger = get_logger()

def background_task():
    """Runs a background task every 10 seconds."""
    while True:
        logger.info("⏳ Running background task...")
        time.sleep(10)

def start_task():
    """Starts the background task in a separate thread."""
    thread = threading.Thread(target=background_task, daemon=True)
    thread.start()
    logger.info("🎯 Background task started!")

# Example usage
if __name__ == "__main__":
    logger.info("🚀 Starting background tasks...")
    start_task()
    
    # Keep the main thread running
    while True:
        time.sleep(1)
