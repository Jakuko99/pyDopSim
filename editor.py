from PyQt5.QtWidgets import QGraphicsScene, QGraphicsRectItem, QSplashScreen, QGraphicsEllipseItem, QListWidgetItem
from PyQt5.QtGui import QBrush, QPen, QFont
from PyQt5.QtCore import Qt
import os
from time import sleep
from game.dialogs.qt_app import PyQtApp
from game.dialogs.boxes import entryWindow
from game.tracks.track import Track
from game.tracks.switch import Switch

app = PyQtApp("assets/editor.ui")
assets_path = (os.getcwd() + "/assets/").replace("\\", "/")
tool = None
tracks : list[Track] = []
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
    pass

def onHover(event):
    x, y = event.pos().x(), event.pos().y()
    app.window.label1.setText(f"[{x}, {y}]")

def selectTool(toolName):
    global tool
    tool = toolName

def deleteSelected():
    item : QListWidgetItem = app.window.listWidget1.currentItem()
    itemText = item.text() # needs to be done this way for some reason
    a,b = itemText.find("[") + 1, itemText.find("]")
    position = (itemText[a:b].replace(" ","").split(","))
    global tracks
    for track in tracks:
        pos = track.returnPosition()
        if (pos[0] == int(position[0]) and pos[1] == int(position[1])):
            track.removeTrack()
            app.window.listWidget1.takeItem(app.window.listWidget1.currentRow())
            tracks.remove(track)

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
        global tracks
        x, y = x - (x % 10), y - (y % 10) # grid correction
        track = Track(x,y,lenght, scene=scene)
        track.drawTrack(game=False)
        app.window.listWidget1.addItem(f"Track at [{track.x}, {track.y}], lenght: {lenght}") #add object to list
        tracks.append(track)
    
def addSwitch(x,y):
    entry = entryWindow("Define switch orientation")
    while True:
        entry.selectionWindow(Orientation=["0","180"], Segments=["1","2","3"])
        orientation = entry.getText()
        if orientation is None:
            break
        try:
            orientation = int(orientation[0])
        except ValueError:
            app.window.statusBar.showMessage("Invalid input!")
        else:
            break
    if orientation:
        global tracks
        x, y = x - (x % 10), y - (y % 10)
        switch = Switch(x,y,orientation, scene=scene)
        switch.drawSwitch(game=False)
        app.window.listWidget1.addItem(f"Switch at [{switch.x}, {switch.y}], orientation: {orientation}")
        tracks.append(switch)

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
    x, y = event.pos().x(), event.pos().y()
    if tool == "track":
        addTrack(x,y)
    elif tool == "switch":
        addSwitch(x,y)
    elif tool == "label":
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
    app.window.actionRemove_element.triggered.connect(deleteSelected)
    app.window.Button1.clicked.connect(deleteSelected)
    app.window.actionTrack.triggered.connect(lambda: selectTool("track"))
    app.window.actionSwitch.triggered.connect(lambda: selectTool("switch"))
    app.window.graphicsView.mousePressEvent = lambda event: onClick(event)
    app.window.graphicsView.mouseMoveEvent = lambda event: onHover(event)
    app.window.actionStation.triggered.connect(addStation)
    app.window.actionLabel.triggered.connect(lambda: selectTool("label"))
    app.execute()

if __name__ == "__main__":
    scene = createScene()
    main()