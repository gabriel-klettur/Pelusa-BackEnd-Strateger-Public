#Path: run.py

import uvicorn
import signal
import sys
from app.config import settings

from loguru import logger
from colorama import Fore

def signal_handler(sig, frame):
    logger.info('Shutting down gracefully...')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

if __name__ == "__main__":

    try:
        if settings.MODE_DEVELOPING:     
            print(Fore.RED +"----------------------------------------------MODE: DEVELOPING----------------------------------------------")
            uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)       
        else:      
            print(Fore.RED +"----------------------------------------------MODE: PRODUCTION----------------------------------------------")
            uvicorn.run(
                "app.main:app",
                host="0.0.0.0",
                port=8000,
                reload=True,
                ssl_keyfile="certs/key.pem",
                ssl_certfile="certs/cert.pem",                
                http="h11"  # Protocolo compatible con HTTP/2
                
            )
    except KeyboardInterrupt:
        logger.info("Server stopped by user (Ctrl+C)")
    except ConnectionResetError as e:
        logger.warning(f"Connection was reset: {e}")
        
