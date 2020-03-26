from rs.wrappers.int import Int
from rs.wrappers.set import Set
from rs.wrappers.hash import Hash
from rs.wrappers.list import List
from rs.settings import USER_INCOMING_MESSAGES_LIST_PREFIX, MESSAGE_NEXT_ID_NAME, MESSAGES_HASH_SET_PREFIX,\
    MESSAGE_IDS_CREATED_SET_NAME, MESSAGE_IDS_IN_QUEUE_SET_NAME, MESSAGE_QUEUE_LIST_NAME, USER_OUTCOMING_MESSAGES_SET_PREFIX


class Messages:
    def __init__(self):
        self.__next_id_message = Int(MESSAGE_NEXT_ID_NAME)
        if not self.__next_id_message.exists():
            self.__next_id_message.set(0)
        self.__message_prefix = MESSAGES_HASH_SET_PREFIX
        self.__incoming_message_prefix = USER_INCOMING_MESSAGES_LIST_PREFIX
        self.__outcoming__messages_prefix = USER_OUTCOMING_MESSAGES_SET_PREFIX
        self.__created_messages_set = Set(MESSAGE_IDS_CREATED_SET_NAME)
        self.__messages_in_queue_set = Set(MESSAGE_IDS_IN_QUEUE_SET_NAME)
        self.__message_queue = List(MESSAGE_QUEUE_LIST_NAME)

    def send_message(self, payload: str, from_username: str, to_username: str):
        message_id = self.__message_prefix + self.__next_id_message.increment()
        message = Hash(message_id)
        message.set_all({
            'payload': payload,
            'from': from_username,
            'to': to_username
        })
        Set(self.__outcoming__messages_prefix + from_username).add(message_id)
        self.__created_messages_set.add(message_id)
        self.__message_queue.add(message_id)
        self.__messages_in_queue_set.add(message_id)

    def read_messages(self, username: str):
        incoming_messages_list = List(self.__incoming_message_prefix + username)
        messages = incoming_messages_list.get_all()
        return [Hash(message_id).get('payload') for message_id in messages]
