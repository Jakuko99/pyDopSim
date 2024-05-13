from PyQt5.QtWidgets import (
    QMainWindow,
    QLabel,
    QPushButton,
    QComboBox,
    QLineEdit,
    QMessageBox,
    QMenu,
    QAction,
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
)
from game.dialogs.api_package import ConnectDialog
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
        self.setGeometry(0, 0, 1100, 800)
        self.setWindowTitle("Station test window")
        self.setFixedSize(1100, 800)
        self.font_obj = QFont("Arial", 20)

        # ----- menu items -----
        self.menu_bar = self.menuBar()
        self.client_menu = self.menu_bar.addMenu("Klient")
        self.refresh_action = QAction("Obnoviť", self)
        self.client_menu.addAction(self.refresh_action)

        exit_action = QAction("Ukončiť", self)
        exit_action.triggered.connect(self.close)
        self.client_menu.addAction(exit_action)

        self.server_menu = self.menu_bar.addMenu("Server")
        self.connect_action = QAction("Pripojiť", self)
        self.connect_action.triggered.connect(
            lambda: ConnectDialog(self).exec_()
        )  # TODO: pass values back to window
        self.server_menu.addAction(self.connect_action)

        self.disconnect_action = QAction("Odpojiť", self)
        self.server_menu.addAction(self.disconnect_action)
        self.disconnect_action.setEnabled(False)

        self.help_menu = self.menu_bar.addMenu("Pomoc")
        self.about_action = QAction("O programe", self)
        self.help_menu.addAction(self.about_action)

        self.background = QLabel(self)
        self.background.setPixmap(QPixmap("assets/reliefRE_uzol.bmp"))
        self.background.setScaledContents(True)
        self.background.setGeometry(0, 20, 1100, 780)

        self.title = QLabel(station_name, self)
        self.title.move(372, 37)
        self.title.setAlignment(Qt.AlignCenter)
        self.font_obj.setBold(True)
        self.title.setFixedSize(356, 55)
        self.title.setFont(self.font_obj)

        self.path_build = AbstractIndicatorSlim(
            indicator_color=IndicatorColor.RED, parent=self
        )
        self.path_build.move(397, 207)

        self.path_build_cancel = AbstractButton(
            parent=self, button_type=ButtonType.NORMAL
        )
        self.path_build_cancel.move(468, 204)

        self.check_switch_positions = AbstractButton(ButtonType.NORMAL, self)
        self.check_switch_positions.move(540, 204)

        self.check_track_segments = AbstractButton(ButtonType.NORMAL, self)
        self.check_track_segments.move(615, 204)

        self.switch_cut_L = AbstractIndicatorSlim(IndicatorColor.RED, self)
        self.switch_cut_L.move(97, 304)

        self.switch_cut_S = AbstractIndicatorSlim(IndicatorColor.RED, self)
        self.switch_cut_S.move(970, 304)

        self.announce_disable_L = AbstractButton(ButtonType.NORMAL, self)
        self.announce_disable_L.move(24, 220)

        self.announce_disable_S = AbstractButton(ButtonType.NORMAL, self)
        self.announce_disable_S.move(1038, 220)

        self.switch_cut_disable_L = AbstractButton(ButtonType.NORMAL, self)
        self.switch_cut_disable_L.move(24, 300)

        self.switch_cut_disable_S = AbstractButton(ButtonType.NORMAL, self)
        self.switch_cut_disable_S.move(1038, 300)

        self.time_5s = AbstractIndicatorSlim(IndicatorColor.RED, self)
        self.time_5s.move(545, 130)

        self.time_1min = AbstractIndicatorSlim(IndicatorColor.RED, self)
        self.time_1min.move(617, 130)

        self.time_3min = AbstractIndicatorSlim(IndicatorColor.RED, self)
        self.time_3min.move(688, 130)

        self.train_nr = AbstractIndicatorSlim(IndicatorColor.WHITE, self)
        self.train_nr.move(688, 208)
        self.train_nr.set_state(IndicatorState.ON)

        self.switch_1_3 = AbstractLeverSlim(self)
        self.switch_1_3.move(12, 55)

        self.switch_2 = AbstractLeverSlim(self)
        self.switch_2.move(82, 55)

        self.switch_4_vk2 = AbstractLeverSlim(self)
        self.switch_4_vk2.move(152, 55)

        self.switch_5 = AbstractLeverSlim(self)
        self.switch_5.move(225, 55)

        self.vk_1 = AbstractLeverSlim(self)
        self.vk_1.move(295, 55)

        self.switch_6_7 = AbstractLeverSlim(self)
        self.switch_6_7.move(814, 55)

        self.switch_8 = AbstractLeverSlim(self)
        self.switch_8.move(885, 55)

        self.switch_9 = AbstractLeverSlim(self)
        self.switch_9.move(955, 55)

        self.switch_10 = AbstractLeverSlim(self)
        self.switch_10.move(1027, 55)
