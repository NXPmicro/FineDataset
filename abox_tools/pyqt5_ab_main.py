# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './abox_tools/pyqt5_ab_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1409, 912)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.fraConsole = QtWidgets.QGroupBox(self.centralwidget)
        self.fraConsole.setGeometry(QtCore.QRect(980, 140, 421, 681))
        self.fraConsole.setObjectName("fraConsole")
        self.btnValidate = QtWidgets.QPushButton(self.fraConsole)
        self.btnValidate.setGeometry(QtCore.QRect(190, 640, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.btnValidate.setFont(font)
        self.btnValidate.setObjectName("btnValidate")
        self.btnValidateRandom = QtWidgets.QPushButton(self.fraConsole)
        self.btnValidateRandom.setGeometry(QtCore.QRect(100, 640, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.btnValidateRandom.setFont(font)
        self.btnValidateRandom.setObjectName("btnValidateRandom")
        self.btnApplyABCfg = QtWidgets.QPushButton(self.fraConsole)
        self.btnApplyABCfg.setGeometry(QtCore.QRect(10, 640, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.btnApplyABCfg.setFont(font)
        self.btnApplyABCfg.setObjectName("btnApplyABCfg")
        self.lblMain = QtWidgets.QLabel(self.centralwidget)
        self.lblMain.setGeometry(QtCore.QRect(10, 10, 961, 841))
        self.lblMain.setFrameShape(QtWidgets.QFrame.Box)
        self.lblMain.setObjectName("lblMain")
        self.btnDrawABs = QtWidgets.QPushButton(self.centralwidget)
        self.btnDrawABs.setGeometry(QtCore.QRect(990, 10, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.btnDrawABs.setFont(font)
        self.btnDrawABs.setObjectName("btnDrawABs")
        self.sldABsToDraw = QtWidgets.QSlider(self.centralwidget)
        self.sldABsToDraw.setGeometry(QtCore.QRect(1110, 10, 211, 22))
        self.sldABsToDraw.setMinimum(1)
        self.sldABsToDraw.setMaximum(1600)
        self.sldABsToDraw.setProperty("value", 9)
        self.sldABsToDraw.setOrientation(QtCore.Qt.Horizontal)
        self.sldABsToDraw.setObjectName("sldABsToDraw")
        self.btnCluster = QtWidgets.QPushButton(self.centralwidget)
        self.btnCluster.setGeometry(QtCore.QRect(1330, 10, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btnCluster.setFont(font)
        self.btnCluster.setObjectName("btnCluster")
        self.pgsBar = QtWidgets.QProgressBar(self.centralwidget)
        self.pgsBar.setGeometry(QtCore.QRect(970, 860, 118, 23))
        self.pgsBar.setProperty("value", 24)
        self.pgsBar.setObjectName("pgsBar")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(1290, 60, 26, 16))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.cmbSubSet = QtWidgets.QComboBox(self.centralwidget)
        self.cmbSubSet.setGeometry(QtCore.QRect(1320, 60, 81, 20))
        self.cmbSubSet.setObjectName("cmbSubSet")
        self.btnLoadDataset = QtWidgets.QPushButton(self.centralwidget)
        self.btnLoadDataset.setGeometry(QtCore.QRect(990, 90, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btnLoadDataset.setFont(font)
        self.btnLoadDataset.setObjectName("btnLoadDataset")
        self.btnDSFolder = QtWidgets.QPushButton(self.centralwidget)
        self.btnDSFolder.setGeometry(QtCore.QRect(990, 50, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnDSFolder.setFont(font)
        self.btnDSFolder.setObjectName("btnDSFolder")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(1100, 60, 26, 16))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.cmbDSType = QtWidgets.QComboBox(self.centralwidget)
        self.cmbDSType.setGeometry(QtCore.QRect(1132, 60, 141, 20))
        self.cmbDSType.setObjectName("cmbDSType")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(1270, 110, 45, 16))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.cmbIoUThd = QtWidgets.QComboBox(self.centralwidget)
        self.cmbIoUThd.setGeometry(QtCore.QRect(1322, 110, 69, 20))
        self.cmbIoUThd.setObjectName("cmbIoUThd")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1409, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menuA_test = QtWidgets.QMenu(self.menubar)
        self.menuA_test.setObjectName("menuA_test")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menu_ClusterCfg = QtWidgets.QAction(MainWindow)
        self.menu_ClusterCfg.setObjectName("menu_ClusterCfg")
        self.menuSaveABSettingsAs = QtWidgets.QAction(MainWindow)
        self.menuSaveABSettingsAs.setObjectName("menuSaveABSettingsAs")
        self.menuLoadABSettings = QtWidgets.QAction(MainWindow)
        self.menuLoadABSettings.setObjectName("menuLoadABSettings")
        self.menuSaveABSettings = QtWidgets.QAction(MainWindow)
        self.menuSaveABSettings.setObjectName("menuSaveABSettings")
        self.menuShowRandom = QtWidgets.QAction(MainWindow)
        self.menuShowRandom.setObjectName("menuShowRandom")
        self.menuDSFolder = QtWidgets.QAction(MainWindow)
        self.menuDSFolder.setObjectName("menuDSFolder")
        self.menuStatAboxMatching = QtWidgets.QAction(MainWindow)
        self.menuStatAboxMatching.setObjectName("menuStatAboxMatching")
        self.menuShowAt = QtWidgets.QAction(MainWindow)
        self.menuShowAt.setObjectName("menuShowAt")
        self.menu.addAction(self.menuSaveABSettings)
        self.menu.addAction(self.menuSaveABSettingsAs)
        self.menu.addAction(self.menuLoadABSettings)
        self.menu.addSeparator()
        self.menu.addAction(self.menuDSFolder)
        self.menuA_test.addAction(self.menu_ClusterCfg)
        self.menuA_test.addAction(self.menuStatAboxMatching)
        self.menu_2.addAction(self.menuShowRandom)
        self.menu_2.addAction(self.menuShowAt)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menuA_test.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "锚框设计与验证工具"))
        self.fraConsole.setTitle(_translate("MainWindow", "各特征图上的锚框配置"))
        self.btnValidate.setText(_translate("MainWindow", "再次验证"))
        self.btnValidateRandom.setText(_translate("MainWindow", "随机验证"))
        self.btnApplyABCfg.setText(_translate("MainWindow", "应用配置"))
        self.lblMain.setText(_translate("MainWindow", "TextLabel"))
        self.btnDrawABs.setText(_translate("MainWindow", "绘制部分锚框"))
        self.btnCluster.setText(_translate("MainWindow", "边框聚类"))
        self.label_15.setText(_translate("MainWindow", "子集"))
        self.btnLoadDataset.setText(_translate("MainWindow", "装载"))
        self.btnDSFolder.setText(_translate("MainWindow", "数据集目录..."))
        self.label_13.setText(_translate("MainWindow", "类型"))
        self.label_14.setText(_translate("MainWindow", "匹配IoU"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menuA_test.setTitle(_translate("MainWindow", "工具"))
        self.menu_2.setTitle(_translate("MainWindow", "测试"))
        self.menu_ClusterCfg.setText(_translate("MainWindow", "边框聚类..."))
        self.menu_ClusterCfg.setShortcut(_translate("MainWindow", "Ctrl+T"))
        self.menuSaveABSettingsAs.setText(_translate("MainWindow", "锚框设置另存为..."))
        self.menuSaveABSettingsAs.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.menuLoadABSettings.setText(_translate("MainWindow", "读取锚框配置..."))
        self.menuLoadABSettings.setShortcut(_translate("MainWindow", "Ctrl+L"))
        self.menuSaveABSettings.setText(_translate("MainWindow", "保存锚框配置"))
        self.menuSaveABSettings.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.menuShowRandom.setText(_translate("MainWindow", "Show Random"))
        self.menuDSFolder.setText(_translate("MainWindow", "Select dataset folder"))
        self.menuStatAboxMatching.setText(_translate("MainWindow", "统计锚框匹配情况"))
        self.menuShowAt.setText(_translate("MainWindow", "Show specified index"))
