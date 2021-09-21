from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow,self).__init__()

        self.setWindowTitle("Monstro's Bestiary")
        self.setGeometry(100, 200, 1280, 600)
        self.setupMenuBar()

    def setupFileMenuBar(self):
        f = self.fileMenu

        f.clear()
        self.fa = f.addAction("New",self.newConfig, QKeySequence("CTRL+N"))
        self.fc = f.addAction("Open",self.openConfig, QKeySequence("CTRL+O"))

    def setupMenuBar(self):
        mb = self.menuBar()

        self.fileMenu = mb.addMenu("&File")
        self.setupFileMenuBar()

    #menu items def

    def newConfig(self):
        message = QMessageBox.warning(self,"Warning", "what ya trying to do, lol")
    
    def openConfig(self):
         message = QMessageBox.warning(self,"Warning", "open stuff is not done yet")


if __name__ == "__main__":

    app = QApplication(sys.argv)

    mainWindow = MainWindow()

    mainWindow.show()
    sys.exit(app.exec())