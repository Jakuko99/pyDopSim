from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QPen
from PyQt5.QtWidgets import QGraphicsScene
from game.dialogs.qt_app import addShape

class Track: # maybe create base class track segment and then inherit from it
    def __init__(self, x : int, y : int, nrSegments : int, scene : QGraphicsScene, **kwargs):
        self.x = x
        self.y = y
        self.segments = nrSegments
        self.segmentsObj = []
        self.canvas = scene
        self.occupied = False
        self.occupiedBy = "free"

    @property
    def isOccupied(self):
        return self.occupied

    def occupiedBy(self):
        return self.occupiedBy

    def occupy(self, train : str):
        self.occupied = True
        self.occupiedBy = train
        self._changeState(self.occupied)

    def free(self):
        self.occupied = False
        self.occupiedBy = "free"
        self._changeState(self.occupied)

    def _changeState(self, state : bool):
        self.occupied = state
        if self.occupied: # set color to red
            for segment in self.segmentsObj:
                segment.setBrush(QBrush(Qt.red))
        else: # set color to gray 
            for segment in self.segmentsObj:
                segment.setBrush(QBrush(Qt.gray))

    def drawTrack(self, game : bool = True):
        pen = QPen(Qt.black)
        pen.setWidth(5)
        for i in range(self.segments):
            rect = addShape("rect", self.x - 80 + (i * 60), self.y - 30, 50, 20, pen, QBrush(Qt.gray))          
            self.segmentsObj.append(rect)
            self.canvas.addItem(rect)            
        if game:
            start = addShape("ellipse", self.x - 105, self.y - 45, 15, 15, pen, QBrush(Qt.green))
            end = addShape("ellipse", self.x - 80 + (self.segments * 60), self.y - 45, 15, 15, pen, QBrush(Qt.red))
            shunt = []        
            shunt.append(addShape("ellipse", self.x - 125, self.y - 45, 15, 15, pen, QBrush(Qt.white)))
            shunt.append(addShape("ellipse", self.x - 60 + (self.segments * 60), self.y - 45, 15, 15, pen, QBrush(Qt.white)))
            self.canvas.addItem(end)
            self.canvas.addItem(shunt[0])
            self.canvas.addItem(shunt[1])
            self.canvas.addItem(start)