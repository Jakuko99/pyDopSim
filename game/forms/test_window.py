from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton, QComboBox

from game.qt_components.api_package import AbstractSignal
from game.data_types.api_package import SignalSign


class TestWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 800, 600)
        self.setWindowTitle("Component test window")

        self.signal = AbstractSignal(5, self)
        self.signal.move(40, 5)

        self.combo = QComboBox(self)
        self.combo.addItems([item for item in SignalSign.__members__])
        self.combo.move(5, 90)
        self.button = QPushButton("Change Signal", self)
        self.button.move(5, 125)
        self.button.clicked.connect(self.change_signal)

        self.signal1 = AbstractSignal(2, self)
        self.signal1.move(160, 5)

        self.combo1 = QComboBox(self)
        self.combo1.addItems([item for item in SignalSign.__members__])
        self.combo1.move(120, 90)
        self.button1 = QPushButton("Change Signal", self)
        self.button1.move(120, 125)
        self.button1.clicked.connect(self.change_signal1)

        self.signal2 = AbstractSignal(3, self)
        self.signal2.move(280, 5)

        self.combo2 = QComboBox(self)
        self.combo2.addItems([item for item in SignalSign.__members__])
        self.combo2.move(240, 90)
        self.button2 = QPushButton("Change Signal", self)
        self.button2.move(240, 125)
        self.button2.clicked.connect(self.change_signal2)

    def change_signal(self):
        self.signal.set_sign(SignalSign[self.combo.currentText()])

    def change_signal1(self):
        self.signal1.set_sign(SignalSign[self.combo1.currentText()])

    def change_signal2(self):
        self.signal2.set_sign(SignalSign[self.combo2.currentText()])
