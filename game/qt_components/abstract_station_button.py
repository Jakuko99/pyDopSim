from PyQt5.QtWidgets import QWidget, QPushButton, QMenu, QAction
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QIcon
from queue import Queue

from game.forms.log_window import LogWindow
from game.dialogs.debug_dialog import DebugDialog
from utils.api_package import queue_handler


class AbstractStationButton(QWidget):
    def __init__(self, log_pipe: Queue = None, parent=None):
        self._parent = parent
        QWidget.__init__(self, parent=parent)
        if log_pipe:
            self.log_pipe: Queue = log_pipe
        else:
            self.log_pipe = queue_handler.get_logging_pipe()

        self.setGeometry(0, 0, 80, 55)
        self.log_window = LogWindow(self, log_pipe)
        self.right_click_function = lambda: None
        self.middle_click_function = lambda: None
        self.debug: bool = False

        # ----- Context menu -----
        self.context_menu = QMenu(self)
        self.client_info: QAction = QAction("Informácie o klientovi", self)
        self.client_info.setIcon(QIcon("assets/client_icon.png"))
        self.context_menu.addAction(self.client_info)

        self.log_action = QAction("Zobraziť log", self)
        self.log_action.triggered.connect(self.log_window.show)
        self.log_action.setIcon(QIcon("assets/log_icon.png"))
        self.context_menu.addAction(self.log_action)

        self.debug_action = QAction("Debug okno", self)
        self.debug_action.setVisible(False)
        self.debug_action.setIcon(QIcon("assets/debug_icon.png"))
        self.debug_action.triggered.connect(self._debug_action)
        self.context_menu.addAction(self.debug_action)

        self.settings_menu = QMenu(self)
        self.settings_menu.setTitle("Nastavenia")
        self.settings_menu.setIcon(QIcon("assets/settings_icon.png"))
        action = self.settings_menu.addAction("Zvuky simulácie")
        action.setCheckable(True)
        action.setChecked(True)

        action = self.settings_menu.addAction("Zvuky dopravného denníka")
        action.setCheckable(True)
        action.setChecked(True)

        self.settings_menu.addSeparator()
        action = self.settings_menu.addAction("Rozšírené nastavenia")

        self.context_menu.addMenu(self.settings_menu)

        self.button = QPushButton(self)
        icon = QIcon("assets/station_button.png")
        self.button.setIconSize(QSize(80, 55))
        self.button.setIcon(icon)
        self.button.move(0, 0)
        self.button.setFixedSize(80, 55)

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

    def _debug_action(self):
        self.debug_dialog.show()

    def enable_debug(self):
        self.debug = True
        self.debug_dialog = DebugDialog(self._parent)
        self.context_menu.actions()[2].setVisible(True)
