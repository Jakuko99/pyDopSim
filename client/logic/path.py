from game.api_package import REStation, SwitchPosition


class Path:
    def __init__(self, start_signal: str, end_signal: str, shunt_path: bool = False):
        self.start_signal: str = start_signal
        self.end_signal: str = end_signal
        self.switches: dict[str:SwitchPosition] = dict()
        self.tracks: list[str] = list()
        self.free_tracks: list[str] = (
            list()
        )  # Tracks that need to be free to take this path
        self.shunt_path: bool = shunt_path

    def add_switch(self, switch: dict):
        self.switches.update(switch)

    def add_track(self, track: str, require_free: bool = False):
        self.tracks.append(track)
        if require_free:
            self.free_tracks.append(track)

    def verify(self, relief: REStation):
        for switch in self.switches:
            if relief.get_switch(switch).switch_position != self.switches[switch]:
                return False
        return True

    def __str__(self):
        return f"{self.start_signal} -> {self.end_signal} : {self.switches}"
