from enum import Enum, auto


class SignalSign(Enum):
    STOP = auto()
    SUMMON = auto()
    FREE = auto()
    SHUNT = auto()
    SHUNT_PROHIBITED = auto()
    WARN = auto()
    WARN_40 = auto()
    EXP40 = auto()
    EXP60 = auto()
    EXP80 = auto()
    SDP40_FREE = auto()
    EXP40_40 = auto()
    EXP40_60 = auto()

    # ----- AB signals -----
    AB_STOP = auto()
    AB_FREE = auto()
    AB_WARN = auto()
    AB_EXP40 = auto()
    AB_EXP60 = auto()
    AB_EXP80 = auto()
