from PyQt5.QtWidgets import QMainWindow, QLabel, QMessageBox
from PyQt5.QtGui import QFont, QIcon


class DispatcherGUI(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Dispečerské okno")
        self.setWindowIcon(QIcon("assets/app_icon.png"))
        self.setFont(QFont("Arial", 11))
