from PyQt5.QtWidgets import QGraphicsScene, QGraphicsRectItem, QSplashScreen, QGraphicsEllipseItem
from PyQt5.QtGui import QBrush, QPen, QFont
from PyQt5.QtCore import Qt
import os
from time import sleep
from game.dialogs.qt_app import PyQtApp
from game.dialogs.boxes import entryWindow
from game.control.track_segment import Track

app = PyQtApp("assets/editor.ui")
assets_path = (os.getcwd() + "/assets/").replace("\\", "/")
tool = None
map = dict()

def exit() -> None:
    app.window.close()

def message():
    # app.window.statusBar.showMessage("Hello World!")
    scene.clear()

def createScene():
    scene = QGraphicsScene(0,0,1000,550)
    app.window.graphicsView.setScene(scene)
    return scene

def testGraphics(x,y, scene):
    app.window.statusBar.showMessage("Not used")

def onHover(event):
    x, y = event.pos().x(), event.pos().y()
    app.window.label1.setText(f"[{x}, {y}]")

def selectTool(toolName):
    global tool
    tool = toolName

def deleteObject(x,y):
    for item in scene.items():
        if item.rect().x() == x and item.rect().y() == y:
            scene.removeItem(item)
            break

def addShape(type, x, y, xSize, ySize, pen, brush=QBrush(Qt.white)):
    if type == "rect":
        rect = QGraphicsRectItem(x, y, xSize, ySize)
        rect.setBrush(brush)
        rect.setPen(pen)
        return rect
    elif type == "ellipse":
        ellipse = QGraphicsEllipseItem(x, y, xSize, ySize)
        ellipse.setBrush(brush)
        ellipse.setPen(pen)
        return ellipse

def addTrack(x,y):
    entry = entryWindow("Define platform length")
    while True:
        entry.showWindow("Enter track segments count")
        lenght = entry.getText()
        if lenght is None:
            break
        try:
            lenght = int(lenght[0])
        except ValueError:
            app.window.statusBar.showMessage("Invalid input!")
        else:
            break
    if lenght:
        track = Track(x,y,lenght, scene=scene)
        track.drawTrack(game=False)
        # print(x,y)
        # pen = QPen(Qt.black)
        # pen.setWidth(4)
        # for i in range(lenght):
        #     rect = addShape("rect", x - 80 + (i * 60), y - 30, 50, 20, pen, QBrush(Qt.gray))          
        #     scene.addItem(rect)
        # start = addShape("ellipse", x - 105, y - 45, 15, 15, pen, QBrush(Qt.green))
        # end = addShape("ellipse", x - 80 + (lenght * 60), y - 45, 15, 15, pen, QBrush(Qt.red))
        # shunt = []        
        # shunt.append(addShape("ellipse", x - 125, y - 45, 15, 15, pen, QBrush(Qt.white)))
        # shunt.append(addShape("ellipse", x - 60 + (lenght * 60), y - 45, 15, 15, pen, QBrush(Qt.white)))
        # scene.addItem(end)
        # scene.addItem(shunt[0])
        # scene.addItem(shunt[1])
        # scene.addItem(start)
        # if map.get("tracks"):
        #     map["tracks"].append({"x": x, "y": y, "lenght": lenght})
        # else:
        #     map["tracks"] = [{"x": x, "y": y, "lenght": lenght}]

def addStation(): # add entry to config file
    entry = entryWindow("New station")
    while True:
        entry.showWindow("Station name")
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
    if tool == "delete":
        x, y = event.pos().x(), event.pos().y()
        deleteObject(x,y)
    if tool == "label":
        x, y = event.pos().x(), event.pos().y()
        t = scene.addText("here", QFont("Arial", 20))
        t.setPos(x-80,y-30) # calibration for click position
        a = scene.addEllipse(x-60,y-10,10,10,QPen(Qt.black),QBrush(Qt.red))
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
    app.window.actionRemove_element.triggered.connect(lambda: selectTool("delete"))
    app.window.actionTrack.triggered.connect(lambda: selectTool("track"))
    app.window.graphicsView.mousePressEvent = lambda event: onClick(event)
    app.window.graphicsView.mouseMoveEvent = lambda event: onHover(event)
    app.window.actionStation.triggered.connect(addStation)
    app.window.actionLabel.triggered.connect(lambda: selectTool("label"))
    app.execute()

if __name__ == "__main__":
    scene = createScene()
    main()