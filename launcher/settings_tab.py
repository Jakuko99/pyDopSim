from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QComboBox, QCheckBox


class SettingsTab(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.allow_2L_checkbox = QCheckBox("Povoliť 2L v teste stanice", self)
        self.allow_2L_checkbox.setChecked(True)
        self.allow_2L_checkbox.move(5, 5)
