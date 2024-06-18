from game.api_package import REStation, SwitchPosition


class Path:
    def __init__(self, start_signal: str, end_signal: str):
        self.start_signal: str = start_signal
        self.end_signal: str = end_signal
        self.switches: dict[str:SwitchPosition] = dict()

    def add_switch(self, switch: dict):
        self.switches.update(switch)

    def add_switches(self, switches: dict[str:SwitchPosition]):
        for switch in switches:
            self.switches.update(switch)

    def verify(self, relief: REStation):
        for switch in self.switches:
            if relief.get_switch(switch).switch_position != self.switches[switch]:
                return False
        return True

    def __str__(self):
        return f"{self.start_signal} -> {self.end_signal} : {self.switches}"
