from PyQt5.QtWidgets import QFileDialog

from game.dialogs.qt_app import PyQtApp

if __name__ == "__main__":
    app = PyQtApp("assets/client.ui") # TODO: create layout file
    app.window.show()
    app.run()