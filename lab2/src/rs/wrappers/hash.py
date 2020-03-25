from rs.connection import RedisClient


class Hash:
    def __init__(self, name: str):
        self.__redis = RedisClient().get_connection()
        self.__hash_name = name

    def delete(self, key: str):
        return self.__redis.hdel(self.__hash_name, key)

    def get(self, key: str):
        return self.__redis.hget(self.__hash_name, key)

    def set(self, key: str, value: str):
        return self.__redis.hset(self.__hash_name, key, value)

    def set_all(self, payload: dict):
        return self.__redis.hmset(self.__hash_name, payload)
