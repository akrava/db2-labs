from rs.wrappers.int import Int
from rs.wrappers.set import Set
from rs.wrappers.hash import Hash
from rs.wrappers.list import List
from rs.settings import USER_INCOMING_MESSAGES_LIST_PREFIX, MESSAGE_NEXT_ID_NAME, MESSAGES_HASH_SET_PREFIX,\
    MESSAGE_IDS_CREATED_SET_NAME, MESSAGE_IDS_IN_QUEUE_SET_NAME, MESSAGE_QUEUE_LIST_NAME, \
    USER_OUTCOMING_MESSAGES_SET_PREFIX, MESSAGE_IDS_PROCESSING_SET_NAME, MESSAGE_IDS_BLOCKED_SET_NAME, \
    MESSAGE_IDS_SEND_SET_NAME, MESSAGE_IDS_DELIVERED_SET_NAME


class Messages:
    def __init__(self):
        self.__next_id_message = Int(MESSAGE_NEXT_ID_NAME)
        if not self.__next_id_message.exists():
            self.__next_id_message.set(0)
        # message storage
        self.__message_prefix = MESSAGES_HASH_SET_PREFIX
        # sets of messages ids for users
        self.__incoming_message_prefix = USER_INCOMING_MESSAGES_LIST_PREFIX
        self.__outcoming__messages_prefix = USER_OUTCOMING_MESSAGES_SET_PREFIX
        # processing queue
        self.__message_queue = List(MESSAGE_QUEUE_LIST_NAME)
        # status sets
        self.__created_messages_status_set = Set(MESSAGE_IDS_CREATED_SET_NAME)
        self.__messages_in_queue_status_set = Set(MESSAGE_IDS_IN_QUEUE_SET_NAME)

    def send_message(self, payload: str, from_username: str, to_username: str):
        if not isinstance(payload, str) or len(payload) < 3:
            raise Exception("Length of message should be >= 3")
        message_id = self.__message_prefix + str(self.__next_id_message.increment())
        message = Hash(message_id)
        message.set_all({
            'payload': payload,
            'from': from_username,
            'to': to_username
        })
        Set(self.__outcoming__messages_prefix + from_username).add(message_id)
        self.__created_messages_status_set.add(message_id)
        self.__message_queue.add(message_id)
        self.__created_messages_status_set.move_to(self.__messages_in_queue_status_set.get_name(), message_id)

    def read_messages(self, username: str):
        incoming_messages_list = List(self.__incoming_message_prefix + username)
        messages = incoming_messages_list.get_all()
        return [Hash(message_id).get('payload') for message_id in messages]

    def count_messages_by_statuses(self, username: str, status: [int]):
        if len(status) == 0:
            return 0
        statuses_names_constant = [MESSAGE_IDS_CREATED_SET_NAME, MESSAGE_IDS_IN_QUEUE_SET_NAME,
                                   MESSAGE_IDS_PROCESSING_SET_NAME, MESSAGE_IDS_BLOCKED_SET_NAME,
                                   MESSAGE_IDS_SEND_SET_NAME, MESSAGE_IDS_DELIVERED_SET_NAME]
        statuses_set_names = []
        for index in status:
            statuses_set_names.append(statuses_names_constant[index])
        self.__created_messages_status_set.union(statuses_set_names, 'temp')
        messages_outcoming_set_name = self.__outcoming__messages_prefix + username
        return self.__created_messages_status_set.intersect([messages_outcoming_set_name, 'temp'], 'temp')
