from PyQt5.QtWidgets import QWidget

from game.qt_components.api_package import AbstractButton, AbstractIndicatorSlim


class AutoBlock(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
