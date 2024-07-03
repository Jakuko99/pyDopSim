from game.api_package import SwitchPosition
from .path import Path


class REPaths:
    def __init__(self):
        self.paths: list[Path] = list()

    def add_path(self, path: Path):
        self.paths.append(path)

    def get_path(self, start_signal: str, end_signal: str) -> Path:
        for path in self.paths:
            if path.start_signal == start_signal and path.end_signal == end_signal:
                return path
        return Path(None, None)  # return empty path if not found


re_paths = REPaths()  # singleton

# ----- shunting paths -----
shunting_Se1_S1 = Path("Se1", "S1", shunt_path=True)
shunting_Se1_S1.add_switch(
    {
        "1_3": SwitchPosition.Z_DOWN_STRAIGHT,
        "2": SwitchPosition.STRAIGHT,
    }
)
shunting_Se1_S1.add_track("1")
re_paths.add_path(shunting_Se1_S1)

shunting_S1_Se1 = Path("S1", "Se1", shunt_path=True)
shunting_S1_Se1.add_switch(
    {
        "2": SwitchPosition.STRAIGHT,
        "1_3": SwitchPosition.Z_DOWN_STRAIGHT,
    }
)
shunting_S1_Se1.add_track("1L")
re_paths.add_path(shunting_S1_Se1)

shunting_Se1_S2 = Path("Se1", "S2", shunt_path=True)
shunting_Se1_S2.add_switch(
    {
        "1_3": SwitchPosition.Z_DOWN_STRAIGHT,
        "2": SwitchPosition.TURNED,
        "4": SwitchPosition.STRAIGHT,
    }
)
shunting_Se1_S2.add_track("2")
re_paths.add_path(shunting_Se1_S2)

shunting_S2_Se1 = Path("S2", "Se1", shunt_path=True)
shunting_S2_Se1.add_switch(
    {
        "1_3": SwitchPosition.Z_DOWN_STRAIGHT,
        "2": SwitchPosition.TURNED,
        "4": SwitchPosition.STRAIGHT,
    }
)
shunting_S2_Se1.add_track("1L")
re_paths.add_path(shunting_S2_Se1)

shunting_Se1_S3 = Path("Se1", "S3", shunt_path=True)
shunting_Se1_S3.add_switch(
    {
        "1_3": SwitchPosition.TURNED,
        "5": SwitchPosition.STRAIGHT,
    }
)
shunting_Se1_S3.add_track("3")
re_paths.add_path(shunting_Se1_S3)

shunting_S3_Se1 = Path("S3", "Se1", shunt_path=True)
shunting_S3_Se1.add_switch(
    {
        "5": SwitchPosition.STRAIGHT,
        "1_3": SwitchPosition.TURNED,
    }
)
shunting_S3_Se1.add_track("1L")
re_paths.add_path(shunting_S3_Se1)

shunting_Se1_Se3 = Path("Se1", "Se3", shunt_path=True)
shunting_Se1_Se3.add_switch(
    {
        "1_3": SwitchPosition.Z_DOWN_STRAIGHT,
        "2": SwitchPosition.TURNED,
        "4": SwitchPosition.TURNED,
    }
)
shunting_Se1_Se3.add_track("4")
re_paths.add_path(shunting_Se1_Se3)

shunting_Se3_Se1 = Path("Se3", "Se1", shunt_path=True)
shunting_Se3_Se1.add_switch(
    {
        "4": SwitchPosition.TURNED,
        "2": SwitchPosition.TURNED,
        "1_3": SwitchPosition.Z_DOWN_STRAIGHT,
    }
)
shunting_Se3_Se1.add_track("1L")
re_paths.add_path(shunting_Se3_Se1)

shunting_Se1_S5 = Path("Se1", "S5", shunt_path=True)
shunting_Se1_S5.add_switch(
    {
        "1_3": SwitchPosition.TURNED,
        "5": SwitchPosition.TURNED,
    }
)
shunting_Se1_S5.add_track("5")
re_paths.add_path(shunting_Se1_S5)

shunting_S5_Se1 = Path("S5", "Se1", shunt_path=True)
shunting_S5_Se1.add_switch(
    {
        "5": SwitchPosition.TURNED,
        "1_3": SwitchPosition.TURNED,
    }
)
shunting_S5_Se1.add_track("1L")
re_paths.add_path(shunting_S5_Se1)

shunting_Se2_S3 = Path("Se2", "S3", shunt_path=True)
shunting_Se2_S3.add_switch(
    {
        "1_3": SwitchPosition.Z_UP_STRAIGHT,
        "5": SwitchPosition.STRAIGHT,
    }
)
shunting_Se2_S3.add_track("3")
re_paths.add_path(shunting_Se2_S3)

