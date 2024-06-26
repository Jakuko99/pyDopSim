from enum import Enum, auto


class StationStatus(Enum):
    ONLINE = auto()
    OFFLINE = auto()
    UNKNOWN = auto()
    BUSY = auto()
