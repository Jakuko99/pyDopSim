import os
from PyQt5.QtWidgets import (
    QLabel,
    QPushButton,
    QComboBox,
    QLineEdit,
    QMessageBox,
    QDialog,
    QMainWindow,
    QComboBox,
    QListWidget,
    QScrollArea,
    QCheckBox,
)
from PyQt5.QtGui import QPixmap, QFont, QIntValidator, QIcon
from PyQt5.QtCore import Qt
import os

from game.data_types.api_package import TrainType, Tracks
from game.objects.api_package import TrainObject, Consist


class ConsistPreview(QMainWindow):
    def __init__(self, consist: Consist, parent=None):
        super().__init__(parent)

        self.scroll = QScrollArea()
        self.consist = consist
        consist.setParent(self)

        self.setStyleSheet("background-color: black;")
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.consist)

        self.setCentralWidget(self.scroll)
        self.setWindowTitle("Náhľad súpravy")
        self.setFixedHeight(75)
        self.setGeometry(120, 150, 1000, 75)

        del self.consist  # prevent overwriting local variable


class NewTrainDialog(QDialog):
    def __init__(self, parent, on_confirm):
        super().__init__(parent)
        self.on_confirm = on_confirm
        self.font_obj = QFont("Arial", 10)
        self.setWindowTitle("Vytvoriť nový vlak")
        self.setWindowIcon(QIcon("assets/app_icon.png"))
        self.setFixedSize(630, 365)

        self.consist = Consist()
        self.preview = None

        self.train_assets = [
            v.replace(".bmp", "") for v in os.listdir("assets/vozidla")
        ]
        self.train_assets = [
            v
            for v in self.train_assets
            if not (v.endswith(".png") or v.endswith(".gif"))
        ]

        self.search_field = QLineEdit(self)
        self.search_field.setPlaceholderText("Hľadať vozidlo...")
        self.search_field.setFixedSize(150, 25)
        self.search_field.move(5, 0)
        self.search_field.textChanged.connect(self.search_function)

        self.train_list = QListWidget(self)
        self.train_list.setFont(self.font_obj)
        self.train_list.setFixedSize(150, 300)
        self.train_list.addItems(self.train_assets)
        self.train_list.move(5, 28)
        self.train_list.itemClicked.connect(self.on_train_selected)

        self.train_preview = QLabel(self)
        self.train_preview.setFixedSize(300, 45)
        self.train_preview.setAutoFillBackground(True)
        self.train_preview.move(165, 125)
        self.on_train_selected(self.train_list.item(0))  # auto select first item

        self.add_loco_button = QPushButton("Pridať vozidlo", self)
        self.add_loco_button.move(165, 65)
        self.add_loco_button.setFixedSize(100, 25)
        self.add_loco_button.clicked.connect(
            self.add_vehicle
        )  # dynammic adding is not working

        self.consist_list = QListWidget(self)
        self.consist_list.setFont(self.font_obj)
        self.consist_list.setFixedSize(150, 300)
        self.consist_list.move(475, 28)

        self.remove_one_button = QPushButton("Odstrániť položku", self)
        self.remove_one_button.move(360, 65)
        self.remove_one_button.setFixedSize(110, 25)
        self.remove_one_button.clicked.connect(
            lambda: self.consist_list.takeItem(self.consist_list.currentRow())
        )

        self.remove_all_button = QPushButton("Odstrániť všetko", self)
        self.remove_all_button.move(360, 95)
        self.remove_all_button.setFixedSize(110, 25)
        self.remove_all_button.clicked.connect(self.remove_all)

        self.preview_button = QPushButton("Náhľad súpravy", self)
        self.preview_button.move(5, 335)
        self.preview_button.setFixedSize(150, 25)
        self.preview_button.clicked.connect(self.show_consist_preview)

        self.confirm_button = QPushButton("Pridať súpravu", self)
        self.confirm_button.move(475, 335)
        self.confirm_button.setFixedSize(150, 25)
        self.confirm_button.clicked.connect(self.create_consist)

        self.train_pos_label = QLabel("Koľaj:", self)
        self.train_pos_label.setFont(self.font_obj)
        self.train_pos_label.move(170, 5)

        self.track_pos_combo = QComboBox(self)
        self.track_pos_combo.setFont(self.font_obj)
        self.track_pos_combo.addItems(
            [v.name for v in Tracks if "MANIPULACNA" in v.name]
        )
        self.track_pos_combo.move(240, 5)
        self.track_pos_combo.setFixedSize(175, 25)

        self.track_pos_label1 = QLabel("Pozícia:", self)
        self.track_pos_label1.setFont(self.font_obj)
        self.track_pos_label1.move(170, 35)

        self.track_pos_field = QLineEdit("0", self)
        self.track_pos_field.setFont(self.font_obj)
        self.track_pos_field.setValidator(QIntValidator(0, 5000))  # accept only numbers
        self.track_pos_field.setFixedSize(50, 25)
        self.track_pos_field.move(240, 35)

        self.train_nr_checkbox = QCheckBox("Priradiť číslo vlaku", self)
        self.train_nr_checkbox.setFont(self.font_obj)
        self.train_nr_checkbox.move(165, 190)
        self.train_nr_checkbox.stateChanged.connect(self.change_train_nr)

        self.train_type_label = QLabel("Typ vlaku:", self)
        self.train_type_label.setFont(self.font_obj)
        self.train_type_label.move(165, 215)

        self.train_type_combo = QComboBox(self)
        self.train_type_combo.setFont(self.font_obj)
        self.train_type_combo.addItems([v.name for v in TrainType])
        self.train_type_combo.move(250, 215)
        self.train_type_combo.setFixedSize(75, 25)
        self.train_type_combo.setEnabled(False)

        self.train_nr_label = QLabel("Číslo vlaku:", self)
        self.train_nr_label.setFont(self.font_obj)
        self.train_nr_label.move(165, 245)

        self.train_nr_field = QLineEdit(self)
        self.train_nr_field.setFixedSize(65, 25)
        self.train_nr_field.setValidator(QIntValidator(0, 99999))
        self.train_nr_field.move(250, 245)
        self.train_nr_field.setEnabled(False)

    def on_train_selected(self, item):
        pixmap = QPixmap(f"assets/vozidla/{item.text()}.bmp")
        if pixmap.width() > 300:  # fit to width
            pixmap = pixmap.scaledToWidth(300)
        self.train_preview.setPixmap(pixmap)

    def search_function(self):
        search_text = self.search_field.text().lower()
        self.train_list.clear()
        self.train_list.addItems(
            [v for v in self.train_assets if search_text in v.lower()]
        )  # make search case insensitive

    def add_vehicle(self):
        self.consist_list.addItem(self.train_list.currentItem().text())
        loco = TrainObject(self.train_list.currentItem().text())
        self.consist.add_train_obj(loco)

    def change_train_nr(self):
        if self.train_nr_checkbox.isChecked():
            self.train_nr_field.setEnabled(True)
            self.train_type_combo.setEnabled(True)
        else:
            self.train_nr_field.setEnabled(False)
            self.train_type_combo.setEnabled(False)

    def show_consist_preview(self):
        self.preview = ConsistPreview(self.consist, self)
        self.preview.show()

    def remove_all(self):
        self.consist_list.clear()
        self.consist = Consist()

    def create_consist(self):
        if not self.consist.vehicles_count == 0:
            if self.train_nr_checkbox.isChecked():  # set train number if checked
                self.consist.set_train_number(
                    train_type=TrainType.__getitem__(
                        self.train_type_combo.currentText()
                    ),
                    train_nr=int(self.train_nr_field.text()),
                )
            self.on_confirm(
                self.consist,
                Tracks.__getitem__(self.track_pos_combo.currentText()),
                int(self.track_pos_field.text()),
            )
            self.reset_window()  # reset window after closing
            self.close()
        else:
            QMessageBox.warning(self, "Chyba", "Súprava je prázdna")

    def reset_window(self):
        self.remove_all()
        self.track_pos_combo.setCurrentIndex(0)
        self.track_pos_field.setText("0")
        self.train_nr_checkbox.setChecked(False)
        self.train_nr_field.setText("")
        self.train_type_combo.setCurrentIndex(0)
        self.train_list.setCurrentRow(0)

    def closeEvent(self, event):
        if self.preview:
            self.preview.close()
        event.accept()
