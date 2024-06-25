import logging
from PyQt5.QtWidgets import QApplication

from utils.api_package import queue_handler
from launcher.api_package import Launcher

# ----- logger configuration -----
logger = logging.getLogger("App")
logger.setLevel(logging.DEBUG)
log_format = logging.Formatter(
    "[%(asctime)s][%(levelname)s] - %(name)s: %(message)s", datefmt="%d-%m-%y %H:%M:%S"
)
logger.addHandler(queue_handler)

if __name__ == "__main__":
    app = QApplication([])
    launcher = Launcher(log_pipe=queue_handler.get_logging_pipe())
    launcher.show()
    app.exec_()
