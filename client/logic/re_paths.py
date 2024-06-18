from game.api_package import SwitchPosition
from .path import Path


class REPaths:
    def __init__(self):
        self.paths: list[Path] = list()

    def add_path(self, path: Path):
        self.paths.append(path)

    def get_path(self, start_signal: str, end_signal: str) -> Path:
        for path in self.paths:
            if (
                path.start_signal == start_signal and path.end_signal == end_signal
            ) or (path.start_signal == end_signal and path.end_signal == start_signal):
                return path
        return Path(None, None)  # return empty path if not found


re_paths = REPaths()  # singleton

_1L_path_S1 = Path("1L", "S1")
_1L_path_S1.add_switch({"1_3": SwitchPosition.Z_DOWN_STRAIGHT})
_1L_path_S1.add_switch({"2": SwitchPosition.STRAIGHT})
_1L_path_S1.add_track("1")
_1L_path_S1.add_track("1L")
re_paths.add_path(_1L_path_S1)

_1L_path_S2 = Path("1L", "S2")
_1L_path_S2.add_switch({"1_3": SwitchPosition.Z_DOWN_STRAIGHT})
_1L_path_S2.add_switch({"2": SwitchPosition.TURNED})
_1L_path_S2.add_switch({"4": SwitchPosition.STRAIGHT})
re_paths.add_path(_1L_path_S2)

_1L_path_S3 = Path("1L", "S3")
_1L_path_S3.add_switch({"1_3": SwitchPosition.TURNED})
_1L_path_S3.add_switch({"5": SwitchPosition.STRAIGHT})
re_paths.add_path(_1L_path_S3)

_1L_path_Se3 = Path("1L", "Se3")
_1L_path_Se3.add_switch({"1_3": SwitchPosition.Z_DOWN_STRAIGHT})
_1L_path_Se3.add_switch({"2": SwitchPosition.TURNED})
_1L_path_Se3.add_switch({"4": SwitchPosition.TURNED})
re_paths.add_path(_1L_path_Se3)

_1L_path_S5 = Path("1L", "S5")
_1L_path_S5.add_switch({"1_3": SwitchPosition.TURNED})
_1L_path_S5.add_switch({"5": SwitchPosition.TURNED})
re_paths.add_path(_1L_path_S5)

_2L_path_S3 = Path("2L", "S3")
_2L_path_S3.add_switch({"1_3": SwitchPosition.Z_UP_STRAIGHT})
_2L_path_S3.add_switch({"5": SwitchPosition.STRAIGHT})
re_paths.add_path(_2L_path_S3)

_2L_path_S5 = Path("2L", "S5")
_2L_path_S5.add_switch({"1_3": SwitchPosition.Z_UP_STRAIGHT})
_2L_path_S5.add_switch({"5": SwitchPosition.TURNED})
re_paths.add_path(_2L_path_S5)

_S_path_L1 = Path("S", "L1")
_S_path_L1.add_switch({"10": SwitchPosition.STRAIGHT})
_S_path_L1.add_switch({"9": SwitchPosition.STRAIGHT})
re_paths.add_path(_S_path_L1)

_S_path_L2 = Path("S", "L2")
_S_path_L2.add_switch({"10": SwitchPosition.STRAIGHT})
_S_path_L2.add_switch({"9": SwitchPosition.TURNED})
_S_path_L2.add_switch({"6_7": SwitchPosition.Z_UP_STRAIGHT})
re_paths.add_path(_S_path_L2)

_S_path_L3 = Path("S", "L3")
_S_path_L3.add_switch({"10": SwitchPosition.TURNED})
_S_path_L3.add_switch({"8": SwitchPosition.STRAIGHT})
re_paths.add_path(_S_path_L3)

_S_path_L4 = Path("Se6", "Se4")
_S_path_L4.add_switch({"10": SwitchPosition.STRAIGHT})
_S_path_L4.add_switch({"9": SwitchPosition.TURNED})
_S_path_L4.add_switch({"6_7": SwitchPosition.TURNED})
re_paths.add_path(_S_path_L4)

_S_path_L5 = Path("S", "L5")
_S_path_L5.add_switch({"10": SwitchPosition.TURNED})
_S_path_L5.add_switch({"8": SwitchPosition.TURNED})
re_paths.add_path(_S_path_L5)

_Se5_path_Se4 = Path("Se5", "Se4")
_Se5_path_Se4.add_switch({"6_7": SwitchPosition.Z_DOWN_STRAIGHT})
re_paths.add_path(_Se5_path_Se4)
