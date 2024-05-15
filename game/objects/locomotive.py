from PyQt5.QtWidgets import QMenu, QAction, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from uuid import UUID, uuid4
import os


class Locomotive(QWidget):
    def __init__(self, train_asset: str, parent=None):
        super().__init__(parent=parent)
        self.uuid: UUID = uuid4()
        self.setMinimumSize(5, 45)

        if os.path.exists(f"assets/vozidla/{train_asset}.bmp"):
            self.train_body = QLabel(self)
            self.train_asset: QPixmap = QPixmap(f"assets/vozidla/{train_asset}.bmp")
            self.train_body.setPixmap(self.train_asset)
            self.train_body.move(0, 0)
        else:
            raise FileNotFoundError(f"Locomotive asset {train_asset} not found")

        self.setFixedSize(self.train_asset.width(), 45)
