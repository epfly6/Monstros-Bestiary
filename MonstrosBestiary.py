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
        self.xmlText.clear()
        self.xmlText.insertPlainText(ET.tostring(entitiesXML, encoding="unicode"))
        attrs = entitiesXML.attrib

        self.hpBaseBox.setValue(float(attrs["baseHP"]) if "baseHP" in attrs else 0)
        self.hpStageBox.setValue(float(attrs["stageHP"]) if "stageHP" in attrs else 0)
        self.shieldBox.setValue(float(attrs["shieldStrength"]) if "shieldStrength" in attrs else 0)
        self.frictionBox.setValue(float(attrs["friction"]) if "friction" in attrs else 0)
        self.shadowSizeBox.setValue(int(attrs["shadowSize"]) if "shadowSize" in attrs else 0)
        self.portraitBox.setValue(int(attrs["portrait"]) if "portrait" in attrs else 0)

        self.collisionMassBox.setValue(float(attrs["collisionMass"]) if "collisionMass" in attrs else 0)
        self.collisionDamageBox.setValue(float(attrs["collisionDamage"]) if "collisionDamage" in attrs else 0)
        self.collisionRadiusBox.setValue(float(attrs["collisionRadius"]) if "collisionRadius" in attrs else 0)
        self.collisionIntervalBox.setValue(int(attrs["collisionInterval"]) if "collisionInterval" in attrs else 1)
        self.collisionRadiusXMultiBox.setValue(float(attrs["collisionRadiusXMulti"]) if "collisionRadiusXMulti" in attrs else 0)
        self.collisionRadiusYMultiBox.setValue(float(attrs["collisionRadiusYMulti"]) if "collisionRadiusYMulti" in attrs else 0)
        self.gridCollPointsBox.setValue(int(attrs["numGridCollisionPoints"]) if "numGridCollisionPoints" in attrs else 0)
        self.gridCollisionInput.setText(attrs["gridCollision"] if "gridCollision" in attrs else "")

        self.bossCheckBox.setChecked(True if "boss" in attrs and attrs["boss"] == "1" else False)
        self.championCheckBox.setChecked(True if "champion" in attrs and attrs["champion"] == "1" else False)
        self.shutDoorsCheckBox.setChecked(True if "shutdoors" in attrs and attrs["shutdoors"] == "true" else False)
        self.rerollCheckBox.setChecked(True if "reroll" in attrs and attrs["reroll"] == "true" else False)

    def newFile(self):
        self.clearAll()

    def openFile(self):
        self.clearAll()
        fname = QFileDialog.getOpenFileName(None, 'Open entities file', self.filePath, "Entities Config (entities2.xml)")
        self.filePath = fname[0]
        self.currentXml = ET.parse(self.filePath).getroot()
        for child in list(self.currentXml):
            attrs = child.attrib
            self.entitiesList.addItem(attrs["id"] + "." + attrs["variant"] + " " + attrs["name"])

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

       self.hpBaseBox = self.findChild(QDoubleSpinBox, 'hpBaseBox')
       self.hpStageBox = self.findChild(QDoubleSpinBox, 'hpStageBox')
       self.shieldBox = self.findChild(QDoubleSpinBox, 'shieldBox')
       self.frictionBox = self.findChild(QDoubleSpinBox, 'frictionBox')
       self.shadowSizeBox = self.findChild(QSpinBox, 'shadowSizeBox')
       self.portraitBox = self.findChild(QSpinBox, 'portraitBox')
       
       self.collisionMassBox = self.findChild(QDoubleSpinBox, 'collisionMassBox')
       self.collisionDamageBox = self.findChild(QDoubleSpinBox, 'collisionDamageBox')
       self.collisionRadiusBox = self.findChild(QDoubleSpinBox, 'collisionRadiusBox')
       self.collisionIntervalBox = self.findChild(QSpinBox, 'collisionIntervalBox')
       self.collisionRadiusXMultiBox = self.findChild(QDoubleSpinBox, 'collisionRadiusXMultiBox')
       self.collisionRadiusYMultiBox = self.findChild(QDoubleSpinBox, 'collisionRadiusYMultiBox')
       self.gridCollPointsBox = self.findChild(QSpinBox, 'gridCollPointsBox')
       self.gridCollisionInput = self.findChild(QLineEdit, 'gridCollisionInput')

       self.bossCheckBox = self.findChild(QCheckBox,'bossCheckBox')
       self.championCheckBox = self.findChild(QCheckBox,'championCheckBox')
       self.shutDoorsCheckBox = self.findChild(QCheckBox,'shutDoorsCheckBox')
       self.rerollCheckBox = self.findChild(QCheckBox,'rerollCheckBox')

       self.xmlText = self.findChild(QPlainTextEdit, 'xmlText')
       

if __name__ == "__main__":
    app = QApplication(sys.argv)

    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())