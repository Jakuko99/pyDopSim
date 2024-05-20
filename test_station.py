import logging
from queue import Queue

import game.api_package as game
import utils.api_package as utils

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
    app = game.StationTest(log_pipe=gui_handler.get_logging_pipe())
    app.add_test_bindings()
    logger.info("PyDopSim started in testmode")

    app.run()
