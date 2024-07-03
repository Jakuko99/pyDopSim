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
    table_headers = ["Stanica", "Meno výpravcu", "Stav", "Vedľajšie stanice"]

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
            self.tableWidget.setItem(pos, 1, QTableWidgetItem(content.player_name))
            self.tableWidget.setItem(pos, 2, QTableWidgetItem(content.status.name))
            next_stations: str = ""
            if content.left_station:
                next_stations += content.left_station + ", "
            if content.right_station:
                next_stations += content.right_station + ", "
            if content.turn_station:
                next_stations += content.turn_station
            self.tableWidget.setItem(
                pos, 3, QTableWidgetItem(next_stations.strip(", "))
            )
            pos += 1

        self.tableWidget.resizeRowsToContents()

        #    for vlak in response_obj:
        #     self.tableWidget.setItem(pos, 0, QTableWidgetItem(
        #         vlak.get('DruhVlakuKom').strip()+" "+str(vlak.get("CisloVlaku"))))
        #     train_types.add(vlak.get('DruhVlakuKom').strip())
        #     self.tableWidget.setItem(
        #         pos, 1, QTableWidgetItem(vlak.get('StanicaVychodzia')))
        #     self.tableWidget.setItem(
        #         pos, 2, QTableWidgetItem(vlak.get('CasVychodzia')))
        #     self.tableWidget.setItem(
        #         pos, 3, QTableWidgetItem(vlak.get('StanicaCielova')))
        #     self.tableWidget.setItem(
        #         pos, 4, QTableWidgetItem(vlak.get('CasCielova')))
        #     self.tableWidget.setItem(
        #         pos, 5, QTableWidgetItem(vlak.get('StanicaUdalosti')))
        #     self.tableWidget.setItem(
        #         pos, 6, QTableWidgetItem(vlak.get('CasUdalosti')))
        #     self.tableWidget.setItem(pos, 7, QTableWidgetItem(
        #         str(vlak.get('Meskanie')) + " min"))
        #     # set color of the cell based on the value
        #     if vlak.get('Meskanie') <= 0:
        #         self.tableWidget.item(pos, 7).setBackground(
        #             QColor(255, 255, 255))
        #     elif vlak.get('Meskanie') < 10:
        #         self.tableWidget.item(pos, 7).setBackground(QColor(0, 255, 0))
        #     elif vlak.get('Meskanie') < 20:
        #         self.tableWidget.item(pos, 7).setBackground(
        #             QColor(255, 255, 0))
        #     else:
        #         self.tableWidget.item(pos, 7).setBackground(QColor(255, 0, 0))
        #     self.tableWidget.setItem(
        #         pos, 8, QTableWidgetItem(vlak.get('Dopravca')))
        #     pos += 1
        # self.tableWidget.resizeColumnsToContents()
