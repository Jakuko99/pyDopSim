from PyQt5.QtWidgets import (
    QMainWindow,
    QLabel,
)
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtCore import Qt
from queue import Queue
import ctypes
import logging

from game.qt_components.api_package import (
    AbstractTrack,
    AbstractSwitch,
    AbstractTrackSignal,
    AbstractIndicator,
    AbstractLeverSlim,
    AbstractIndicatorSlim,
    AbstractButton,
    AbstractStationButton,
    AbstractClock,
    AbstractTrackButton,
)
from game.forms.station_platforms import StationPlatforms
from game.data_types.api_package import (
    SignalSign,
    TrackState,
    SignalType,
    SwitchType,
    IndicatorState,
    LeverState,
    IndicatorColor,
    ButtonType,
)
from utils.api_package import queue_handler

myappid = f"Jakub.PyDopSim.beta"
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


class REStation(QMainWindow):
    def __init__(self, station_name: str, log_pipe: Queue = None):
        super().__init__()
        self.setGeometry(0, 0, 1100, 780)
        self.setWindowTitle(f"PyDopSim: RE - {station_name}")
        self.setWindowIcon(QIcon("assets/app_icon.png"))
        self.setFixedSize(1100, 780)
        self.font_obj = QFont("Arial", 20)
        if log_pipe:
            self.log_pipe: Queue = log_pipe
        else:
            self.log_pipe = queue_handler.get_logging_pipe()

        self.logger = logging.getLogger("App.REStation")
        self.logger.setLevel(logging.DEBUG)
        self.logger.info("REStation initialized")
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

        self.switch_1_3_controller = AbstractLeverSlim(self)
        self.switch_1_3_controller.move(12, 35)

        self.switch_2_controller = AbstractLeverSlim(self)
        self.switch_2_controller.move(82, 35)

        self.switch_4_vk2_controller = AbstractLeverSlim(self)
        self.switch_4_vk2_controller.move(152, 35)

        self.switch_5_controller = AbstractLeverSlim(self)
        self.switch_5_controller.move(225, 35)

        self.switch_6_7_controller = AbstractLeverSlim(self)
        self.switch_6_7_controller.move(814, 35)

        self.switch_8_controller = AbstractLeverSlim(self)
        self.switch_8_controller.move(885, 35)

        self.switch_9_controller = AbstractLeverSlim(self)
        self.switch_9_controller.move(955, 35)

        self.switch_10_controller = AbstractLeverSlim(self)
        self.switch_10_controller.move(1027, 35)

        self.station_button = AbstractStationButton(parent=self, log_pipe=self.log_pipe)
        self.station_button.move(476, 632)
        self.station_button.setFunctions(
            lambda: (
                self.station_platforms.show()
                if not self.station_platforms.isVisible()
                else self.station_platforms.raise_()
            )
        )  # bring window forward if already open

        self.clock = AbstractClock(parent=self)
        self.clock.setFixedSize(400, 100)
        self.clock.move(465, 705)

        self.track_1 = AbstractTrack(track_segments=2, parent=self)
        self.track_1.move(420, 413)

        self.track_2 = AbstractTrack(track_segments=2, parent=self)
        self.track_2.move(420, 491)

        self.track_3 = AbstractTrack(track_segments=2, parent=self)
        self.track_3.move(420, 335)

        self.track_4 = AbstractTrack(track_segments=2, parent=self, shunt_track=True)
        self.track_4.move(420, 568)

        self.track_4a = AbstractTrack(
            track_segments=1, parent=self, shunt_track=True, no_buttons=True
        )
        self.track_4a.move(819, 586)

        self.track_5 = AbstractTrack(track_segments=2, parent=self)
        self.track_5.move(420, 257)

        self.switch_1_3 = AbstractSwitch(switch_type=SwitchType.Z_TYPE, parent=self)
        self.switch_1_3.move(256, 352)

        self.switch_5 = AbstractSwitch(switch_type=SwitchType.UP_45_RIGHT, parent=self)
        self.switch_5.move(354, 292)

        self.switch_2 = AbstractSwitch(
            switch_type=SwitchType.DOWN_45_RIGHT, parent=self
        )
        self.switch_2.move(306, 452)

        self.switch_4 = AbstractSwitch(
            switch_type=SwitchType.DOWN_45_RIGHT, parent=self
        )
        self.switch_4.move(349, 530)

        self.switch_1_3_track_up = AbstractTrack(2, parent=self, no_buttons=True)
        self.switch_1_3_track_up.move(312, 352)
        self.switch_1_3_track_down = AbstractTrack(2, parent=self, no_buttons=True)
        self.switch_1_3_track_down.move(312, 430)

        self.switch_2.add_associated_track(self.switch_1_3_track_down)
        self.switch_5.add_associated_track(self.switch_1_3_track_up)

        self.switch_4_track = AbstractTrack(1, parent=self, no_buttons=True)
        self.switch_4_track.move(370, 508)
        self.switch_4.add_associated_track(self.switch_4_track)

        self.switch_6_7 = AbstractSwitch(switch_type=SwitchType.Z_TYPE, parent=self)
        self.switch_6_7.move(710, 509)

        self.switch_8 = AbstractSwitch(switch_type=SwitchType.UP_45_LEFT, parent=self)
        self.switch_8.move(751, 293)

        self.switch_8_track = AbstractTrack(1, parent=self, no_buttons=True)
        self.switch_8_track.move(725, 352)
        self.switch_8_track_up = AbstractTrack(1, parent=self, no_buttons=True)
        self.switch_8_track_up.move(710, 274)
        self.switch_8.add_associated_track(self.switch_8_track, self.switch_8_track_up)

        self.switch_9 = AbstractSwitch(switch_type=SwitchType.DOWN_45_LEFT, parent=self)
        self.switch_9.move(752, 452)

        self.switch_9_track = AbstractTrack(1, parent=self, no_buttons=True)
        self.switch_9_track.move(725, 430)
        self.switch_9.add_associated_track(self.switch_9_track)

        self.switch_10 = AbstractSwitch(switch_type=SwitchType.UP_45_LEFT, parent=self)
        self.switch_10.move(791, 368)

        self.switch_10_track = AbstractTrack(1, parent=self, no_buttons=True)
        self.switch_10_track.move(790, 430)
        self.switch_10.add_associated_track(self.switch_10_track)

        self.track_S_button = AbstractTrackButton(
            button_color=IndicatorColor.GREEN, parent=self
        )
        self.track_S_button.move(1005, 421)

        self.track_S_button_shunt = AbstractTrackButton(
            button_color=IndicatorColor.WHITE, parent=self
        )
        self.track_S_button_shunt.move(852, 421)

        self.track_1L_button = AbstractTrackButton(
            button_color=IndicatorColor.GREEN, parent=self
        )
        self.track_1L_button.move(55, 421)

        self.track_1L_button_shunt = AbstractTrackButton(
            button_color=IndicatorColor.WHITE, parent=self
        )
        self.track_1L_button_shunt.move(215, 421)

        self.track_2L_button = AbstractTrackButton(
            button_color=IndicatorColor.GREEN, parent=self
        )
        self.track_2L_button.move(55, 343)

        self.track_2L_button_shunt = AbstractTrackButton(
            button_color=IndicatorColor.WHITE, parent=self
        )
        self.track_2L_button_shunt.move(215, 343)

        self.track_4a_shunt_button = AbstractTrackButton(
            button_color=IndicatorColor.WHITE, parent=self
        )
        self.track_4a_shunt_button.move(780, 577)

        self.signal_2L = AbstractTrackSignal(
            signal_type=SignalType.ENTRY_SIGNAL, parent=self
        )
        self.signal_2L.move(85, 387)

        self.pr_2L_signal = AbstractTrackSignal(
            signal_type=SignalType.EXPECT_SIGNAL, parent=self
        )
        self.pr_2L_signal.move(24, 387)

        self.signal_1L = AbstractTrackSignal(
            signal_type=SignalType.ENTRY_SIGNAL, parent=self
        )
        self.signal_1L.move(85, 465)

        self.pr_1L_signal = AbstractTrackSignal(
            signal_type=SignalType.EXPECT_SIGNAL, parent=self
        )
        self.pr_1L_signal.move(24, 465)

        self.signal_S5 = AbstractTrackSignal(
            signal_type=SignalType.DEPARTURE_SIGNAL, parent=self, flipped=True
        )
        self.signal_S5.move(405, 232)

        self.signal_S3 = AbstractTrackSignal(
            signal_type=SignalType.DEPARTURE_SIGNAL, parent=self, flipped=True
        )
        self.signal_S3.move(405, 310)

        self.signal_S1 = AbstractTrackSignal(
            signal_type=SignalType.DEPARTURE_SIGNAL, parent=self, flipped=True
        )
        self.signal_S1.move(405, 388)

        self.signal_S2 = AbstractTrackSignal(
            signal_type=SignalType.DEPARTURE_SIGNAL, parent=self, flipped=True
        )
        self.signal_S2.move(405, 466)

        self.signal_Se3 = AbstractTrackSignal(
            signal_type=SignalType.SHUNTING_SIGNAL, parent=self, flipped=True
        )
        self.signal_Se3.move(429, 545)

        self.signal_Se1 = AbstractTrackSignal(
            signal_type=SignalType.SHUNTING_SIGNAL, parent=self
        )
        self.signal_Se1.move(232, 465)

        self.signal_Se2 = AbstractTrackSignal(
            signal_type=SignalType.SHUNTING_SIGNAL, parent=self
        )
        self.signal_Se2.move(232, 387)

        self.pr_2L_track = AbstractTrack(1, parent=self, no_buttons=True)
        self.pr_2L_track.move(-1, 352)

        self.pr_1L_track = AbstractTrack(1, parent=self, no_buttons=True)
        self.pr_1L_track.move(-1, 430)

        self.track_2L = AbstractTrack(2, parent=self, no_buttons=True)
        self.track_2L.move(97, 352)

        self.track_1L = AbstractTrack(2, parent=self, no_buttons=True)
        self.track_1L.move(97, 430)

        self.signal_L5 = AbstractTrackSignal(
            signal_type=SignalType.DEPARTURE_SIGNAL, parent=self
        )
        self.signal_L5.move(666, 310)

        self.signal_L3 = AbstractTrackSignal(
            signal_type=SignalType.DEPARTURE_SIGNAL, parent=self
        )
        self.signal_L3.move(666, 388)

        self.signal_L1 = AbstractTrackSignal(
            signal_type=SignalType.DEPARTURE_SIGNAL, parent=self
        )
        self.signal_L1.move(666, 465)

        self.signal_L2 = AbstractTrackSignal(
            signal_type=SignalType.DEPARTURE_SIGNAL, parent=self
        )
        self.signal_L2.move(666, 544)

        self.signal_Se4 = AbstractTrackSignal(
            signal_type=SignalType.SHUNTING_SIGNAL, parent=self
        )
        self.signal_Se4.move(666, 620)

        self.signal_Se5 = AbstractTrackSignal(
            signal_type=SignalType.SHUNTING_SIGNAL, parent=self, flipped=True
        )
        self.signal_Se5.move(763, 543)

        self.signal_Se6 = AbstractTrackSignal(
            signal_type=SignalType.SHUNTING_SIGNAL, parent=self, flipped=True
        )
        self.signal_Se6.move(840, 386)

        self.signal_S = AbstractTrackSignal(
            signal_type=SignalType.ENTRY_SIGNAL, parent=self, flipped=True
        )
        self.signal_S.move(899, 386)

        self.pr_S_signal = AbstractTrackSignal(
            signal_type=SignalType.EXPECT_SIGNAL, parent=self, flipped=True
        )
        self.pr_S_signal.move(1040, 386)

        self.track_S = AbstractTrack(2, parent=self, no_buttons=True)
        self.track_S.move(889, 430)

        self.pr_S_track = AbstractTrack(1, parent=self, no_buttons=True)
        self.pr_S_track.move(1042, 430)

        self.summon_L_button = AbstractButton(ButtonType.NORMAL, self)
        self.summon_L_button.move(286, 684)

        self.summon_S1_S5_button = AbstractButton(ButtonType.NORMAL, self)
        self.summon_S1_S5_button.move(357, 684)

        self.summon_L1_L5_button = AbstractButton(ButtonType.NORMAL, self)
        self.summon_L1_L5_button.move(707, 684)

        self.summon_S_button = AbstractButton(ButtonType.NORMAL, self)
        self.summon_S_button.move(780, 684)

    def stop_blinking(self):
        self.track_1.stop_blinking()
        self.track_2.stop_blinking()
        self.track_3.stop_blinking()
        self.track_4.stop_blinking()
        self.track_5.stop_blinking()
        self.track_S_button.stop_blinking()
        self.track_S_button_shunt.stop_blinking()
        self.track_1L_button.stop_blinking()
        self.track_1L_button_shunt.stop_blinking()
        self.track_2L_button.stop_blinking()
        self.track_2L_button_shunt.stop_blinking()
        self.track_4a_shunt_button.stop_blinking()
