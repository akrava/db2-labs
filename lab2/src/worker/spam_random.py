import logging
from worker.message_processor import MessageProcessor
from random import randrange
from time import sleep


class SpamRandomMessageProcessor(MessageProcessor):
    def __init__(self, delay: int, delay_range: int, spam_niceness: int):
        self.__delay = delay
        self.__delay_range = delay_range
        self.__spam_niceness = spam_niceness
        logging.basicConfig(level=logging.INFO)

    def validate_message(self, message: str) -> bool:
        logging.info("Processing msg: `%s`" % message)
        count_ms = self.__delay + randrange(self.__delay_range)
        sleep(count_ms / 1000)
        res = randrange(10) % self.__spam_niceness != 0
        logging.info("Is valid: `%s`" % str(res))
        return res
