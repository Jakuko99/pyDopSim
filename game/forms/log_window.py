import logging
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QMenu, QAction, QFileDialog
from PyQt5.QtGui import QFont, QColor, QIcon
from PyQt5.QtCore import QTimer
from queue import Queue, Empty


class LogWindow(QMainWindow):
    def __init__(self, parent=None, queue: Queue = None):
        super().__init__(parent)
        self.logger = logging.getLogger("Game.LogWindow")
        self.logger.setLevel(logging.DEBUG)
        self.logger.info("Log window started")

        self.setWindowIcon(QIcon("assets/log_icon.png"))
        self.setWindowTitle("Log Window")
        self.setGeometry(0, 0, 500, 300)
        if queue:
            self.log_pipe = queue
        else:
            self.log_pipe = Queue()  # create empty queue if not provided

        self.context_menu = QMenu(self)
        self.save_log_action = QAction("Uložiť log", self)
        self.save_log_action.triggered.connect(self.save_log)
        self.save_log_action.setIcon(QIcon("assets/save_icon.png"))
        self.context_menu.addAction(self.save_log_action)

        self.log_area = QTextEdit(self)
        self.log_area.setReadOnly(True)
        self.log_area.setStyleSheet("background-color: black")
        self.log_area.setFont(QFont("Consolas", 10))
        self.log_area.contextMenuEvent = self.show_context_menu
        self.log_timer = QTimer(self)
        self.log_timer.timeout.connect(self.update_log)
        self.log_timer.start(50)

    def resizeEvent(self, event):
        self.log_area.setGeometry(0, 0, self.width(), self.height())

    def show_context_menu(self, event):
        self.context_menu.exec_(event.globalPos())

    def save_log(self):
        filename = QFileDialog.getSaveFileName(
            self, "Uložiť log", filter="Log files (*.log)"
        )
        if not filename[0] == "":
            with open(filename[0], "w") as f:
                f.write(self.log_area.toPlainText())

    def update_log(self):
        try:
            log_data: dict = self.log_pipe.get(block=False)
        except Empty:
            pass
        else:
            self.log_area.setTextColor(QColor(255, 255, 255))
            self.log_area.setTextBackgroundColor(QColor(0, 0, 0))
            if log_data.get("log", None):  # log text color based on level
                if log_data["level"] == "WARNING":
                    self.log_area.setTextColor(QColor(255, 165, 0))
                elif log_data["level"] == "ERROR":
                    self.log_area.setTextColor(QColor(255, 0, 0))
                elif log_data["level"] == "CRITICAL":
                    self.log_area.setTextColor(QColor(255, 255, 255))
                    self.log_area.setTextBackgroundColor(QColor(255, 0, 0))
                elif log_data["level"] == "DEBUG":
                    self.log_area.setTextColor(QColor(192, 192, 192))
                self.log_area.append(log_data["log"])
