import sys
import signal
from threading import Thread
from random import randrange
from worker.spam_random import SpamRandomMessageProcessor
from worker.instance import WorkerInstance
from rs.controller.clients import Clients
from rs.controller.messages import Messages
from rs.connection import RedisClient
from settings import MESSAGE_PROCESSING_DELAY_MS, MESSAGE_PROCESSING_DELAY_RANGE_MS, SPAM_NICENESS

workers = []
usernames = []


def handle_interrupt_event(_sig, _frame):
    client_controller = Clients()
    for x in usernames:
        client_controller.logout_user(x)
    sys.exit(0)


def threaded_worker_function():
    pr = SpamRandomMessageProcessor(MESSAGE_PROCESSING_DELAY_MS, MESSAGE_PROCESSING_DELAY_RANGE_MS, SPAM_NICENESS)
    instance = WorkerInstance(pr, True)
    try:
        instance.run()
    except:
       pass


def send_messages(count_users: int):
    user_prefix = "user_id_"
    client_controller = Clients()
    message_controller = Messages()
    for idx in range(count_users):
        usernames.append(user_prefix + str(idx))
        client_controller.register_client(usernames[idx])
        client_controller.login_client(usernames[idx])
    index = 0
    while True:
        from_username = user_prefix + str(randrange(len(usernames)))
        to_username = from_username
        while to_username != from_username:
            to_username = user_prefix + str(randrange(len(usernames)))
        message = "test-id" + str(index)
        index += 1
        message_controller.send_message(message, from_username, to_username)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Need two argument")
        sys.exit(1)
    else:
        try:
            count_workers = int(sys.argv[1])
            max_users = int(sys.argv[2])
        except Exception as e:
            print(e)
            sys.exit(1)
        for i in range(count_workers):
            thread = Thread(target=threaded_worker_function)
            workers.append(thread)
            thread.start()
        signal.signal(signal.SIGINT, handle_interrupt_event)
        RedisClient().get_connection().flushall()
        send_messages(max_users)
