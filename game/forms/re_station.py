from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QComboBox, QLineEdit
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt

from game.qt_components.api_package import (
    AbstractSignal,
    AbstractTrack,
    AbstractSwitch,
    AbstractIndicator,
    AbstractLever,
    AbstractLeverSlim,
    AbstractIndicatorSlim,
    AbstractButton,
)
from game.data_types.api_package import (
    SignalSign,
    TrackState,
    SwitchType,
    IndicatorState,
    LeverState,
    IndicatorColor,
)


class REStation(QMainWindow):
    def __init__(self, station_name: str):
        super().__init__()
        self.setGeometry(0, 0, 1100, 780)
        self.setWindowTitle("Station test window")
        self.setFixedSize(1100, 780)

        self.font_obj = QFont("Arial", 20)

        self.background = QLabel(self)
        self.background.setPixmap(QPixmap("assets/reliefRE_uzol.bmp"))
        self.background.setScaledContents(True)
        self.background.setGeometry(0, 0, 1100, 780)

        self.title = QLabel(station_name, self)
        self.title.move(372, 17)
        self.title.setAlignment(Qt.AlignCenter)
        self.font_obj.setBold(True)
        self.title.setFixedSize(356, 55)
        self.title.setFont(self.font_obj)

        self.path_build = AbstractIndicatorSlim(indicator_color=IndicatorColor.RED, parent=self)
        self.path_build.move(397, 187)

        self.path_build_cancel = AbstractButton(self)
        self.path_build_cancel.setFunctions(
            lambda: print("left click"),
            lambda: print("right click"),
            lambda: print("middle click"),
        )  # refuses to work
        self.path_build_cancel.move(465, 184)

        self.check_switch_positions = AbstractButton(self)
        self.check_switch_positions.move(540, 184)

        self.check_track_segments = AbstractButton(self)
        self.check_track_segments.move(615, 184)

        self.switch_cut_L = AbstractIndicatorSlim(IndicatorColor.RED, self)
        self.switch_cut_L.move(97, 284)

        self.switch_cut_S = AbstractIndicatorSlim(IndicatorColor.RED, self)
        self.switch_cut_S.move(970, 284)

        self.announce_disable_L = AbstractButton(self)
        self.announce_disable_L.move(24, 200)

        self.announce_disable_S = AbstractButton(self)
        self.announce_disable_S.move(1038, 200)

        self.switch_cut_disable_L = AbstractButton(self)
        self.switch_cut_disable_L.move(24, 280)

        self.switch_cut_disable_S = AbstractButton(self)
        self.switch_cut_disable_S.move(1038, 280)

        self.switch_1_3 = AbstractLeverSlim(
            lambda state: self.switch_1_3.set_light(state.value, "lightblue"), self
        )
        self.switch_1_3.move(12, 35)

        self.switch_2 = AbstractLeverSlim(
            lambda state: self.switch_2.set_light(state.value, "lightblue"), self
        )
        self.switch_2.move(82, 35)

        self.switch_4_vk2 = AbstractLeverSlim(
            lambda state: self.switch_4_vk2.set_light(state.value, "lightblue"), self
        )
        self.switch_4_vk2.move(152, 35)

        self.switch_5 = AbstractLeverSlim(
            lambda state: self.switch_5.set_light(state.value, "lightblue"), self
        )
        self.switch_5.move(225, 35)

        self.vk_1 = AbstractLeverSlim(
            lambda state: self.vk_1.set_light(state.value, "lightblue"), self
        )
        self.vk_1.move(295, 35)

        self.switch_6_7 = AbstractLeverSlim(
            lambda state: self.switch_6_7.set_light(state.value, "lightblue"), self
        )
        self.switch_6_7.move(814, 35)

        self.switch_8 = AbstractLeverSlim(
            lambda state: self.switch_8.set_light(state.value, "lightblue"), self
        )
        self.switch_8.move(885, 35)

        self.switch_9 = AbstractLeverSlim(
            lambda state: self.switch_9.set_light(state.value, "lightblue"), self
        )
        self.switch_9.move(955, 35)

        self.switch_10 = AbstractLeverSlim(
            lambda state: self.switch_10.set_light(state.value, "lightblue"), self
        )
        self.switch_10.move(1027, 35)
