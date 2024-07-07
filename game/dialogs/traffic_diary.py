from PyQt5.QtWidgets import QMainWindow, QLabel, QMessageBox
from PyQt5.QtGui import QFont, QIcon


class TrafficDiary(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Dopravný deník")
        self.setWindowIcon(QIcon("assets/app_icon.png"))
        self.setFont(QFont("Arial", 11))
