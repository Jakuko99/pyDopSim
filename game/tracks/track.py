from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QPen, QColor
from PyQt5.QtWidgets import QGraphicsScene

from game.tracks.track_segment import TrackSegment
from game.dialogs.qt_app import addShape


class Track(TrackSegment):  # inherits properties from TrackSegment
    def __init__(self, x: int, y: int, nrSegments: int, scene: QGraphicsScene, **kwargs):
        super().__init__(x, y)
        self.x = x
        self.y = y
        self.segments = nrSegments
        self.segmentsObj = []
        self.canvas = scene
        self.game = True

    @property
    def as_dict(self):
        return {"type":"track","x": self.x, "y": self.y, "segments": self.segments}

    def returnPosition(self) -> tuple:
        return self.x, self.y

    @property
    def length(self):
        return self.segments

    def _changeState(self, state: bool):
        self.occupied = state
        if self.occupied:  # set color to orange
            for segment in self.segmentsObj:
                # RGB values for orange color
                segment.setBrush(QBrush(QColor(255, 127, 0)))
        else:  # set color to gray
            for segment in self.segmentsObj:
                segment.setBrush(QBrush(Qt.gray))

    def drawTrack(self, game: bool = True):
        self.game = game  # override default value
        pen = QPen(Qt.black)
        pen.setWidth(5)
        for i in range(self.segments):
            rect = addShape("rect", self.x - 80 + (i * 60),
                            self.y - 30, 50, 20, pen, QBrush(Qt.gray))
            self.segmentsObj.append(rect)
            self.canvas.addItem(rect)
        if game:
            start = addShape("ellipse", self.x - 105, self.y -
                             45, 15, 15, pen, QBrush(Qt.green))
            end = addShape("ellipse", self.x - 80 + (self.segments * 60),
                           self.y - 45, 15, 15, pen, QBrush(Qt.red))
            shunt = []
            shunt.append(addShape("ellipse", self.x - 125,
                         self.y - 45, 15, 15, pen, QBrush(Qt.white)))
            shunt.append(addShape("ellipse", self.x - 60 + (self.segments * 60),
                         self.y - 45, 15, 15, pen, QBrush(Qt.white)))
            self.canvas.addItem(end)
            self.canvas.addItem(shunt[0])
            self.canvas.addItem(shunt[1])
            self.canvas.addItem(start)

    def removeTrack(self, **kwargs):  # will be probably used only in editor
        items = self.canvas.items()
        for item in items:
            for obj in self.segmentsObj:
                if obj.x == item.x and obj.y == item.y:
                    self.canvas.removeItem(item)

    def moveTrack(self, x: int, y: int):
        for i in range(self.segments):
            self.segmentsObj[i].setPos(x, y)
