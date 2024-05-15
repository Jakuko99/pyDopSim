import os
from PyQt5.QtWidgets import (
    QLabel,
    QPushButton,
    QComboBox,
    QLineEdit,
    QMessageBox,
    QDialog,
    QComboBox,
    QListWidget,
)
from PyQt5.QtGui import QPixmap, QFont
import os

from game.data_types.api_package import TrainType
from game.objects.api_package import Locomotive, Carriage, Consist


class NewTrainDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.font_obj = QFont("Arial", 10)
        self.setWindowTitle("Vytvoriť nový vlak")
        self.consist.move(0, 335)

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

        self.train_type_combo = QComboBox(self)
        self.train_type_combo.setFont(self.font_obj)
        self.train_type_combo.addItems([v.name for v in TrainType])
        self.train_type_combo.move(165, 0)
        self.train_type_combo.setFixedSize(75, 25)

        self.add_loco_button = QPushButton("Pridať lokomotívu", self)
        self.add_loco_button.move(165, 60)
        self.add_loco_button.clicked.connect(
            lambda: self.consist.add_locomotive(
                Locomotive(self.train_list.currentItem().text())
            )
        )  # dynammic adding is not working

        self.add_carriage_button = QPushButton("Pridať vozeň", self)
        self.add_carriage_button.move(165, 90)
        self.add_carriage_button.clicked.connect(
            lambda: self.consist.add_carriage(
                Carriage(self.train_list.currentItem().text())
            )
        )

    def on_train_selected(self, item):
        pixmap = QPixmap(f"assets/vozidla/{item.text()}.bmp")
        if pixmap.width() > 300:  # fit to width
            pixmap = pixmap.scaledToWidth(300)
        self.train_preview.setPixmap(pixmap)

    def search_function(self):
        search_text = self.search_field.text()
        self.train_list.clear()
        self.train_list.addItems([v for v in self.train_assets if search_text in v])


if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    ex = NewTrainDialog(None)
    ex.show()
    sys.exit(app.exec_())
