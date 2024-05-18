from PyQt5.QtWidgets import QLayout

from game.data_types.api_package import Tracks


class AbstractTrainLayout(QLayout):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._parent = parent
