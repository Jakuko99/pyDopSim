from enum import Enum, auto


class SwitchType(Enum):
    Z_TYPE_LEFT = auto()
    Z_TYPE_RIGHT = auto()
    X_TYPE = auto()
    DOWN_45_LEFT = auto()
    UP_45_LEFT = auto()
    DOWN_45_RIGHT = auto()
    UP_45_RIGHT = auto()
