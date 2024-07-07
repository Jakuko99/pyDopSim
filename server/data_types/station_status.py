from enum import Enum, auto


class StationStatus(Enum):
    ONLINE = "ONLINE"
    OFFLINE = "OFFLINE"
    UNKNOWN = "UNKNOWN"
    BUSY = "BUSY"