shunting_S3_Se2 = Path("S3", "Se2", shunt_path=True)
shunting_S3_Se2.add_switch(
    {
        "5": SwitchPosition.STRAIGHT,
        "1_3": SwitchPosition.Z_UP_STRAIGHT,
    }
)
shunting_S3_Se2.add_track("2L")
re_paths.add_path(shunting_S3_Se2)

shunting_Se2_S5 = Path("Se2", "S5", shunt_path=True)
shunting_Se2_S5.add_switch(
    {
        "1_3": SwitchPosition.Z_UP_STRAIGHT,
        "5": SwitchPosition.TURNED,
    }
)
shunting_Se2_S5.add_track("5")
re_paths.add_path(shunting_Se2_S5)

shunting_S5_Se2 = Path("S5", "Se2", shunt_path=True)
shunting_S5_Se2.add_switch(
    {
        "5": SwitchPosition.TURNED,
        "1_3": SwitchPosition.Z_UP_STRAIGHT,
    }
)
shunting_S5_Se2.add_track("2L")
re_paths.add_path(shunting_S5_Se2)

shunting_Se4_Se5 = Path("Se4", "Se5", shunt_path=True)
shunting_Se4_Se5.add_switch(
    {
        "6_7": SwitchPosition.Z_DOWN_STRAIGHT,
    }
)
shunting_Se4_Se5.add_track("4a")
re_paths.add_path(shunting_Se4_Se5)

shunting_Se5_Se4 = Path("Se5", "Se4", shunt_path=True)
shunting_Se5_Se4.add_switch(
    {
        "6_7": SwitchPosition.Z_DOWN_STRAIGHT,
    }
)
shunting_Se5_Se4.add_track("4")
re_paths.add_path(shunting_Se5_Se4)

shunting_Se6_Se4 = Path("Se6", "Se4", shunt_path=True)
shunting_Se6_Se4.add_switch(
    {
        "10": SwitchPosition.STRAIGHT,
        "9": SwitchPosition.TURNED,
        "6_7": SwitchPosition.TURNED,
    }
)
shunting_Se6_Se4.add_track("4")
re_paths.add_path(shunting_Se6_Se4)

shunting_Se4_Se6 = Path("Se4", "Se6", shunt_path=True)
shunting_Se4_Se6.add_switch(
    {
        "6_7": SwitchPosition.TURNED,
        "9": SwitchPosition.TURNED,
        "10": SwitchPosition.STRAIGHT,
    }
)
shunting_Se4_Se6.add_track("S")
re_paths.add_path(shunting_Se4_Se6)

shunting_Se6_L2 = Path("Se6", "L2", shunt_path=True)
shunting_Se6_L2.add_switch(
    {
        "10": SwitchPosition.STRAIGHT,
        "9": SwitchPosition.TURNED,
        "6_7": SwitchPosition.Z_UP_STRAIGHT,
    }
)
shunting_Se6_L2.add_track("2")
re_paths.add_path(shunting_Se6_L2)

shunting_L2_Se6 = Path("L2", "Se6", shunt_path=True)
shunting_L2_Se6.add_switch(
    {
        "6_7": SwitchPosition.Z_UP_STRAIGHT,
        "9": SwitchPosition.TURNED,
        "10": SwitchPosition.STRAIGHT,
    }
)
shunting_L2_Se6.add_track("S")
re_paths.add_path(shunting_L2_Se6)

shunting_Se6_L1 = Path("Se6", "L1", shunt_path=True)
shunting_Se6_L1.add_switch(
    {
        "10": SwitchPosition.STRAIGHT,
        "9": SwitchPosition.STRAIGHT,
    }
)
shunting_Se6_L1.add_track("1")
re_paths.add_path(shunting_Se6_L1)

shunting_L1_Se6 = Path("L1", "Se6", shunt_path=True)
shunting_L1_Se6.add_switch(
    {
        "9": SwitchPosition.STRAIGHT,
        "10": SwitchPosition.STRAIGHT,
    }
)
shunting_L1_Se6.add_track("S")
re_paths.add_path(shunting_L1_Se6)

shunting_Se6_L3 = Path("Se6", "L3", shunt_path=True)
shunting_Se6_L3.add_switch(
    {
        "10": SwitchPosition.TURNED,
        "8": SwitchPosition.STRAIGHT,
    }
)
shunting_Se6_L3.add_track("3")
re_paths.add_path(shunting_Se6_L3)

