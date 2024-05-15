from PyQt5.QtWidgets import QMenu, QAction, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from uuid import UUID, uuid4
import os


class Carriage(QWidget):
    def __init__(self, carriage_asset: str, parent=None):
        super().__init__(parent=parent)
        self.uuid: UUID = uuid4()
        self.setMinimumSize(5, 45)

        if os.path.exists(f"assets/vozidla/{carriage_asset}.bmp"):
            self.carriage_body = QLabel(self)
            self.carriage_asset: QPixmap = QPixmap(
                f"assets/vozidla/{carriage_asset}.bmp"
            )
            self.carriage_body.setPixmap(self.carriage_asset)
            self.carriage_body.move(0, 0)
        else:
            raise FileNotFoundError(f"Train asset {carriage_asset} not found")

        self.setGeometry(0, 0, self.carriage_asset.width(), 45)
