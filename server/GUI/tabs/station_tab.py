from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QComboBox,
    QCheckBox,
    QListView,
    QLineEdit,
    QGroupBox,
    QFileDialog,
)
from PyQt5.QtGui import QFont, QIntValidator


class StationTab(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.setFont(QFont("Arial", 11))

        self.station_name_label = QLabel("Názov stanice (N):", self)
        self.station_name_label.move(5, 5)

        self.station_name_input = QLineEdit(self)
        self.station_name_input.move(140, 5)

        self.station_name_G_label = QLabel("Názov stanice (G):", self)
        self.station_name_G_label.move(5, 35)

        self.station_name_G_input = QLineEdit(self)
        self.station_name_G_input.move(140, 35)

        self.allow_2L_checkbox = QCheckBox("Povoliť 2L", self)
        self.allow_2L_checkbox.move(5, 65)

        self.add_station_button = QPushButton("Pridať stanicu", self)
        self.add_station_button.move(5, 95)

        self.station_list = QListView(self)
        self.station_list.move(300, 5)
        self.station_list.setFixedSize(290, 400)

        self.remove_station_button = QPushButton("Odstrániť stanicu", self)
        self.remove_station_button.move(470, 410)

        self.show_advanced_checkbox = QCheckBox("Zobraziť rozšírené nastavenia", self)
        self.show_advanced_checkbox.move(5, 125)
        self.show_advanced_checkbox.stateChanged.connect(
            lambda: self.advanced_settings_group.setVisible(
                self.show_advanced_checkbox.isChecked()
            )
        )

        self.advanced_settings_group = QGroupBox("Rozšírené nastavenia", self)
        self.advanced_settings_group.move(5, 150)
        self.advanced_settings_group.setFixedSize(290, 300)
        self.advanced_settings_group.hide()

        self.load_track_file = QPushButton("Načítať trať", self)
        self.load_track_file.clicked.connect(self.load_track_file_func)
        self.load_track_file.setFixedSize(100, 25)
        self.load_track_file.move(5, 510)

        self.save_track_file = QPushButton("Uložiť trať", self)
        self.save_track_file.clicked.connect(self.save_track_file_func)
        self.save_track_file.setFixedSize(100, 25)
        self.save_track_file.move(110, 510)

    def load_track_file_func(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Načítať trať", "", "JSON súbory (*.json)"
        )
        if file_name:
            self.parent.logger.debug(f"Loading track file: {file_name}")
            pass

    def save_track_file_func(self):
        file_name, _ = QFileDialog.getSaveFileName(
            self, "Uložiť trať", "", "JSON súbory (*.json)"
        )
        if file_name:
            self.parent.logger.debug(f"Saving track file: {file_name}")
            pass
