from PyQt5.QtWidgets import QLayout

from game.data_types.api_package import Tracks
from game.objects.api_package import Consist
from game.data_types.exceptions import (
    InvalidTrack,
    NotEnoughSpace,
    TrainTooLong,
    TrainAlreadyOnTrack,
)


class AbstractTrainLayout(QLayout):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._parent = parent

    def add_train(self, track_nr: Tracks, track_pos: int, train: Consist):
        pass
