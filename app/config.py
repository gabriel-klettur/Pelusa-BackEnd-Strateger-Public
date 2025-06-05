# Path: app/config.py
import os
from dotenv import load_dotenv
from loguru import logger

load_dotenv()

class Settings:
    # Base de datos (Neon)
    DATABASE_URL = os.getenv("DATABASE_URL")
    # Otros ajustes
    APIURL = os.getenv("APIURL")
    APIKEY = os.getenv("APIKEY")
    SECRETKEY = os.getenv("SECRETKEY")
    ALLOWED_IPS = os.getenv("ALLOWED_IPS", "").split(",")
    BLOCKED_IPS = os.getenv("BLOCKED_IPS", "").split(",")
    UPLOAD_DIRECTORY = "./app/strateger/uploads/diary"
    MODE_DEVELOPING = os.getenv("MODE_DEVELOPING", "false").strip().lower() in ["true", "1", "yes", "on"]

settings = Settings()
