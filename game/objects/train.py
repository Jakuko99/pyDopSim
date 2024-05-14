from PyQt5.QtWidgets import QMenu, QAction, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from uuid import UUID, uuid4
import os

from game.objects.carriage import Carriage


class Train(QWidget):
    def __init__(self, train_asset: str, train_nr: int = None, parent=None):
        super().__init__(parent=parent)
        self.uuid: UUID = uuid4()
        self.train_nr = train_nr
        self.carriages: list[Carriage] = []

        if os.path.exists(f"assets/vozidla/{train_asset}.bmp"):
            self.train_body = QLabel(self)
            self.train_asset: QPixmap = QPixmap(f"assets/vozidla/{train_asset}.bmp")
            self.train_body.setPixmap(self.train_asset)
            self.train_body.move(0, 0)
        else:
            raise FileNotFoundError(f"Train asset {train_asset} not found")

        self.setGeometry(0, 0, self.train_asset.width(), 45)

        self.context_menu = QMenu(self)  # move top menu into station button ???
        if self.train_nr:
            train_nr_item = QAction(str(self.train_nr), self)
            train_nr_item.setEnabled(False)
            self.context_menu.addAction(train_nr_item)
            self.context_menu.addSeparator()

        self.shunt_action = QAction("Posun", self)
        self.shunt_action.setIcon(QIcon("assets/shunting_icon.png"))
        self.context_menu.addAction(self.shunt_action)

        self.dispatch_action = QAction("Vypraviť", self)
        self.dispatch_action.setIcon(QIcon("assets/dispatch_icon.png"))
        self.context_menu.addAction(self.dispatch_action)

        self.new_train_action = QAction("Zaviesť nový vlak", self)
        self.new_train_action.setIcon(QIcon("assets/new_train_icon.png"))
        self.context_menu.addAction(self.new_train_action)

        self.refresh_train_action = QAction("Obnoviť vlak", self)
        self.refresh_train_action.setIcon(QIcon("assets/refresh_train_icon.png"))
        self.context_menu.addAction(self.refresh_train_action)

    def add_carriage(self, carriage: Carriage):
        self.carriages.append(carriage)
        carriage.setParent(self)
        carriage.move(self.width(), 0)
        self.setGeometry(
            0,
            0,
            self.train_asset.width() + sum([c.width() for c in self.carriages]),
            45,
        )

    def contextMenuEvent(self, event):
        self.context_menu.exec_(event.globalPos())
