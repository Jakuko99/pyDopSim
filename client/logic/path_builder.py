import logging

from .re_paths import re_paths, REPaths, Path
from game.api_package import REStation, SwitchPosition, TrackState


class PathBuilder:
    def __init__(self, relief: REStation, relief_type: str = "RE"):
        self.relief: REStation = relief

        self.logger = logging.getLogger("App.Client.PathBuilder")
        self.logger.setLevel(logging.DEBUG)

        if relief_type == "RE":
            self.path_collection: REPaths = re_paths

    def build_path(self, start_signal: str, end_signal: str):
        path: Path = self.path_collection.get_path(start_signal, end_signal)
        if path.start_signal is not None:
            for switch in path.switches.keys():
                self.relief.get_switch(switch).switch_position = path.switches[switch]
                self.relief.get_switch(switch).set_state(TrackState.RESERVED)

            self.logger.debug(f"Path from {start_signal} to {end_signal} is built")
        else:
            self.logger.error(f"Path from {start_signal} to {end_signal} is not found")
    
