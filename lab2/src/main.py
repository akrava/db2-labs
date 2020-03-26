import sys
from ui.common import App
from worker.spam_random import SpamRandomMessageProcessor
from worker.instance import WorkerInstance
from settings import MESSAGE_PROCESSING_DELAY_MS, MESSAGE_PROCESSING_DELAY_RANGE_MS, SPAM_NICENESS

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Need one argument")
        sys.exit(1)
    if sys.argv[1] == "--cui":
        App().run()
    elif sys.argv[1] == "--worker":
        print("Starting worker")
        pr = SpamRandomMessageProcessor(MESSAGE_PROCESSING_DELAY_MS, MESSAGE_PROCESSING_DELAY_RANGE_MS, SPAM_NICENESS)
        instance = WorkerInstance(pr)
        instance.run()
    else:
        print("Unknown argument")
        sys.exit(1)
