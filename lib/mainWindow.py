# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './lib/mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1025, 697)
        mainWindow.setMinimumSize(QtCore.QSize(900, 650))
        mainWindow.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 5, 4, 3, 2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 0, 0, 1, 16)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 0, 19, 1)
        self.probaLabel = QtWidgets.QLabel(self.centralwidget)
        self.probaLabel.setObjectName("probaLabel")
        self.gridLayout.addWidget(self.probaLabel, 7, 7, 1, 1)
        self.classLabel = QtWidgets.QLabel(self.centralwidget)
        self.classLabel.setObjectName("classLabel")
        self.gridLayout.addWidget(self.classLabel, 6, 7, 1, 1)
        self.buildingLine = QtWidgets.QFrame(self.centralwidget)
        self.buildingLine.setFrameShape(QtWidgets.QFrame.VLine)
        self.buildingLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.buildingLine.setObjectName("buildingLine")
        self.gridLayout.addWidget(self.buildingLine, 5, 6, 3, 1)
        self.idLabel = QtWidgets.QLabel(self.centralwidget)
        self.idLabel.setObjectName("idLabel")
        self.gridLayout.addWidget(self.idLabel, 5, 7, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 3, 4, 1, 1)
        self.sceneLine = QtWidgets.QFrame(self.centralwidget)
        self.sceneLine.setFrameShape(QtWidgets.QFrame.VLine)
        self.sceneLine.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.sceneLine.setObjectName("sceneLine")
        self.gridLayout.addWidget(self.sceneLine, 16, 10, 2, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 8, 3, 2, 12)
        self.validateButton = QtWidgets.QPushButton(self.centralwidget)
        self.validateButton.setObjectName("validateButton")
        self.gridLayout.addWidget(self.validateButton, 10, 4, 1, 11)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 7, 11, 1, 3)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 5, 11, 1, 3)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 1, 15, 19, 1)
        self.boundLabel = QtWidgets.QLabel(self.centralwidget)
        self.boundLabel.setObjectName("boundLabel")
        self.gridLayout.addWidget(self.boundLabel, 16, 7, 1, 1)
        self.boundxValueLabel = QtWidgets.QLabel(self.centralwidget)
        self.boundxValueLabel.setObjectName("boundxValueLabel")
        self.gridLayout.addWidget(self.boundxValueLabel, 16, 11, 1, 1)
        self.boundyValueLabel = QtWidgets.QLabel(self.centralwidget)
        self.boundyValueLabel.setObjectName("boundyValueLabel")
        self.gridLayout.addWidget(self.boundyValueLabel, 17, 11, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem8, 13, 3, 1, 12)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 6, 12, 1, 2)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem10, 15, 4, 3, 2)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem11, 11, 3, 1, 12)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem12, 4, 3, 1, 12)
        self.correctButton = QtWidgets.QPushButton(self.centralwidget)
        self.correctButton.setObjectName("correctButton")
        self.gridLayout.addWidget(self.correctButton, 12, 4, 1, 11)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem13, 18, 1, 1, 14)
        self.helpLogo = QtWidgets.QLabel(self.centralwidget)
        self.helpLogo.setMaximumSize(QtCore.QSize(20, 20))
        self.helpLogo.setText("")
        self.helpLogo.setPixmap(QtGui.QPixmap(":help.png"))
        self.helpLogo.setScaledContents(True)
        self.helpLogo.setObjectName("helpLogo")
        self.gridLayout.addWidget(self.helpLogo, 6, 11, 1, 1)
        self.instanceView = QtWidgets.QGraphicsView(self.centralwidget)
        self.instanceView.setMinimumSize(QtCore.QSize(500, 500))
        self.instanceView.setMaximumSize(QtCore.QSize(1500, 1500))
        self.instanceView.setObjectName("instanceView")
        self.gridLayout.addWidget(self.instanceView, 3, 1, 15, 2)
        self.questionLabel = QtWidgets.QLabel(self.centralwidget)
        self.questionLabel.setObjectName("questionLabel")
        self.gridLayout.addWidget(self.questionLabel, 3, 5, 1, 5)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem14, 15, 8, 3, 2)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(mainWindow)
        self.menuBar.setEnabled(True)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1025, 25))
        self.menuBar.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.menuBar.setDefaultUp(False)
        self.menuBar.setObjectName("menuBar")
        self.fileMenu = QtWidgets.QMenu(self.menuBar)
        self.fileMenu.setObjectName("fileMenu")
        mainWindow.setMenuBar(self.menuBar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.loaderAction = QtWidgets.QAction(mainWindow)
        self.loaderAction.setObjectName("loaderAction")
        self.actionExit = QtWidgets.QAction(mainWindow)
        self.actionExit.setObjectName("actionExit")
        self.fileMenu.addAction(self.loaderAction)
        self.fileMenu.addAction(self.actionExit)
        self.menuBar.addAction(self.fileMenu.menuAction())

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Sgrisner"))
        self.probaLabel.setText(_translate("mainWindow", "Probability"))
        self.classLabel.setText(_translate("mainWindow", "Class"))
        self.idLabel.setText(_translate("mainWindow", "Identifier"))
        self.validateButton.setText(_translate("mainWindow", "Validate"))
        self.boundLabel.setText(_translate("mainWindow", "Scene bounds:"))
        self.boundxValueLabel.setText(_translate("mainWindow", "(xmin, ymin)"))
        self.boundyValueLabel.setText(_translate("mainWindow", "(xmax, ymax)"))
        self.correctButton.setText(_translate("mainWindow", "Correct"))
        self.questionLabel.setText(_translate("mainWindow", "Is this instance well classified?"))
        self.fileMenu.setTitle(_translate("mainWindow", "File"))
        self.loaderAction.setText(_translate("mainWindow", "Open..."))
        self.actionExit.setText(_translate("mainWindow", "Exit"))
