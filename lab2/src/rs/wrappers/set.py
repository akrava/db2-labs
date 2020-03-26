from rs.connection import RedisClient


class Set:
    def __init__(self, name: str):
        self.__redis = RedisClient().get_connection()
        self.__set_name = name

    def add(self, value: str):
        return self.__redis.sadd(self.__set_name, value)

    def contains(self, value: str):
        return self.__redis.sismember(self.__set_name, value)

    def get_all(self):
        # use SSCAN to iterate when sets are to huge
        return [x.decode("utf-8") for x in self.__redis.smembers(self.__set_name)]

    def remove(self, value: str):
        return self.__redis.srem(self.__set_name, value)
