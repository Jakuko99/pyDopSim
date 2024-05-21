import logging
from queue import Queue

import game.api_package as game
import utils.api_package as utils

# ----- logger configuration -----
logger = logging.getLogger("App")
logger.setLevel(logging.DEBUG)

# ----- queue handler -----
logger.addHandler(utils.queue_handler)

if __name__ == "__main__":
    app = game.StationTest()
    app.add_test_bindings()
    logger.info("PyDopSim started in testmode")

    app.run()
