import redis
from settings import REDIS_HOST, REDIS_PORT, REDIS_DB, REDIS_PASSWORD


class SingletonMeta(type):
    _instance = None

    def __call__(cls):
        if cls._instance is None:
            cls._instance = super().__call__()
        return cls._instance


class RedisClient(metaclass=SingletonMeta):
    def __init__(self):
        self.__conn = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB, password=REDIS_PASSWORD)

    def get_connection(self):
        return self.__conn
