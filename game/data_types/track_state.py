from enum import Enum, auto


class TrackState(Enum):
    FREE = auto()
    OCCUPIED = auto()
    CLOSURE = auto()
    RESERVED = auto()
    ALL = auto()  # only for switches in blink mode
    TEST = auto()
