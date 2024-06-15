from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QComboBox


class SettingsTab(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
