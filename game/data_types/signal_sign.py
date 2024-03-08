from enum import Enum, auto


class SignalSign(Enum):
    STOP = auto()
    FREE = auto()
    SHUNT = auto()
    SHUNT_PROHIBITED = auto()
    EXP40 = auto()
    EXP40_40 = auto()

    # ----- AB signals -----
    AB_STOP = auto()
    AB_FREE = auto()
    AB_WARN = auto()
