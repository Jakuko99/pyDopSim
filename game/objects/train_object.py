from PyQt5.QtWidgets import QMenu, QAction, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from uuid import UUID, uuid4
import os

from game.data_types.exceptions import AssetNotFound


class TrainObject(QWidget):
    def __init__(self, train_asset: str, parent=None):
        super().__init__(parent=parent)
        self.uuid: UUID = uuid4()
        self.setMinimumSize(5, 45)
        self.movable: bool = False

        if os.path.exists(f"assets/vozidla/{train_asset}.bmp"):
            self.train_body = QLabel(self)
            self.train_asset_name: str = train_asset
            self.train_asset: QPixmap = QPixmap(f"assets/vozidla/{train_asset}.bmp")
            self.train_body.setPixmap(self.train_asset)
            self.train_body.move(0, 0)

            if (
                self.train_asset_name.startswith("1")
                or self.train_asset_name.startswith("2")
                or self.train_asset_name.startswith("3")
                or self.train_asset_name.startswith("4")
                or self.train_asset_name.startswith("5")
                or self.train_asset_name.startswith("6")
                or self.train_asset_name.startswith("7")
                or self.train_asset_name.startswith("8")
            ):
                self.movable = True
        else:
            raise AssetNotFound(f"Súbor pre vozidlo {train_asset} nebol nájdený.")

        self.setFixedSize(self.train_asset.width(), 45)
