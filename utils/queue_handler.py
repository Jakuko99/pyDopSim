import logging
from queue import Queue


class QueueHandler(logging.StreamHandler):
    def __init__(self):
        super().__init__()
        self.queue: Queue = Queue()

    def emit(self, record: logging.LogRecord):
        if (
            record.name == "uvicorn.error" or record.name == "uvicorn.access"
        ):  # rename uvicorn loggers
            record.name = "App.RESTServer.uvicorn"

        msg: str = self.format(record)

        self.queue.put({"log": msg, "level": record.levelname})

    def get_logging_pipe(self) -> Queue:
        return self.queue


log_format = logging.Formatter(
    "[%(asctime)s][%(levelname)s] - %(name)s: %(message)s", datefmt="%d-%m-%y %H:%M:%S"
)
queue_handler: QueueHandler = QueueHandler()  # singleton for obtaining logging pipe
queue_handler.setFormatter(log_format)
queue_handler.setLevel(logging.DEBUG)

if __name__ == "__main__":
    handler = QueueHandler()
    logger = logging.getLogger("App")
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    log_format = logging.Formatter(
        "[%(asctime)s][%(levelname)s] - %(name)s: %(message)s",
        datefmt="%d-%m-%y %H:%M:%S",
    )
    handler.setFormatter(log_format)

    queue = handler.queue

    logger.info("test")
    logger.debug("test1")
    logger.warning("test2")
    logger.error("test3")
    logger.critical("test4")

    while not queue.empty():
        print(queue.get())
