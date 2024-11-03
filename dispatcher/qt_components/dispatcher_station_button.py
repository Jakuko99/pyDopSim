from PyQt5.QtWidgets import QWidget, QPushButton, QMenu, QAction
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon


class DispatcherStationButton(QWidget):
    def __init__(self, parent=None):
        self._parent = parent
        QWidget.__init__(self, parent=parent)

        self.setGeometry(0, 0, 41, 23)
        self.setToolTip("Hlavné menu JOP")
        self.setToolTipDuration(750)
        self.right_click_function = lambda: None
        self.middle_click_function = lambda: None

        # ----- Context menu -----
        self.context_menu = QMenu(self)

        self.take_over_action = QAction("Prevziať obsluhu", self)
        self.context_menu.addAction(self.take_over_action)

        self.new_train_action = QAction("Nový vlak", self)
        self.context_menu.addAction(self.new_train_action)

        self.context_menu.addSeparator()

        self.clear_track_menu = QMenu("Uvoľniť koľaj", self)
        self.context_menu.addMenu(self.clear_track_menu)

        self.clear_track_1_action = QAction("1", self)
        self.clear_track_2_action = QAction("2", self)
        self.clear_track_3_action = QAction("3", self)
        self.clear_track_4_action = QAction("4", self)
        self.clear_track_5_action = QAction("5", self)

        self.clear_track_menu.addActions(
            [
                self.clear_track_5_action,
                self.clear_track_3_action,
                self.clear_track_1_action,
                self.clear_track_2_action,
                self.clear_track_4_action,
            ]
        )

        self.station_master_action = QAction("Návestný majster", self)
        self.context_menu.addAction(self.station_master_action)

        self.message_action = QAction("Správa", self)
        self.context_menu.addAction(self.message_action)

        self.context_menu.addSeparator()

        self.disconnect_action = QAction("Odpojiť", self)
        self.context_menu.addAction(self.disconnect_action)

        self.button = QPushButton(self)
        self.icon = QIcon("assets/jop_station_button_offline.png")
        self.doz_icon = QIcon("assets/jop_station_button.png")
        self.button.setIconSize(QSize(41, 23))
        self.button.setIcon(self.icon)
        self.button.move(0, 0)
        self.button.setFixedSize(41, 23)

    def setFunctions(
        self,
        left_click_function,
        right_click_function=lambda: None,
        middle_click_function=lambda: None,
    ):
        self.button.clicked.connect(left_click_function)
        self.right_click_function = right_click_function
        self.middle_click_function = middle_click_function

    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.RightButton:
            self.right_click_function()
        if QMouseEvent.button() == Qt.MiddleButton:
            self.middle_click_function()

    def contextMenuEvent(self, event):
        self.context_menu.exec_(event.globalPos())

    def go_online(self):
        self.button.setIcon(self.doz_icon)
        self.take_over_action.setText("Odovzdať obsluhu")

    def go_offline(self):
        self.button.setIcon(self.icon)
        self.take_over_action.setText("Prevziať obsluhu")
