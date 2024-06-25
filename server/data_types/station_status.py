from enum import Enum, auto


class StationStatus(Enum):
    ONLINE = auto()
    OFFLINE = auto()
    AVAILABLE = auto()
    UNKNOWN = auto()
    BUSY = auto()
