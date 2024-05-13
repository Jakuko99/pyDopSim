from PyQt5.QtWidgets import QWidget, QLabel, QScrollArea, QHBoxLayout, QMainWindow
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
import sys


class StationPlatforms(QMainWindow):
    def __init__(self):
        super().__init__()

        self.scroll = QScrollArea()
        self.widget = QWidget()
        self.vbox = QHBoxLayout()

        self.label = QLabel()
        self.label.setPixmap(QPixmap("assets/station_platforms.png"))
        self.vbox.addWidget(self.label)
        self.label.setFixedHeight(500)

        self.widget.setLayout(self.vbox)
        self.widget.move(0, 0)

        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)

        self.setCentralWidget(self.scroll)
        self.setStyleSheet("background-color: #303030;")
        self.setFixedHeight(550)
        self.setWindowTitle("Pohľad do koľajiska")


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = StationPlatforms()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
