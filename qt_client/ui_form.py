# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QStatusBar, QWidget)

class Ui_Application(object):
    def setupUi(self, Application):
        if not Application.objectName():
            Application.setObjectName(u"Application")
        Application.resize(800, 600)
        self.actionSettings = QAction(Application)
        self.actionSettings.setObjectName(u"actionSettings")
        self.actionExit = QAction(Application)
        self.actionExit.setObjectName(u"actionExit")
        self.actionAbout = QAction(Application)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionConnect_to_server = QAction(Application)
        self.actionConnect_to_server.setObjectName(u"actionConnect_to_server")
        self.actionDisconnect = QAction(Application)
        self.actionDisconnect.setObjectName(u"actionDisconnect")
        self.actionDisconnect.setEnabled(False)
        self.centralwidget = QWidget(Application)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 801, 31))
        font = QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setLineWidth(1)
        self.label.setTextFormat(Qt.MarkdownText)
        self.label.setAlignment(Qt.AlignCenter)
        Application.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Application)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        self.menuGame = QMenu(self.menubar)
        self.menuGame.setObjectName(u"menuGame")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        Application.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Application)
        self.statusbar.setObjectName(u"statusbar")
        Application.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuGame.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuGame.addAction(self.actionConnect_to_server)
        self.menuGame.addAction(self.actionDisconnect)
        self.menuGame.addAction(self.actionSettings)
        self.menuGame.addSeparator()
        self.menuGame.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(Application)

        QMetaObject.connectSlotsByName(Application)
    # setupUi

    def retranslateUi(self, Application):
        Application.setWindowTitle(QCoreApplication.translate("Application", u"PyDopSim", None))
        self.actionSettings.setText(QCoreApplication.translate("Application", u"Settings", None))
#if QT_CONFIG(shortcut)
        self.actionSettings.setShortcut(QCoreApplication.translate("Application", u"Ctrl+P", None))
#endif // QT_CONFIG(shortcut)
        self.actionExit.setText(QCoreApplication.translate("Application", u"Exit", None))
#if QT_CONFIG(shortcut)
        self.actionExit.setShortcut(QCoreApplication.translate("Application", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionAbout.setText(QCoreApplication.translate("Application", u"About", None))
#if QT_CONFIG(shortcut)
        self.actionAbout.setShortcut(QCoreApplication.translate("Application", u"Ctrl+H", None))
#endif // QT_CONFIG(shortcut)
        self.actionConnect_to_server.setText(QCoreApplication.translate("Application", u"Connect to server", None))
#if QT_CONFIG(shortcut)
        self.actionConnect_to_server.setShortcut(QCoreApplication.translate("Application", u"Ctrl+E", None))
#endif // QT_CONFIG(shortcut)
        self.actionDisconnect.setText(QCoreApplication.translate("Application", u"Disconnect", None))
        self.label.setText(QCoreApplication.translate("Application", u"**Station name**", None))
        self.menuGame.setTitle(QCoreApplication.translate("Application", u"Game", None))
        self.menuHelp.setTitle(QCoreApplication.translate("Application", u"Help", None))
    # retranslateUi

