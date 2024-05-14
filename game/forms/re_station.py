from PyQt5.QtWidgets import (
    QMainWindow,
    QLabel,
)
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
    AbstractStationButton,
)
from game.forms.station_platforms import StationPlatforms
from game.data_types.api_package import (
    SignalSign,
    TrackState,
    SwitchType,
    IndicatorState,
    LeverState,
    IndicatorColor,
    ButtonType,
)


class REStation(QMainWindow):
    def __init__(self, station_name: str):
        super().__init__()
        self.setGeometry(0, 0, 1100, 780)
        self.setWindowTitle("Station test window")
        self.setFixedSize(1100, 780)
        self.font_obj = QFont("Arial", 20)
        self.station_platforms = StationPlatforms(station_name=station_name)

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

        self.path_build = AbstractIndicatorSlim(
            indicator_color=IndicatorColor.RED, parent=self
        )
        self.path_build.move(397, 187)

        self.path_build_cancel = AbstractButton(
            parent=self, button_type=ButtonType.NORMAL
        )
        self.path_build_cancel.move(468, 184)

        self.check_switch_positions = AbstractButton(ButtonType.NORMAL, self)
        self.check_switch_positions.move(540, 184)

        self.check_track_segments = AbstractButton(ButtonType.NORMAL, self)
        self.check_track_segments.move(615, 184)

        self.switch_cut_L = AbstractIndicatorSlim(IndicatorColor.RED, self)
        self.switch_cut_L.move(97, 284)

        self.switch_cut_S = AbstractIndicatorSlim(IndicatorColor.RED, self)
        self.switch_cut_S.move(970, 284)

        self.announce_disable_L = AbstractButton(ButtonType.NORMAL, self)
        self.announce_disable_L.move(24, 200)

        self.announce_disable_S = AbstractButton(ButtonType.NORMAL, self)
        self.announce_disable_S.move(1038, 200)

        self.switch_cut_disable_L = AbstractButton(ButtonType.NORMAL, self)
        self.switch_cut_disable_L.move(24, 280)

        self.switch_cut_disable_S = AbstractButton(ButtonType.NORMAL, self)
        self.switch_cut_disable_S.move(1038, 280)

        self.time_5s = AbstractIndicatorSlim(IndicatorColor.RED, self)
        self.time_5s.move(545, 110)

        self.time_1min = AbstractIndicatorSlim(IndicatorColor.RED, self)
        self.time_1min.move(617, 110)

        self.time_3min = AbstractIndicatorSlim(IndicatorColor.RED, self)
        self.time_3min.move(688, 110)

        self.train_nr = AbstractIndicatorSlim(IndicatorColor.WHITE, self)
        self.train_nr.move(688, 188)
        self.train_nr.set_state(IndicatorState.ON)

        self.switch_1_3 = AbstractLeverSlim(self)
        self.switch_1_3.move(12, 35)

        self.switch_2 = AbstractLeverSlim(self)
        self.switch_2.move(82, 35)

        self.switch_4_vk2 = AbstractLeverSlim(self)
        self.switch_4_vk2.move(152, 35)

        self.switch_5 = AbstractLeverSlim(self)
        self.switch_5.move(225, 35)

        self.vk_1 = AbstractLeverSlim(self)
        self.vk_1.move(295, 35)

        self.switch_6_7 = AbstractLeverSlim(self)
        self.switch_6_7.move(814, 35)

        self.switch_8 = AbstractLeverSlim(self)
        self.switch_8.move(885, 35)

        self.switch_9 = AbstractLeverSlim(self)
        self.switch_9.move(955, 35)

        self.switch_10 = AbstractLeverSlim(self)
        self.switch_10.move(1027, 35)

        self.station_button = AbstractStationButton(self)
        self.station_button.move(476, 632)
        self.station_button.setFunctions(lambda: self.station_platforms.show())
