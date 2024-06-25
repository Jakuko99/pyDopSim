import os
from PyQt5.QtWidgets import (
    QLabel,
    QPushButton,
    QComboBox,
    QLineEdit,
    QMessageBox,
    QMainWindow,
    QComboBox,
    QDialog,
)
from PyQt5.QtGui import QFont, QIcon, QIntValidator
from PyQt5.QtCore import Qt
import os

from game.data_types.api_package import TrainType


class TrainNumberDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.font_obj = QFont("Arial", 10)
        self.setWindowTitle("Zaviest nový vlak")
        self.setWindowIcon(QIcon("assets/new_train_icon.png"))
        self.setFixedSize(280, 75)

        self.train_type_label = QLabel("Typ vlaku:", self)
        self.train_type_label.setFont(self.font_obj)
        self.train_type_label.move(5, 10)

        self.train_type_combo = QComboBox(self)
        self.train_type_combo.setFont(self.font_obj)
        self.train_type_combo.addItems([v.name for v in TrainType])
        self.train_type_combo.move(95, 10)
        self.train_type_combo.setFixedSize(75, 25)
        self.train_type_combo.setCurrentIndex(-1)

        self.train_nr_label = QLabel("Číslo vlaku:", self)
        self.train_nr_label.setFont(self.font_obj)
        self.train_nr_label.move(5, 45)

        self.train_nr_field = QLineEdit(self)
        self.train_nr_field.setFixedSize(75, 25)
        self.train_nr_field.setValidator(QIntValidator(0, 99999))
        self.train_nr_field.move(95, 45)

        self.cancel_button = QPushButton("Zrušiť", self)
        self.cancel_button.setFont(self.font_obj)
        self.cancel_button.move(180, 45)
        self.cancel_button.clicked.connect(self.close)

        self.confirm_button = QPushButton("Potvrdiť", self)
        self.confirm_button.setFont(self.font_obj)
        self.confirm_button.move(180, 10)
        self.confirm_button.clicked.connect(self.assign_number)

    def assign_number(self):
        if (
            self.train_nr_field.text() == ""
            or self.train_type_combo.currentText() == ""
        ):
            QMessageBox.warning(
                self, "Chyba", "Čislo alebo typ vlaku chýba!", QMessageBox.Ok
            )
        else:
            pass  # TODO: add method for assigning number
