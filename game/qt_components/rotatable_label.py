from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import QSize

class RotatableLabel(QLabel):

    def __init__(self, text: str, angle:int, parent=None):
        QLabel.__init__(self, text=text, parent=parent)
        self.angle = angle

    def paintEvent(self, event):
        QLabel.paintEvent(self, event)
        painter = QPainter (self)
        painter.translate(0, self.height()-1)
        painter.rotate(self.angle)
        self.setGeometry(self.x(), self.y(), self.height(), self.width())
        QLabel.render(self, painter)

    def minimumSizeHint(self):
        size = QLabel.minimumSizeHint(self)
        return QSize(size.height(), size.width())

    def sizeHint(self):
        size = QLabel.sizeHint(self)
        return QSize(size.height(), size.width())