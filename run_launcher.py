from PyQt5.QtWidgets import QApplication

from launcher.api_package import Launcher

if __name__ == "__main__":
    app = QApplication([])
    launcher = Launcher()
    launcher.show()
    app.exec_()
