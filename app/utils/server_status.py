# app/utils/server_status.py

import asyncio
from loguru import logger
from datetime import datetime

async def log_server_status():
    while True:
        try:            
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"[{current_time}] Server is running smoothly")
        except Exception as e:
            logger.error(f"Server status check failed: {e}")
        await asyncio.sleep(1) 
