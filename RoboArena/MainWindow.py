import sys

import PyQt5
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QSizePolicy
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import QImage,QPalette,QBrush

from ArenaButton import ArenaButton
from PlayWindow import PlayWindow



class Window(QWidget):

    def __init__(self,windowWidth,windowHeight):
        self.windowwidth = windowWidth
        self.windowHeight = windowHeight
        super().__init__()
        self.initUI()

    def initUI(self):
        exitbutton = ArenaButton("exitbutton","exit",self)
        playbutton = ArenaButton("playbutton","play", self)
        settingbutton = ArenaButton("settingbutton","setting", self)
        playbutton.clicked.connect(self.PlayWindowcall)
        exitbutton.clicked.connect(QtCore.QCoreApplication.instance().quit)

        self.l1 = QLabel('Robo Arena',self)
        self.l1.setStyleSheet(
            "font-size:100px;"
            "font-style: oblique;"
            "font-weight: 900;"
            "font-variant: small-caps;"
            "color:black;"
        )
        self.l1.setAlignment(QtCore.Qt.AlignCenter)


        oImage = QImage("backgroundimage.jpg")
        sImage = oImage.scaled(QSize(self.windowwidth, self.windowHeight))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)

        self.setFixedSize(self.windowwidth,self.windowHeight)
        self.setWindowTitle("Robo-Arena-Team")
        self.show()

    def PlayWindowcall(self):
        self.w = PlayWindow(1500, 1100)
        self.hide()






app = QApplication(sys.argv)
w = Window(1500,1100)

sys.exit(app.exec_())


