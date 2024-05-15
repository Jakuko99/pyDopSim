from PyQt5.QtWidgets import QMenu, QAction, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from uuid import UUID, uuid4

from game.objects.carriage import Carriage
from game.objects.locomotive import Locomotive
from game.data_types.api_package import TrainType


class Consist(QWidget):
    def __init__(self, train_nr: int = None, parent=None):
        super().__init__(parent=parent)
        self.uuid: UUID = uuid4()
        self.carriages: list[Carriage] = []
        self.locomotives: list[Locomotive] = []
        self.train_nr = train_nr
        self.train_type: TrainType = None
        self.setGeometry(0, 0, 5, 45)
        self.setMinimumSize(5, 45)

        self.context_menu = QMenu(self)  # move top menu into station button ???
        if self.train_nr:
            train_nr_item = QAction(
                f"{self.train_type.name if self.train_type else ''} {self.train_nr}",
                self,
            )
            train_nr_item.setEnabled(False)
            self.context_menu.addAction(train_nr_item)
            self.context_menu.addSeparator()
        else:
            train_nr_item = QAction("(nepriradené číslo)", self)
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
        carriage.move(self.width() + 2, 0)
        self.setFixedSize(self.width() + carriage.width() + 2, 45)

    def add_locomotive(self, locomotive: Locomotive):
        self.locomotives.append(locomotive)
        locomotive.setParent(self)
        locomotive.move(self.width() + 2, 0)
        self.setFixedSize(self.width() + locomotive.width() + 2, 45)

    def remove_all(self):
        self.locomotives.clear()  # TODO: need to fix this method
        self.carriages.clear()

    def contextMenuEvent(self, event):
        self.context_menu.exec_(event.globalPos())

    def set_train_number(self, train_type: TrainType, train_nr: int):
        self.train_type = train_type
        self.train_nr = train_nr
        self.context_menu.actions()[0].setText(
            f"{self.train_type.name} {self.train_nr}"
        )
