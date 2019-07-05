# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\code\hellopyqt/menutoolbar.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menuFIle = QtWidgets.QMenu(self.menubar)
        self.menuFIle.setObjectName("menuFIle")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionsave = QtWidgets.QAction(MainWindow)
        self.actionsave.setObjectName("actionsave")
        self.actionnew = QtWidgets.QAction(MainWindow)
        self.actionnew.setObjectName("actionnew")
        self.actionclose = QtWidgets.QAction(MainWindow)
        self.actionclose.setObjectName("actionclose")
        self.menuFIle.addAction(self.actionsave)
        self.menuFIle.addAction(self.actionnew)
        self.menuFIle.addSeparator()
        self.menuFIle.addAction(self.actionclose)
        self.menubar.addAction(self.menuFIle.menuAction())
        self.toolBar.addAction(self.actionsave)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionnew)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFIle.setTitle(_translate("MainWindow", "FIle"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionsave.setText(_translate("MainWindow", "save"))
        self.actionsave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionnew.setText(_translate("MainWindow", "new"))
        self.actionclose.setText(_translate("MainWindow", "close"))

