import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage,QPalette,QBrush

from ArenaButton import ArenaButton
class ArenaWindow(QWidget):
    def __init__(self, windowWidth, windowHeight):
         self.windowwidth = windowWidth
         self.windowHeight = windowHeight
         super().__init__()
         self.initPlayWindow()

    def initPlayWindow(self):
        self.l1 = QLabel('Hier kommt dann die Arena', self)
        self.l1.move(0,0)
        self.l1.setStyleSheet(
            "font-size:100px;"
            "color:red;"
        )
        self.setFixedSize(self.windowwidth, self.windowHeight)
        self.setWindowTitle("Robo-Arena-Team")
        self.show()






