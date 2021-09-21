import sys
import xml.etree.ElementTree as ET
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

class MainWindow(QMainWindow):
    mainWindow = None
    filePath = "C:\\"
    currentXml = None


    def clearAll(self):
        self.entitiesList.clear()
        self.currentXml = None

    def loadEntitesValues(self, index):
        entitiesXML = list(self.currentXml)[index]
        attrs = entitiesXML.attrib

        self.shadowSizeBox.setValue(int(attrs["shadowSize"]) if "shadowSize" in attrs else 0)
        self.collisionDamageBox.setValue(float(attrs["collisionDamage"]) if "collisionDamage" in attrs else 0)
        self.collisionRadiusBox.setValue(float(attrs["collisionRadius"]) if "collisionRadius" in attrs else 0)
        self.collisionMassBox.setValue(float(attrs["collisionMass"]) if "collisionMass" in attrs else 0)
        self.frictionBox.setValue(float(attrs["friction"]) if "friction" in attrs else 0)
        self.gridCollPointsBox.setValue(int(attrs["numGridCollisionPoints"]) if "numGridCollisionPoints" in attrs else 0)
        self.hpBaseBox.setValue(float(attrs["baseHP"]) if "baseHP" in attrs else 0)
        self.hpStageBox.setValue(float(attrs["stageHP"]) if "stageHP" in attrs else 0)

    def newFile(self):
        self.clearAll()

    def openFile(self):
        self.clearAll()
        fname = QFileDialog.getOpenFileName(None, 'Open entities file', self.filePath, "Entities Config (*entities2.xml)")
        self.filePath = fname[0]
        self.currentXml = ET.parse(self.filePath).getroot()
        for child in list(self.currentXml):
            attrs = child.attrib
            if attrs["name"]:
                self.entitiesList.addItem(attrs["name"])

    def switchedEntity(self,index):
        self.loadEntitesValues(index)

    def newEntity(self):
        QMessageBox.warning(self,"Warning", "Add Entity")

    def removeEntity(self):
        QMessageBox.warning(self,"Warning", "Remove Entity")

    def __init__(self):
       super(MainWindow,self).__init__()
       uic.loadUi("monstrosinterface.ui",self)

    #attach stuff
       self.newFileButton = self.findChild(QAction, 'actionNew')
       self.newFileButton.triggered.connect(self.newFile)

       self.openFileButton = self.findChild(QAction, 'actionOpen')
       self.openFileButton.triggered.connect(self.openFile)

       self.addEntityButton = self.findChild(QPushButton, 'addEntityButton')
       self.addEntityButton.clicked.connect(self.newEntity)

       self.removeEntityButton = self.findChild(QPushButton, 'removeEntityButton')
       self.removeEntityButton.clicked.connect(self.removeEntity)

       self.entitiesList = self.findChild(QListWidget, 'entitiesList')
       self.entitiesList.currentRowChanged.connect(self.switchedEntity)

       self.shadowSizeBox = self.findChild(QSpinBox, 'shadowSizeBox')
       self.collisionDamageBox = self.findChild(QDoubleSpinBox, 'collisionDamageBox')
       self.collisionRadiusBox = self.findChild(QDoubleSpinBox, 'collisionRadiusBox')
       self.collisionMassBox = self.findChild(QDoubleSpinBox, 'collisionMassBox')
       self.frictionBox = self.findChild(QDoubleSpinBox, 'frictionBox')
       self.gridCollPointsBox = self.findChild(QSpinBox, 'gridCollPointsBox')
       self.hpBaseBox = self.findChild(QDoubleSpinBox, 'hpBaseBox')
       self.hpStageBox = self.findChild(QDoubleSpinBox, 'hpStageBox')
       

if __name__ == "__main__":
    app = QApplication(sys.argv)

    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())