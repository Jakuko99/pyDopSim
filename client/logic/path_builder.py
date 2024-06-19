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
            self.active_paths: list[Path] = []

    def build_path(self, start_signal: str, end_signal: str):
        path: Path = self.path_collection.get_path(start_signal, end_signal)
        if (
            path.start_signal is not None
            and self.check_duplicity(start_signal, end_signal) is False
        ):  # don't allow to build path that ends or starts at the same signal
            for switch in path.switches.keys():
                if (
                    switch == "1_3" or switch == "6_7"
                ):  # to be able to have paths on both sides of switch
                    if (
                        self.relief.get_switch(switch).switch_position
                        == SwitchPosition.Z_DOWN_STRAIGHT
                        or self.relief.get_switch(switch).switch_position
                        == SwitchPosition.Z_UP_STRAIGHT
                    ) and path.switches[switch] in [
                        SwitchPosition.Z_DOWN_STRAIGHT,
                        SwitchPosition.Z_UP_STRAIGHT,
                    ]:
                        self.relief.get_switch(switch).set_position(
                            SwitchPosition.Z_BOTH
                        )  # TODO: needs to be fixed
                    else:
                        self.relief.get_switch(switch).set_position(
                            path.switches[switch]
                        )
                else:
                    self.relief.get_switch(switch).set_position(path.switches[switch])

                self.relief.get_switch(switch).set_state(TrackState.RESERVED)

            for track in path.tracks:
                self.relief.get_track(track).set_state(TrackState.RESERVED)

            self.logger.debug(f"Path from {start_signal} to {end_signal} is built")
            self.relief.stop_blinking()
            self.active_paths.append(path)
        else:
            self.logger.error(
                f"Path from {start_signal} to {end_signal} is not found or already exists"
            )
            self.relief.stop_blinking()

    def cancel_path(self, start_signal: str):
        path_to_cancel: Path = None
        for path in self.active_paths:
            if path.start_signal == start_signal:
                path_to_cancel = path
        if path_to_cancel:
            for switch in path.switches.keys():
                self.relief.get_switch(switch).switch_position = path.switches[switch]
                if (
                    not self.relief.get_switch(switch).occupancy_status
                    is TrackState.OCCUPIED
                ):
                    if switch == "1_3" or switch == "6_7":
                        if (
                            self.relief.get_switch(switch).switch_position
                            == SwitchPosition.Z_BOTH
                        ):
                            self.relief.get_switch(switch).set_state(
                                TrackState.FREE,
                                (
                                    SwitchPosition.Z_DOWN_STRAIGHT
                                    if path.switches[switch]
                                    is SwitchPosition.Z_UP_STRAIGHT
                                    else SwitchPosition.Z_DOWN_STRAIGHT
                                ),
                            )
                    else:
                        self.relief.get_switch(switch).set_state(TrackState.FREE)

            for track in path.tracks:
                if not self.relief.get_track(track).state is TrackState.OCCUPIED:
                    self.relief.get_track(track).set_state(TrackState.FREE)

            self.logger.debug(f"Path from {start_signal} is cancelled")
            self.active_paths.remove(path_to_cancel)
        else:
            self.logger.error(f"Path from {start_signal} is not found")

    def check_duplicity(self, start_signal: str, end_signal: str):
        for path in self.active_paths:
            if (path.start_signal == start_signal or path.end_signal == end_signal) or (
                path.start_signal == end_signal or path.end_signal == start_signal
            ):
                return True
        return False
