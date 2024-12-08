#Path: run.py

import uvicorn
import signal
import sys
from loguru import logger

def signal_handler(sig, frame):
    logger.info('Shutting down gracefully...')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

if __name__ == "__main__":
    try:
        uvicorn.run(
            "app.main:app",
            host="0.0.0.0",
            port=8000,
            reload=True,
            ssl_keyfile="C:\\certs\\key.pem",
            ssl_certfile="C:\\certs\\cert.pem",
            ssl_ca_certs="C:\\certs\\ca_bundle.pem",
        )
    except KeyboardInterrupt:
        logger.info("Server stopped by user (Ctrl+C)")
    except ConnectionResetError as e:
        logger.warning(f"Connection was reset: {e}")