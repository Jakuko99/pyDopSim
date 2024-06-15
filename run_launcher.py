import logging
from PyQt5.QtWidgets import QApplication

import utils.api_package as utils
from launcher.api_package import Launcher

# ----- logger configuration -----
logger = logging.getLogger("App")
logger.setLevel(logging.DEBUG)
log_format = logging.Formatter(
    "[%(asctime)s][%(levelname)s] - %(name)s: %(message)s", datefmt="%d-%m-%y %H:%M:%S"
)

# ----- queue handler -----
gui_handler = utils.QueueHandler()  # handler for GUI
gui_handler.setFormatter(log_format)
gui_handler.setLevel(logging.DEBUG)
logger.addHandler(gui_handler)

if __name__ == "__main__":
    app = QApplication([])
    launcher = Launcher(log_pipe=gui_handler.get_logging_pipe())
    launcher.show()
    app.exec_()
