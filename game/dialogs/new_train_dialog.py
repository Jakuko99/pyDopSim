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
)
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt
import os

from game.data_types.api_package import TrainType
from game.objects.api_package import Locomotive, Carriage, Consist


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
    def __init__(self, parent):
        super().__init__(parent)
        self.font_obj = QFont("Arial", 10)
        self.setWindowTitle("Vytvoriť nový vlak")
        self.setFixedSize(630, 400)

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

        self.train_type_label = QLabel("Typ vlaku:", self)
        self.train_type_label.setFont(self.font_obj)
        self.train_type_label.move(165, 8)

        self.train_type_combo = QComboBox(self)
        self.train_type_combo.setFont(self.font_obj)
        self.train_type_combo.addItems([v.name for v in TrainType])
        self.train_type_combo.move(240, 5)
        self.train_type_combo.setFixedSize(75, 25)

        self.add_loco_button = QPushButton("Pridať lokomotívu", self)
        self.add_loco_button.move(165, 60)
        self.add_loco_button.setFixedSize(100, 25)
        self.add_loco_button.clicked.connect(
            self.add_locomotive
        )  # dynammic adding is not working

        self.add_carriage_button = QPushButton("Pridať vozeň", self)
        self.add_carriage_button.move(165, 95)
        self.add_carriage_button.setFixedSize(100, 25)
        self.add_carriage_button.clicked.connect(self.add_carriage)

        self.consist_list = QListWidget(self)
        self.consist_list.setFont(self.font_obj)
        self.consist_list.setFixedSize(150, 300)
        self.consist_list.move(475, 28)

        self.remove_one_button = QPushButton("Odstrániť položku", self)
        self.remove_one_button.move(360, 60)
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

    def on_train_selected(self, item):
        pixmap = QPixmap(f"assets/vozidla/{item.text()}.bmp")
        if pixmap.width() > 300:  # fit to width
            pixmap = pixmap.scaledToWidth(300)
        self.train_preview.setPixmap(pixmap)

    def search_function(self):
        search_text = self.search_field.text()
        self.train_list.clear()
        self.train_list.addItems([v for v in self.train_assets if search_text in v])

    def add_locomotive(self):
        self.consist_list.addItem(self.train_list.currentItem().text())
        loco = Locomotive(self.train_list.currentItem().text())
        self.consist.add_locomotive(loco)

    def add_carriage(self):
        self.consist_list.addItem(self.train_list.currentItem().text())
        carriage = Carriage(self.train_list.currentItem().text())
        self.consist.add_carriage(carriage)

    def show_consist_preview(self):
        self.preview = ConsistPreview(self.consist, self)
        self.preview.show()

    def remove_all(self):
        self.consist_list.clear()
        self.consist = Consist()


if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    ex = NewTrainDialog(None)
    ex.show()
    sys.exit(app.exec_())
