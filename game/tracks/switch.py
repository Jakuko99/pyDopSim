from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QPen, QColor
from PyQt5.QtWidgets import QGraphicsScene

from game.tracks.track_segment import TrackSegment
from game.dialogs.qt_app import addShape

class Switch(TrackSegment):
    def __init__(self, x : int, y : int , rotation : int, scene : QGraphicsScene, **kwargs):
        self.x = x
        self.y = y
        self.rotation = rotation
        self.segmentsObj = []
        self.canvas = scene
        self.position = 0 # 0 - straight, 1 - switched (direction depending on the orientation)

    def _changeState(self, state : bool):
        self.occupied = state
        if self.occupied: # set color to orange
            for segment in self.segmentsObj:
                segment.setBrush(QBrush(QColor(255,127,0)))
        else: # set color to gray 
            for segment in self.segmentsObj:
                segment.setBrush(QBrush(Qt.gray))
            
    def returnPosition(self):
        return self.x, self.y
            
    def drawSwitch(self, game : bool = True):
        pen = QPen(Qt.black)
        pen.setWidth(5)
        main_rect = addShape("rect", self.x - 80, self.y - 30, 50, 20, pen, QBrush(Qt.gray))
        self.segmentsObj.append(main_rect)
        self.canvas.addItem(main_rect)
        blade_section = None

    def removeTrack(self, **kwargs): # will be probably used only in editor
        items = self.canvas.items()
        for item in items:
            for obj in self.segmentsObj:
                if obj.x == item.x and obj.y == item.y:
                    self.canvas.removeItem(item)
        