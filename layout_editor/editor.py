from PyQt import PyQtApp
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView, QGraphicsRectItem, QApplication, QSplashScreen
from PyQt5.QtWidgets import QDialog, QPushButton, QLineEdit
from PyQt5.QtGui import QBrush, QPen
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
import os
from time import sleep
from boxes import entryWindow

app = PyQtApp("layout_editor/main.ui")
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
    entry = entryWindow()
    while True:
        entry.showWindow("Enter track segments count:")
        lenght = entry.getText()
        if lenght is None:
            break
        try:
            lenght = int(lenght)
        except ValueError:
            app.window.statusBar.showMessage("Invalid input!")
        else:
            break
    if lenght:
        for i in range(lenght):
            rect = QGraphicsRectItem(x - 80 + (i * 60), y - 30, 50, 20)
            rect.setPos(20,20)
            brush = QBrush(Qt.gray)
            rect.setBrush(brush)
            pen = QPen(Qt.black)
            pen.setWidth(5)
            rect.setPen(pen)
            scene.addItem(rect)

def addStation():
    entry = entryWindow()
    while True:
        entry.showWindow("Enter number of stations")
        try:
            nr = int(entry.getText())
        except ValueError:
            app.window.statusBar.showMessage("Invalid input!")
        else:
            break

    print(nr)


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