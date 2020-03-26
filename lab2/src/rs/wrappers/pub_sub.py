from rs.connection import RedisClient


class PubSub:
    def __init__(self, name: str):
        self.__redis = RedisClient().get_connection()
        self.__ps = self.__redis.pubsub()
        self.__pub_sub_name = name

    def publish(self, msg: str):
        return self.__redis.publish(self.__pub_sub_name, msg)

    def subscribe(self):
        return self.__ps.subscribe(self.__pub_sub_name)

    def listen(self):
        return self.__ps.listen()

    def get_message(self):
        return self.__ps.get_message()
