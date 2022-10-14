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
        if self.rotation == 45:
            main_rect = addShape("rect", self.x - 80, self.y - 30, 50, 20, pen, QBrush(Qt.gray))
            main_segment = addShape("rect", self.x - 20, self.y - 30, 50, 20, pen, QBrush(Qt.gray))
            blade_rect = addShape("rect", self.x - 70, self.y, 50, 20, pen, QBrush(Qt.gray), rotation=30)
            blade_segment = addShape("rect", self.x - 20, self.y + 20, 50, 20, pen, QBrush(Qt.gray))
        elif self.rotation == -45:
            main_rect = addShape("rect", self.x - 80, self.y - 30, 50, 20, pen, QBrush(Qt.gray))
            main_segment = addShape("rect", self.x - 20, self.y - 30, 50, 20, pen, QBrush(Qt.gray))
            blade_rect = addShape("rect", self.x - 20, self.y + 25, 50, 20, pen, QBrush(Qt.gray), rotation=-30)
            blade_segment = addShape("rect", self.x - 80, self.y + 20, 50, 20, pen, QBrush(Qt.gray))
        elif self.rotation == 135:
            main_rect = addShape("rect", self.x - 80, self.y + 20, 50, 20, pen, QBrush(Qt.gray))
            main_segment = addShape("rect", self.x - 20, self.y + 20, 50, 20, pen, QBrush(Qt.gray))
            blade_rect = addShape("rect", self.x - 30, self.y - 15, 50, 20, pen, QBrush(Qt.gray), rotation=150)
            blade_segment = addShape("rect", self.x - 20, self.y - 30, 50, 20, pen, QBrush(Qt.gray))
        elif self.rotation == -135:
            main_rect = addShape("rect", self.x - 80, self.y + 20, 50, 20, pen, QBrush(Qt.gray))
            main_segment = addShape("rect", self.x - 20, self.y + 20, 50, 20, pen, QBrush(Qt.gray))
            blade_rect = addShape("rect", self.x + 25, self.y + 10, 50, 20, pen, QBrush(Qt.gray), rotation=-150)
            blade_segment = addShape("rect", self.x - 80, self.y - 30, 50, 20, pen, QBrush(Qt.gray))
        
        self.segmentsObj += [main_rect, blade_rect, main_segment, blade_segment] # add all segments to the list
        self.canvas.addItem(main_rect)
        self.canvas.addItem(main_segment)
        self.canvas.addItem(blade_rect)
        self.canvas.addItem(blade_segment)

    def removeTrack(self, **kwargs): # will be probably used only in editor
        items = self.canvas.items()
        for item in items:
            for obj in self.segmentsObj:
                if obj.x == item.x and obj.y == item.y:
                    self.canvas.removeItem(item)
        