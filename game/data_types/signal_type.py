from enum import Enum, auto


class SignalType(Enum):
    SHUNTING_SIGNAL = auto()
    EXPECT_SIGNAL = auto()
    DEPARTURE_SIGNAL = auto()
    ENTRY_SIGNAL = auto()
