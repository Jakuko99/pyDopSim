from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QComboBox,
    QCheckBox,
    QLineEdit,
    QWidget,
    QTableWidget,
    QTableWidgetItem,
)
from PyQt5.QtGui import QFont, QIntValidator
from ..objects.api_package import Station


class OverviewTab(QWidget):
    table_headers = ["Stanica", "Typ stanice", "Vedľajšie stanice"]

    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.setFont(QFont("Arial", 11))  # set font globally

        self.tableWidget = QTableWidget(self)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setColumnCount(len(self.table_headers))
        self.tableWidget.move(0, 0)
        self.tableWidget.setFixedSize(595, 400)
        for item in range(len(self.table_headers)):
            self.tableWidget.setHorizontalHeaderItem(
                item, QTableWidgetItem(self.table_headers[item])
            )
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.setWordWrap(True)

    def update_table(self, stations: dict[str:Station]):
        self.tableWidget.setRowCount(
            len(stations)
        )  # TODO: needs to have proper resizing
        pos = 0
        for station, content in stations.items():
            self.tableWidget.setItem(pos, 0, QTableWidgetItem(station))
            self.tableWidget.setItem(pos, 1, QTableWidgetItem(content.station_type))
            next_stations: str = ""
            if content.left_station:
                next_stations += content.left_station + ", "
            if content.right_station:
                next_stations += content.right_station + ", "
            if content.turn_station:
                next_stations += content.turn_station
            self.tableWidget.setItem(
                pos, 2, QTableWidgetItem(next_stations.strip(", "))
            )
            pos += 1

        self.tableWidget.resizeRowsToContents()
        self.tableWidget.resizeColumnToContents(
            0
        )  # resize only first column to fit the content
