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
shunting_Se1_S1.add_switch({"1_3": SwitchPosition.Z_DOWN_STRAIGHT})
shunting_Se1_S1.add_switch({"2": SwitchPosition.STRAIGHT})
shunting_Se1_S1.add_track("1")
re_paths.add_path(shunting_Se1_S1)

shunting_S1_Se1 = Path("S1", "Se1", shunt_path=True)
shunting_S1_Se1.add_switch({"2": SwitchPosition.STRAIGHT})
shunting_S1_Se1.add_switch({"1_3": SwitchPosition.Z_DOWN_STRAIGHT})
shunting_S1_Se1.add_track("1L")
re_paths.add_path(shunting_S1_Se1)

shunting_Se1_S2 = Path("Se1", "S2", shunt_path=True)
shunting_Se1_S2.add_switch({"1_3": SwitchPosition.Z_DOWN_STRAIGHT})
shunting_Se1_S2.add_switch({"2": SwitchPosition.TURNED})
shunting_Se1_S2.add_switch({"4": SwitchPosition.STRAIGHT})
shunting_Se1_S2.add_track("2")
re_paths.add_path(shunting_Se1_S2)

shunting_S2_Se1 = Path("S2", "Se1", shunt_path=True)
shunting_S2_Se1.add_switch({"2": SwitchPosition.TURNED})
shunting_S2_Se1.add_switch({"1_3": SwitchPosition.Z_DOWN_STRAIGHT})
shunting_S2_Se1.add_switch({"4": SwitchPosition.STRAIGHT})
shunting_S2_Se1.add_track("1L")
re_paths.add_path(shunting_S2_Se1)

shunting_Se1_S3 = Path("Se1", "S3", shunt_path=True)
shunting_Se1_S3.add_switch({"1_3": SwitchPosition.TURNED})
shunting_Se1_S3.add_switch({"5": SwitchPosition.STRAIGHT})
shunting_Se1_S3.add_track("3")
re_paths.add_path(shunting_Se1_S3)

shunting_S3_Se1 = Path("S3", "Se1", shunt_path=True)
shunting_S3_Se1.add_switch({"5": SwitchPosition.STRAIGHT})
shunting_S3_Se1.add_switch({"1_3": SwitchPosition.TURNED})
shunting_S3_Se1.add_track("1L")
re_paths.add_path(shunting_S3_Se1)

shunting_Se1_Se3 = Path("Se1", "Se3", shunt_path=True)
shunting_Se1_Se3.add_switch({"1_3": SwitchPosition.Z_DOWN_STRAIGHT})
shunting_Se1_Se3.add_switch({"2": SwitchPosition.TURNED})
shunting_Se1_Se3.add_switch({"4": SwitchPosition.TURNED})
shunting_Se1_Se3.add_track("4")
re_paths.add_path(shunting_Se1_Se3)

shunting_Se3_Se1 = Path("Se3", "Se1", shunt_path=True)
shunting_Se3_Se1.add_switch({"4": SwitchPosition.TURNED})
shunting_Se3_Se1.add_switch({"2": SwitchPosition.TURNED})
shunting_Se3_Se1.add_switch({"1_3": SwitchPosition.Z_DOWN_STRAIGHT})
shunting_Se3_Se1.add_track("1L")
re_paths.add_path(shunting_Se3_Se1)

shunting_Se1_S5 = Path("Se1", "S5", shunt_path=True)
shunting_Se1_S5.add_switch({"1_3": SwitchPosition.TURNED})
shunting_Se1_S5.add_switch({"5": SwitchPosition.TURNED})
shunting_Se1_S5.add_track("5")
re_paths.add_path(shunting_Se1_S5)

shunting_S5_Se1 = Path("S5", "Se1", shunt_path=True)
shunting_S5_Se1.add_switch({"5": SwitchPosition.TURNED})
shunting_S5_Se1.add_switch({"1_3": SwitchPosition.TURNED})
shunting_S5_Se1.add_track("1L")
re_paths.add_path(shunting_S5_Se1)

shunting_Se2_S3 = Path("Se2", "S3", shunt_path=True)
shunting_Se2_S3.add_switch({"1_3": SwitchPosition.Z_UP_STRAIGHT})
shunting_Se2_S3.add_switch({"5": SwitchPosition.STRAIGHT})
shunting_Se2_S3.add_track("3")
re_paths.add_path(shunting_Se2_S3)

shunting_S3_Se2 = Path("S3", "Se2", shunt_path=True)
shunting_S3_Se2.add_switch({"5": SwitchPosition.STRAIGHT})
shunting_S3_Se2.add_switch({"1_3": SwitchPosition.Z_UP_STRAIGHT})
shunting_S3_Se2.add_track("2L")
re_paths.add_path(shunting_S3_Se2)

shunting_Se2_S5 = Path("Se2", "S5", shunt_path=True)
shunting_Se2_S5.add_switch({"1_3": SwitchPosition.Z_UP_STRAIGHT})
shunting_Se2_S5.add_switch({"5": SwitchPosition.TURNED})
shunting_Se2_S5.add_track("5")
re_paths.add_path(shunting_Se2_S5)

shunting_S5_Se2 = Path("S5", "Se2", shunt_path=True)
shunting_S5_Se2.add_switch({"5": SwitchPosition.TURNED})
shunting_S5_Se2.add_switch({"1_3": SwitchPosition.Z_UP_STRAIGHT})
shunting_S5_Se2.add_track("2L")
re_paths.add_path(shunting_S5_Se2)
