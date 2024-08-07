from PyQt5.QtWidgets import (
    QMainWindow,
    QLabel,
    QMessageBox,
    QMenu,
    QMenuBar,
    QAction,
    QTableWidget,
    QTableWidgetItem,
)
import logging
from PyQt5.QtGui import QFont, QIcon, QKeySequence


class TrafficDiary(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Dopravný denník")
        self.setWindowIcon(QIcon("assets/app_icon.png"))
        self.setFont(QFont("Arial", 11))
        self.logger = logging.getLogger("App.Client.TrafficDiary")
        self.logger.setLevel(logging.DEBUG)
        self.setGeometry(200, 200, 600, 500)
        self.setFixedWidth(600)

        self.menuBar = QMenuBar(self)
        self.menuBar.setFont(QFont("Arial", 10))
        self.menuBar.setFixedWidth(600)

        self.table = QTableWidget(self)
        self.table.move(0, 30)
        self.table.setFixedWidth(600)
        self.table.setColumnCount(7)
        self.table.setWordWrap(True)
        self.table.verticalHeader().setVisible(False)
        self.table.setAlternatingRowColors(True)
        self.table.setHorizontalHeaderLabels(
            [
                "Číslo\nvlaku",
                "Príchod",
                "Odchod",
                "Meškanie",
                "Koľaj\ndo",
                "Koľaj\nz",
                "Poznámka",
            ]
        )
        self.table.resizeColumnsToContents()

        self.diary_menu: QMenu = self.menuBar.addMenu("Denník")
        new_train_action: QAction = self.diary_menu.addAction("Nový vlak")
        new_train_action.triggered.connect(
            lambda: self.table.insertRow(self.table.rowCount())
        )
        new_train_action.setShortcut(QKeySequence("Ctrl+N"))
        train_info_action: QAction = self.diary_menu.addAction("Informácie o vlaku")
        train_info_action.setShortcut(QKeySequence("Ctrl+I"))
        self.diary_menu.addSeparator()
        pull_trains_action: QAction = self.diary_menu.addAction("Obnoviť denník")
        pull_trains_action.setShortcut(QKeySequence("Ctrl+R"))
        resize_columns_action: QAction = self.diary_menu.addAction("Prispôsobiť stĺpce")
        resize_columns_action.triggered.connect(self.table.resizeColumnsToContents)
        resize_columns_action.setShortcut(QKeySequence("Ctrl+Shift+R"))

        self.edit_menu: QMenu = self.menuBar.addMenu("Záznam")
        train_departure_action: QAction = self.edit_menu.addAction("Predvídaný odchod")
        train_departure_action.setShortcut(QKeySequence("Ctrl+D"))
        self.edit_menu.addSeparator()
        edit_train_action: QAction = self.edit_menu.addAction("Upraviť vlak")
        edit_train_action.setShortcut(QKeySequence("Ctrl+E"))
        delete_train_action: QAction = self.edit_menu.addAction("Vymazať vlak")
        delete_train_action.setShortcut(QKeySequence("Ctrl+Shift+D"))

    def resizeEvent(self, event):
        self.table.setFixedHeight(self.height() - 30)
