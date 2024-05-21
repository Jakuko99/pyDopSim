from PyQt5.QtWidgets import QLayout
from uuid import UUID

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
        self.consists: dict[UUID, Consist] = dict()

    def add_train(self, track_nr: Tracks, track_pos: int, train: Consist):
        train.setParent(self)
        self.consists[train.uuid] = train
        train.move(track_pos, track_nr.value)
        self.addWidget(train)
