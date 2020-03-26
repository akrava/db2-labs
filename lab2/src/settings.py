import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

REDIS_HOST = os.getenv("HOST")
REDIS_PORT = os.getenv("PORT")
REDIS_DB = os.getenv("DB")
REDIS_PASSWORD = os.getenv("PASSWORD")

MESSAGE_PROCESSING_DELAY_MS = int(os.getenv("MESSAGE_PROCESSING_DELAY_MS"))
MESSAGE_PROCESSING_DELAY_RANGE_MS = int(os.getenv("MESSAGE_PROCESSING_DELAY_RANGE_MS"))
SPAM_NICENESS = int(os.getenv("SPAM_NICENESS"))
