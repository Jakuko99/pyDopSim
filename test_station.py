from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox

import game.api_package as game

if __name__ == "__main__":
    app = QApplication([])
    window = game.REStation("Vrútky")
    window.show()

    app.exec_()
