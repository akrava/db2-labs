from rs.wrappers.list import List
from rs.wrappers.hash import Hash
from rs.settings import MESSAGE_QUEUE_LIST_NAME, MESSAGES_HASH_SET_PREFIX


class DefaultWorker:
    def __init__(self):
        self.__message_queue = List(MESSAGE_QUEUE_LIST_NAME)
        self.__bulk_size = 10

    def run(self):
        while True:
            # TODO use BLPOP command
            count = self.__message_queue.count()
            if self.__bulk_size < count:
                count = self.__bulk_size
            message_ids = []
            while count > 0:
                message_ids.append(self.__message_queue.remove())
                count -= 1
            for message_id in message_ids:
                # TODO move prefix to init
                message = Hash(MESSAGES_HASH_SET_PREFIX + message_id)
                if self.check_message(message.get('payload')):
                    pass
                else:
                    pass

    @staticmethod
    def check_message(payload: str):
        return len(payload) > 3
