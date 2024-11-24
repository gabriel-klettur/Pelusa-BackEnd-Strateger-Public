# Path: app/config.py
import os
from dotenv import load_dotenv
from loguru import logger

load_dotenv()

class Settings:
    DATABASE_URL_DESARROLLO_ALARMAS = os.getenv("DATABASE_URL_DESARROLLO_ALARMAS").replace("pymysql", "aiomysql")
    DATABASE_URL_DESARROLLO_ESTRATEGIAS = os.getenv("DATABASE_URL_DESARROLLO_ESTRATEGIAS").replace("pymysql", "aiomysql")
    DATABASE_URL_DESARROLLO_DIARY = os.getenv("DATABASE_URL_DESARROLLO_DIARY").replace("pymysql", "aiomysql")    
    DATABASE_URL_DESARROLLO_POSITIONS = os.getenv("DATABASE_URL_DESARROLLO_POSITIONS").replace("pymysql", "aiomysql")    
    DATABASE_URL_DESARROLLO_ACCOUNTS = os.getenv("DATABASE_URL_DESARROLLO_ACCOUNTS").replace("pymysql", "aiomysql")    
    DATABASE_URL_DESARROLLO_KLINE_DATA = os.getenv("DATABASE_URL_DESARROLLO_KLINE_DATA").replace("pymysql", "aiomysql")
    DATABASE_URL_DESARROLLO_ORDERS = os.getenv("DATABASE_URL_DESARROLLO_ORDERS").replace("pymysql", "aiomysql")
    APIURL = os.getenv("APIURL")
    APIKEY = os.getenv("APIKEY")
    SECRETKEY = os.getenv("SECRETKEY")
    ALLOWED_IPS = os.getenv("ALLOWED_IPS", "").split(",")
    BLOCKED_IPS = os.getenv("BLOCKED_IPS", "").split(",")
    UPLOAD_DIRECTORY = "./app/strateger/uploads/diary"


settings = Settings()


