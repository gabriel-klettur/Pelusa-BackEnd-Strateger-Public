#Path: run.py

import uvicorn
import signal
import sys
from loguru import logger

def signal_handler(sig, frame):
    logger.info('Shutting down gracefully...')
    sys.exit(0)
    #raise KeyboardInterrupt

signal.signal(signal.SIGINT, signal_handler)

if __name__ == "__main__":
    try:
        uvicorn.run("app.main:app", host="0.0.0.0", port=80, reload=True, log_level="debug")
    except KeyboardInterrupt:
        logger.info('Server stopped by user (Ctrl+C)')