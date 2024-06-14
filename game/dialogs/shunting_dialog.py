import os
from PyQt5.QtWidgets import (
    QLabel,
    QPushButton,
    QComboBox,
    QMessageBox,
    QMainWindow,
    QComboBox,
    QCheckBox,
)
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtCore import Qt, QTimer
import os

from game.data_types.api_package import Tracks


class ShuntingDialog(QMainWindow):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.font_obj = QFont("Arial", 10)
        self.bigger_font_obj = QFont("Arial", 16)
        self.setWindowTitle("Posun súpravy")
        self.setWindowIcon(QIcon("assets/shunting_icon.png"))
        self._parent = parent
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.move_func)
        self.move_increment: int = 0
        self.setFixedSize(400, 300)

        self.loco_label = QLabel("Lokomotívy:", self)
        self.loco_label.setFont(self.font_obj)
        self.loco_label.setStyleSheet("font-weight: bold;")
        self.loco_label.move(5, 0)

        self.loco_list = QComboBox(self)
        self.loco_list.setFixedSize(250, 25)
        self.loco_list.setFont(self.font_obj)
        self.loco_list.setCurrentIndex(-1)
        self.loco_list.move(5, 25)

        self.cars_label = QLabel("Vozne:", self)
        self.cars_label.setFont(self.font_obj)
        self.cars_label.setStyleSheet("font-weight: bold;")
        self.cars_label.move(5, 70)

        self.cars_list = QComboBox(self)
        self.cars_list.setFixedSize(250, 25)
        self.cars_list.setFont(self.font_obj)
        self.cars_list.setCurrentIndex(-1)
        self.cars_list.move(5, 95)

        self.uncouple_loco_button_right = QPushButton("Odpojiť zprava", self)
        self.uncouple_loco_button_right.setFixedSize(100, 25)
        self.uncouple_loco_button_right.move(265, 10)

        self.uncouple_loco_button_left = QPushButton("Odpojiť zľava", self)
        self.uncouple_loco_button_left.setFixedSize(100, 25)
        self.uncouple_loco_button_left.move(265, 35)

        self.uncouple_car_button_right = QPushButton("Odpojiť zprava", self)
        self.uncouple_car_button_right.setFixedSize(100, 25)
        self.uncouple_car_button_right.move(265, 80)

        self.uncouple_car_button_left = QPushButton("Odpojiť zľava", self)
        self.uncouple_car_button_left.setFixedSize(100, 25)
        self.uncouple_car_button_left.move(265, 105)

        self.move_left_button = QPushButton("🡄", self)
        self.move_left_button.setFont(self.bigger_font_obj)
        self.move_left_button.setFixedSize(30, 30)
        self.move_left_button.move(5, 140)
        self.move_left_button.clicked.connect(self.move_left)

        self.move_stop_button = QPushButton("▬", self)
        self.move_stop_button.setFont(self.bigger_font_obj)
        self.move_stop_button.setFixedSize(30, 30)
        self.move_stop_button.move(40, 140)
        self.move_stop_button.clicked.connect(self.move_stop)

        self.move_right_button = QPushButton("🡆", self)
        self.move_right_button.setFont(self.bigger_font_obj)
        self.move_right_button.setFixedSize(30, 30)
        self.move_right_button.move(75, 140)
        self.move_right_button.clicked.connect(self.move_right)

    def populate_dialog(self):
        if self._parent.locomotives:
            self.loco_list.setEnabled(True)
            self.uncouple_loco_button_left.setEnabled(True)
            self.uncouple_loco_button_right.setEnabled(True)
            self.loco_list.addItems(
                [
                    f"{loco.train_asset_name} ({loco.uuid})"
                    for loco in self._parent.locomotives
                ]
            )
        else:
            self.loco_list.setEnabled(False)
            self.uncouple_loco_button_left.setEnabled(False)
            self.uncouple_loco_button_right.setEnabled(False)

        if self._parent.carriages:
            self.cars_list.setEnabled(True)
            self.uncouple_car_button_left.setEnabled(True)
            self.uncouple_car_button_right.setEnabled(True)
            self.cars_list.addItems(
                [
                    f"{car.train_asset_name} ({car.uuid})"
                    for car in self._parent.carriages
                ]
            )
        else:
            self.cars_list.setEnabled(False)
            self.uncouple_car_button_left.setEnabled(False)
            self.uncouple_car_button_right.setEnabled(False)

    def move_left(self):
        self.move_increment = -2
        self.timer.start(20)

    def move_stop(self):
        self.timer.stop()

    def move_right(self):
        self.move_increment = 2
        self.timer.start(20)

    def move_func(self):  # TODO: conditions if train can move
        self._parent.move(self._parent.x() + self.move_increment, self._parent.y())
