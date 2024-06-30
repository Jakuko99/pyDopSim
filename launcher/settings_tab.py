from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QComboBox, QCheckBox


class SettingsTab(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.allow_1L_checkbox = QCheckBox("Povoliť koľaj 1L v teste stanice", self)
        self.allow_1L_checkbox.setChecked(True)
        self.allow_1L_checkbox.move(5, 5)

        self.allow_2L_checkbox = QCheckBox("Povoliť koľaj 2L v teste stanice", self)
        self.allow_2L_checkbox.setChecked(True)
        self.allow_2L_checkbox.move(5, 25)

        self.allow_S_checkbox = QCheckBox("Povoliť koľaj S v teste stanice", self)
        self.allow_S_checkbox.setChecked(True)
        self.allow_S_checkbox.move(5, 45)
