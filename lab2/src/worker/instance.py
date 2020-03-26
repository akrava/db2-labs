import sys
import signal
from rs.wrappers.list import List
from rs.wrappers.hash import Hash
from rs.wrappers.set import Set
from rs.wrappers.zset import ZSet
from rs.wrappers.pub_sub import PubSub
from worker.message_processor import MessageProcessor
from rs.settings import MESSAGE_QUEUE_LIST_NAME, JOURNAL_ACTIVITIES_NAME, MESSAGE_IDS_DELIVERED_SET_NAME, \
    MESSAGE_IDS_SEND_SET_NAME, MESSAGE_IDS_BLOCKED_SET_NAME, MESSAGE_IDS_PROCESSING_SET_NAME, \
    MESSAGE_IDS_IN_QUEUE_SET_NAME, USER_INCOMING_MESSAGES_LIST_PREFIX, ACTIVE_USERS_ZSET_NAME, SPAMERS_ZSET_NAME


class WorkerInstance:
    def __init__(self, processor: MessageProcessor, is_in_thread: bool = False):
        self.__message_queue = List(MESSAGE_QUEUE_LIST_NAME)
        self.__message_processor = processor
        self.__messages_in_queue_status_set = Set(MESSAGE_IDS_IN_QUEUE_SET_NAME)
        self.__messages_processing_status_set = Set(MESSAGE_IDS_PROCESSING_SET_NAME)
        self.__messages_blocked_status_set = Set(MESSAGE_IDS_BLOCKED_SET_NAME)
        self.__messages_send_status_set = Set(MESSAGE_IDS_SEND_SET_NAME)
        self.__messages_delivered_status_set = Set(MESSAGE_IDS_DELIVERED_SET_NAME)
        self.__incoming_message_prefix = USER_INCOMING_MESSAGES_LIST_PREFIX
        self.__active_users_zset = ZSet(ACTIVE_USERS_ZSET_NAME)
        self.__active_spamers_zset = ZSet(SPAMERS_ZSET_NAME)
        self.__journal_pub_sub = PubSub(JOURNAL_ACTIVITIES_NAME)
        if not is_in_thread:
            signal.signal(signal.SIGINT, self.__handle_interrupt_event)

    def run(self):
        while True:
            message_id = self.__message_queue.remove_blocking()
            self.__messages_in_queue_status_set.move_to(MESSAGE_IDS_PROCESSING_SET_NAME, message_id)
            message = Hash(message_id)
            sender = message.get('from')
            message_payload = message.get('payload')
            receiver = message.get('to')
            if self.__message_processor.validate_message(message_payload):
                self.__messages_processing_status_set.move_to(MESSAGE_IDS_SEND_SET_NAME, message_id)
                List(self.__incoming_message_prefix + receiver).add(message_id)
                self.__messages_send_status_set.move_to(MESSAGE_IDS_DELIVERED_SET_NAME, message_id)
                self.__active_users_zset.add(sender, 1)
                self.__journal_pub_sub.publish("User `%s` send message `%s` to user `%s`" %
                                               (sender, message_payload, receiver))
            else:
                self.__messages_processing_status_set.move_to(MESSAGE_IDS_BLOCKED_SET_NAME, message_id)
                self.__active_spamers_zset.add(sender, 1)
                self.__journal_pub_sub.publish("User `%s` tried to send SPAM `%s` to user `%s`" %
                                               (sender, message_payload, receiver))

    @staticmethod
    def __handle_interrupt_event(_sig, _frame):
        sys.exit(0)
