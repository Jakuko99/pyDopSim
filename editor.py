from PyQt5.QtWidgets import QGraphicsScene, QGraphicsRectItem, QSplashScreen, QGraphicsEllipseItem, QListWidgetItem, QFileDialog, QGraphicsPixmapItem
from PyQt5.QtGui import QBrush, QPen, QFont, QPixmap
from PyQt5.QtCore import Qt, QSize
import json
from uuid import uuid4, UUID
import os
from time import sleep

from game.dialogs.qt_app import PyQtApp
from game.dialogs.boxes import entryWindow
from game.tracks.track import Track
from game.tracks.switch import Switch

app = PyQtApp("assets/editor.ui")
assets_path = (os.getcwd() + "/assets/").replace("\\", "/")
tool = None
tracks: dict[UUID:dict] = dict()
hover_obj = None
map = dict()


def exit() -> None:
    app.window.close()


def delete_all_objects():
    # app.window.statusBar.showMessage("Hello World!")
    app.window.listWidget1.clear()
    scene.clear()


def createScene():
    scene = QGraphicsScene(0, 0, 1000, 550)
    app.window.graphicsView.setScene(scene)
    return scene


def testGraphics(x, y, scene):
    pass


def onHover(event):
    global hover_obj
    x, y = event.pos().x(), event.pos().y()
    # x, y = x - (x % 10), y - (y % 10)

    if tool == "track" and hover_obj is None:
        hover_obj = Track(x-164, y-23, 1, scene=scene, app=app)  # 170,25
        hover_obj.drawTrack(game=False)
    elif tool == "track" and hover_obj is not None:
        hover_obj.moveTrack(x-164, y-23)
    app.window.label1.setText(f"[{x}, {y}]")


def selectTool(toolName):
    global tool
    tool = toolName


def deleteSelected():
    item: QListWidgetItem = app.window.listWidget1.currentItem()
    if item is not None:
        itemText = item.text()  # needs to be done this way for some reason
        a, b = itemText.find("[") + 1, itemText.find("]")
        position = (itemText[a:b].replace(" ", "").split(","))
        global tracks
        for track in tracks.items():
            pos = (track["x"], track["y"])
            if (pos[0] == int(position[0]) and pos[1] == int(position[1])):
                # track.removeTrack() # need to have a reference to the object
                app.window.listWidget1.takeItem(
                    app.window.listWidget1.currentRow())
                tracks.popitem(track)
    else:
        app.window.statusBar.showMessage("Nothing selected!")


def addTrack(x, y):
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
        x, y = x - (x % 10), y - (y % 10)  # grid correction
        track = Track(x, y, lenght, scene=scene)
        track.drawTrack(game=False)
        app.window.listWidget1.addItem(
            f"Track at [{track.x}, {track.y}], lenght: {lenght}")  # add object to list
        tracks[str(track.uuid)] = track.as_dict


def addSwitch(x, y):
    entry = entryWindow("Define switch orientation")
    while True:
        entry.selectionWindow(Orientation=["45", "-45", "135", "-135"])
        orientation = entry.getSelection()
        try:
            orientation = int(orientation["Orientation"])
        except KeyError:
            app.window.statusBar.showMessage("Invalid input!")
        else:
            break
    if orientation:
        global tracks
        x, y = x - (x % 10), y - (y % 10)
        switch = Switch(x, y, orientation, scene=scene)
        switch.drawSwitch(game=False)
        app.window.listWidget1.addItem(
            f"Switch at [{switch.x}, {switch.y}], type: {orientation}")
        tracks[str(switch.uuid)] = switch.as_dict


def addStation():  # add entry to config file
    entry = entryWindow("New station")
    while True:
        entry.showWindow("Station name")
        try:
            stationName = entry.getText()
        except ValueError:
            app.window.statusBar.showMessage("Invalid input!")
        else:
            break
    if stationName:
        found = False
        for item in tracks:
            if item["type"] == "station":
                found = True
        if not found:  # only one station allowed
            text = scene.addText(stationName[0], QFont("Arial", 20))
            text.setPos(450, 0)
            tracks[str(uuid4())] = {"type": "station", "name": stationName[0]}
        else:
            app.window.statusBar.showMessage("Station name already set!")


def save():
    dialog = QFileDialog()
    dialog.setNameFilter("JSON (*.json)")
    dialog.setDefaultSuffix("json")
    dialog.setAcceptMode(QFileDialog.AcceptSave)
    dialog.setDirectory(os.getcwd())
    if dialog.exec_():
        filename = dialog.selectedFiles()[0]
        with open(filename, "w") as file:
            json.dump(tracks, file, indent=4)


def onClick(event):
    global tool
    x, y = event.pos().x(), event.pos().y()
    if tool == "track":
        addTrack(x, y)
    elif tool == "switch":
        addSwitch(x, y)
    elif tool == "label":
        t = scene.addText("here", QFont("Arial", 20))
        t.setPos(x-80, y-30)  # calibration for click position
        a = scene.addEllipse(x-60, y-10, 10, 10,
                             QPen(Qt.black), QBrush(Qt.red))
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
    app.window.actionRemove.triggered.connect(delete_all_objects)
    app.window.actionTest.triggered.connect(
        lambda: testGraphics(100, 100, scene))
    app.window.actionRemove_element.triggered.connect(deleteSelected)
    app.window.Button1.clicked.connect(deleteSelected)
    app.window.actionTrack.triggered.connect(lambda: selectTool("track"))
    app.window.actionSwitch.triggered.connect(lambda: selectTool("switch"))
    app.window.graphicsView.mousePressEvent = lambda event: onClick(event)
    app.window.graphicsView.mouseMoveEvent = lambda event: onHover(event)
    app.window.actionStation.triggered.connect(addStation)
    app.window.actionLabel.triggered.connect(lambda: selectTool("label"))
    app.window.actionSave.triggered.connect(save)

    # add image to graphics view
    # image = QPixmap()
    # image.load("assets/splash.png")
    # imageItem = QGraphicsPixmapItem()
    # imageItem.setPixmap(image)
    # imageItem.mousePressEvent = lambda event: app.window.statusBar.showMessage("Clicked!") # define click event on image
    # scene.addItem(imageItem)

    app.execute()


if __name__ == "__main__":
    scene = createScene()
    main()
