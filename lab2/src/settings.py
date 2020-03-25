import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

REDIS_HOST = os.getenv("HOST")
REDIS_PORT = os.getenv("PORT")
REDIS_DB = os.getenv("DB")
REDIS_PASSWORD = os.getenv("PASSWORD")
