# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bnpdemo.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BNPDemo(object):
    def setupUi(self, BNPDemo):
        BNPDemo.setObjectName("BNPDemo")
        BNPDemo.resize(705, 442)
        self.centralwidget = QtWidgets.QWidget(BNPDemo)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 30, 131, 21))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(150, 30, 113, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(70, 100, 160, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.button1 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button1.setObjectName("button1")
        self.verticalLayout.addWidget(self.button1)
        self.button2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button2.setObjectName("button2")
        self.verticalLayout.addWidget(self.button2)
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(320, 90, 312, 173))
        self.calendarWidget.setObjectName("calendarWidget")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(90, 300, 541, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(60, 200, 48, 24))
        self.spinBox.setObjectName("spinBox")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(140, 200, 160, 80))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBox = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_2.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.verticalLayoutWidget_2)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout_2.addWidget(self.checkBox_2)
        BNPDemo.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(BNPDemo)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 705, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        BNPDemo.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(BNPDemo)
        self.statusbar.setObjectName("statusbar")
        BNPDemo.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(BNPDemo)
        self.actionOpen.setObjectName("actionOpen")
        self.actionQuit = QtWidgets.QAction(BNPDemo)
        self.actionQuit.setObjectName("actionQuit")
        self.actionCopy = QtWidgets.QAction(BNPDemo)
        self.actionCopy.setObjectName("actionCopy")
        self.actionCut = QtWidgets.QAction(BNPDemo)
        self.actionCut.setObjectName("actionCut")
        self.actionPaste = QtWidgets.QAction(BNPDemo)
        self.actionPaste.setObjectName("actionPaste")
        self.actionSkewer = QtWidgets.QAction(BNPDemo)
        self.actionSkewer.setObjectName("actionSkewer")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionQuit)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addAction(self.actionSkewer)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(BNPDemo)
        QtCore.QMetaObject.connectSlotsByName(BNPDemo)

    def retranslateUi(self, BNPDemo):
        _translate = QtCore.QCoreApplication.translate
        BNPDemo.setWindowTitle(_translate("BNPDemo", "MainWindow"))
        self.label.setText(_translate("BNPDemo", "Enter Name"))
        self.button1.setText(_translate("BNPDemo", "PushButton"))
        self.button2.setText(_translate("BNPDemo", "PushButton"))
        self.checkBox.setText(_translate("BNPDemo", "CheckBox"))
        self.checkBox_2.setText(_translate("BNPDemo", "CheckBox"))
        self.menuFile.setTitle(_translate("BNPDemo", "File"))
        self.menuEdit.setTitle(_translate("BNPDemo", "Edit"))
        self.actionOpen.setText(_translate("BNPDemo", "Open..."))
        self.actionQuit.setText(_translate("BNPDemo", "Quit"))
        self.actionCopy.setText(_translate("BNPDemo", "Copy"))
        self.actionCut.setText(_translate("BNPDemo", "Cut"))
        self.actionPaste.setText(_translate("BNPDemo", "Paste"))
        self.actionSkewer.setText(_translate("BNPDemo", "Skewer"))