shunting_L3_Se6 = Path("L3", "Se6", shunt_path=True)
shunting_L3_Se6.add_switch(
    {
        "8": SwitchPosition.STRAIGHT,
        "10": SwitchPosition.TURNED,
    }
)
shunting_L3_Se6.add_track("S")
re_paths.add_path(shunting_L3_Se6)

shunting_Se6_L5 = Path("Se6", "L5", shunt_path=True)
shunting_Se6_L5.add_switch(
    {
        "10": SwitchPosition.TURNED,
        "8": SwitchPosition.TURNED,
    }
)
shunting_Se6_L5.add_track("5")
re_paths.add_path(shunting_Se6_L5)

shunting_L5_Se6 = Path("L5", "Se6", shunt_path=True)
shunting_L5_Se6.add_switch(
    {
        "8": SwitchPosition.TURNED,
        "10": SwitchPosition.TURNED,
    }
)
shunting_L5_Se6.add_track("S")
re_paths.add_path(shunting_L5_Se6)

# ----- normal paths -----
path_1L_S1 = Path("1L", "S1")
path_1L_S1.add_switch(
    {
        "1_3": SwitchPosition.Z_DOWN_STRAIGHT,
        "2": SwitchPosition.STRAIGHT,
    }
)
path_1L_S1.add_track("1")
path_1L_S1.add_track("1L")
re_paths.add_path(path_1L_S1)

path_1L_S2 = Path("1L", "S2")
path_1L_S2.add_switch(
    {
        "1_3": SwitchPosition.Z_DOWN_STRAIGHT,
        "2": SwitchPosition.TURNED,
        "4": SwitchPosition.STRAIGHT,
    }
)
path_1L_S2.add_track("2")
path_1L_S2.add_track("1L")
re_paths.add_path(path_1L_S2)

path_1L_S3 = Path("1L", "S3")
path_1L_S3.add_switch(
    {
        "1_3": SwitchPosition.TURNED,
        "5": SwitchPosition.STRAIGHT,
    }
)
path_1L_S3.add_track("3")
path_1L_S3.add_track("1L")
re_paths.add_path(path_1L_S3)

path_1L_S5 = Path("1L", "S5")
path_1L_S5.add_switch(
    {
        "1_3": SwitchPosition.TURNED,
        "5": SwitchPosition.TURNED,
    }
)
path_1L_S5.add_track("5")
path_1L_S5.add_track("1L")
re_paths.add_path(path_1L_S5)

path_2L_S3 = Path("2L", "S3")
path_2L_S3.add_switch(
    {
        "1_3": SwitchPosition.Z_UP_STRAIGHT,
        "5": SwitchPosition.STRAIGHT,
    }
)
path_2L_S3.add_track("3")
path_2L_S3.add_track("2L")
re_paths.add_path(path_2L_S3)

path_2L_S5 = Path("2L", "S5")
path_2L_S5.add_switch(
    {
        "1_3": SwitchPosition.Z_UP_STRAIGHT,
        "5": SwitchPosition.TURNED,
    }
)
path_2L_S5.add_track("5")
path_2L_S5.add_track("2L")
re_paths.add_path(path_2L_S5)

path_S1_1L = Path("S1", "1L")
path_S1_1L.add_switch(
    {
        "2": SwitchPosition.STRAIGHT,
        "1_3": SwitchPosition.Z_DOWN_STRAIGHT,
    }
)
path_S1_1L.add_track("1L")
re_paths.add_path(path_S1_1L)

path_S2_1L = Path("S2", "1L")
path_S2_1L.add_switch(
    {
        "4": SwitchPosition.STRAIGHT,
        "2": SwitchPosition.TURNED,
        "1_3": SwitchPosition.Z_DOWN_STRAIGHT,
    }
)
path_S2_1L.add_track("1L")
re_paths.add_path(path_S2_1L)

path_S3_1L = Path("S3", "1L")
path_S3_1L.add_switch(
    {
        "5": SwitchPosition.STRAIGHT,
        "1_3": SwitchPosition.TURNED,
    }
)
path_S3_1L.add_track("1L")
re_paths.add_path(path_S3_1L)

path_S5_1L = Path("S5", "1L")
path_S5_1L.add_switch(
    {
        "5": SwitchPosition.TURNED,
        "1_3": SwitchPosition.TURNED,
    }
)
path_S5_1L.add_track("1L")
re_paths.add_path(path_S5_1L)

path_S3_2L = Path("S3", "2L")
path_S3_2L.add_switch(
    {
        "5": SwitchPosition.STRAIGHT,
        "1_3": SwitchPosition.Z_UP_STRAIGHT,
    }
)
path_S3_2L.add_track("2L")
re_paths.add_path(path_S3_2L)

