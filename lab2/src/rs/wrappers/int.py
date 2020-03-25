from rs.connection import RedisClient


class Int:
    def __init__(self, name: str):
        self.__redis = RedisClient().get_connection()
        self.__int_name = name

    def set(self, value: int):
        return self.__redis.set(self.__int_name, value)

    def get(self):
        return self.__redis.get(self.__int_name)

    def increment(self):
        return self.__redis.incr(self.__int_name)

    def exists(self):
        return self.get() is not None
