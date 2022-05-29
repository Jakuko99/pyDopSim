from tkinter import E
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsRectItem, QSplashScreen, QGraphicsEllipseItem
from PyQt5.QtGui import QBrush, QPen, QFont
from PyQt5.QtCore import Qt
import os
from time import sleep
from game.dialogs.qt_app import PyQtApp
from game.dialogs.boxes import entryWindow
# from game.control.track_segment import trackSegment

app = PyQtApp("assets/main.ui")
assets_path = (os.getcwd() + "/assets/").replace("\\", "/")
tool = None
map = dict()

def exit() -> None:
    app.window.close()

def message():
    app.window.statusBar.showMessage("Hello World!")

def createScene():
    scene = QGraphicsScene(0,0,1000,550)
    app.window.graphicsView.setScene(scene)
    return scene

def testGraphics(x,y, scene):
    # scene = QGraphicsScene(0,0,700,400)
    rect = QGraphicsRectItem(x - 70,y - 60,50,50)
    rect.setPos(20,20)
    brush = QBrush(Qt.red)
    rect.setBrush(brush)
    pen = QPen(Qt.cyan)
    pen.setWidth(10)
    rect.setPen(pen)
    scene.addItem(rect)
    app.window.graphicsView.setScene(scene)    

def onHover(event):
    x, y = event.pos().x(), event.pos().y()
    app.window.label1.setText(f"[{x}, {y}]")

def selectTrack():
    global tool
    tool = "track"

def addTrack(x,y):
    entry = entryWindow("Define platform lenght")
    while True:
        entry.showWindow("Enter track segments count")
        lenght = entry.getText()[0]
        if lenght is None:
            break
        try:
            lenght = int(lenght)
        except ValueError:
            app.window.statusBar.showMessage("Invalid input!")
        else:
            break
    if lenght:
        pen = QPen(Qt.black)
        pen.setWidth(4)
        for i in range(lenght):
            rect = QGraphicsRectItem(x - 80 + (i * 60), y - 30, 50, 20)
            rect.setPos(20,20)
            rect.setBrush(QBrush(Qt.gray))            
            rect.setPen(pen)            
            scene.addItem(rect)
        start = QGraphicsEllipseItem(x - 80, y - 30, 15, 15)
        start.setPen(pen)
        start.setBrush(QBrush(Qt.green))
        end = QGraphicsEllipseItem(x - 80 + (lenght * 60) + 15, y - 30, 15, 15)
        end.setPen(pen)
        end.setBrush(QBrush(Qt.red))
        scene.addItem(end)
        scene.addItem(start)

def addStation(): # add entry to config file
    entry = entryWindow("Creating station")
    while True:
        entry.showWindow("Set name of station")
        try:
            stationName = entry.getText()
        except ValueError:
            app.window.statusBar.showMessage("Invalid input!")
        else:
            break
    text = scene.addText(stationName[0], QFont("Arial", 20))
    text.setPos(450,0)


def onClick(event):
    global tool
    if tool == "track":
        x, y = event.pos().x(), event.pos().y()
        addTrack(x,y)
    elif tool is None:
        app.window.statusBar.showMessage("Select a tool first!")

def main():
    # splash = QSplashScreen(QtGui.QPixmap(assets_path + "splash.png"))
    # splash.show()
    # splash.showMessage("Loading...", Qt.AlignBottom | Qt.AlignCenter, Qt.black)
    # sleep(1)
    # splash.finish(app.window)
    app.window.actionExit.triggered.connect(exit)
    app.window.actionExit.setShortcut("Ctrl+Q")
    app.window.actionRemove.triggered.connect(message)
    app.window.actionTest.triggered.connect(lambda: testGraphics(100,100, scene))
    app.window.actionTrack.triggered.connect(selectTrack)
    app.window.graphicsView.mousePressEvent = lambda event: onClick(event)
    app.window.graphicsView.mouseMoveEvent = lambda event: onHover(event)
    app.window.actionStation.triggered.connect(addStation)
    app.execute()

if __name__ == "__main__":
    scene = createScene()
    main()