path_S5_2L = Path("S5", "2L")
path_S5_2L.add_switch(
    {
        "5": SwitchPosition.TURNED,
        "1_3": SwitchPosition.Z_UP_STRAIGHT,
    }
)
path_S5_2L.add_track("2L")
re_paths.add_path(path_S5_2L)

path_S_L1 = Path("S", "L1")
path_S_L1.add_switch(
    {
        "9": SwitchPosition.STRAIGHT,
        "10": SwitchPosition.STRAIGHT,
    }
)
path_S_L1.add_track("S")
path_S_L1.add_track("1")
re_paths.add_path(path_S_L1)

path_S_L2 = Path("S", "L2")
path_S_L2.add_switch(
    {
        "10": SwitchPosition.STRAIGHT,
        "9": SwitchPosition.TURNED,
        "6_7": SwitchPosition.Z_UP_STRAIGHT,
    }
)
path_S_L2.add_track("2")
path_S_L2.add_track("S")
re_paths.add_path(path_S_L2)

path_S_L3 = Path("S", "L3")
path_S_L3.add_switch(
    {
        "10": SwitchPosition.TURNED,
        "8": SwitchPosition.STRAIGHT,
    }
)
path_S_L3.add_track("3")
path_S_L3.add_track("S")
re_paths.add_path(path_S_L3)

path_S_L5 = Path("S", "L5")
path_S_L5.add_switch(
    {
        "10": SwitchPosition.TURNED,
        "8": SwitchPosition.TURNED,
    }
)
path_S_L5.add_track("5")
path_S_L5.add_track("S")
re_paths.add_path(path_S_L5)

path_L1_S = Path("L1", "S")
path_L1_S.add_switch(
    {
        "9": SwitchPosition.STRAIGHT,
        "10": SwitchPosition.STRAIGHT,
    }
)
path_L1_S.add_track("S")
re_paths.add_path(path_L1_S)

path_L2_S = Path("L2", "S")
path_L2_S.add_switch(
    {
        "10": SwitchPosition.STRAIGHT,
        "9": SwitchPosition.TURNED,
        "6_7": SwitchPosition.Z_UP_STRAIGHT,
    }
)
path_L2_S.add_track("S")
re_paths.add_path(path_L2_S)

path_L3_S = Path("L3", "S")
path_L3_S.add_switch(
    {
        "10": SwitchPosition.TURNED,
        "8": SwitchPosition.STRAIGHT,
    }
)
path_L3_S.add_track("S")
re_paths.add_path(path_L3_S)

path_L5_S = Path("L5", "S")
path_L5_S.add_switch(
    {
        "10": SwitchPosition.TURNED,
        "8": SwitchPosition.TURNED,
    }
)
path_L5_S.add_track("S")
re_paths.add_path(path_L5_S)

path_1L_S = Path("1L", "S")
path_1L_S.add_switch(
    {
        "1_3": SwitchPosition.Z_DOWN_STRAIGHT,
        "2": SwitchPosition.STRAIGHT,
        "9": SwitchPosition.STRAIGHT,
        "10": SwitchPosition.STRAIGHT,
    }
)
path_1L_S.add_track("1", require_free=True)
path_1L_S.add_track("1L")
path_1L_S.add_track("S")
re_paths.add_path(path_1L_S)

path_2L_S = Path("2L", "S")
path_2L_S.add_switch(
    {
        "1_3": SwitchPosition.Z_UP_STRAIGHT,
        "5": SwitchPosition.STRAIGHT,
        "8": SwitchPosition.STRAIGHT,
        "10": SwitchPosition.TURNED,
    }
)
path_2L_S.add_track("3", require_free=True)
path_2L_S.add_track("2L")
path_2L_S.add_track("S")
re_paths.add_path(path_2L_S)

path_S_1L = Path("S", "1L")
path_S_1L.add_switch(
    {
        "2": SwitchPosition.STRAIGHT,
        "1_3": SwitchPosition.Z_DOWN_STRAIGHT,
        "9": SwitchPosition.STRAIGHT,
        "10": SwitchPosition.STRAIGHT,
    }
)
path_S_1L.add_track("1L")
path_S_1L.add_track("S")
path_S_1L.add_track("1", require_free=True)
re_paths.add_path(path_S_1L)

path_S_2L = Path("S", "2L")
path_S_2L.add_switch(
    {
        "1_3": SwitchPosition.Z_UP_STRAIGHT,
        "5": SwitchPosition.STRAIGHT,
        "8": SwitchPosition.STRAIGHT,
        "10": SwitchPosition.TURNED,
    }
)
path_S_2L.add_track("2L")
path_S_2L.add_track("S")
path_S_2L.add_track("3", require_free=True)
re_paths.add_path(path_S_2L)
