# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widertools.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1380, 901)
        MainWindow.setMinimumSize(QtCore.QSize(1327, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lblImg = QtWidgets.QLabel(self.centralwidget)
        self.lblImg.setGeometry(QtCore.QRect(10, 0, 991, 841))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblImg.sizePolicy().hasHeightForWidth())
        self.lblImg.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(9)
        self.lblImg.setFont(font)
        self.lblImg.setFrameShape(QtWidgets.QFrame.Box)
        self.lblImg.setObjectName("lblImg")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(1010, 220, 351, 151))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(180, 60, 151, 16))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.cmbMaxFacesPerCluster = QtWidgets.QComboBox(self.groupBox)
        self.cmbMaxFacesPerCluster.setGeometry(QtCore.QRect(180, 80, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.cmbMaxFacesPerCluster.setFont(font)
        self.cmbMaxFacesPerCluster.setObjectName("cmbMaxFacesPerCluster")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(220, 120, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.txtDatasetSize = QtWidgets.QLineEdit(self.groupBox)
        self.txtDatasetSize.setGeometry(QtCore.QRect(290, 120, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.txtDatasetSize.setFont(font)
        self.txtDatasetSize.setObjectName("txtDatasetSize")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 120, 51, 16))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.txtOutX = QtWidgets.QLineEdit(self.groupBox)
        self.txtOutX.setGeometry(QtCore.QRect(150, 120, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.txtOutX.setFont(font)
        self.txtOutX.setObjectName("txtOutX")
        self.txtOutY = QtWidgets.QLineEdit(self.groupBox)
        self.txtOutY.setGeometry(QtCore.QRect(60, 120, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.txtOutY.setFont(font)
        self.txtOutY.setObjectName("txtOutY")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(10, 30, 151, 16))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.cmbMinAreaRate = QtWidgets.QComboBox(self.groupBox)
        self.cmbMinAreaRate.setGeometry(QtCore.QRect(150, 30, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.cmbMinAreaRate.setFont(font)
        self.cmbMinAreaRate.setObjectName("cmbMinAreaRate")
        self.cmbMaxAreaRate = QtWidgets.QComboBox(self.groupBox)
        self.cmbMaxAreaRate.setGeometry(QtCore.QRect(250, 30, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.cmbMaxAreaRate.setFont(font)
        self.cmbMaxAreaRate.setObjectName("cmbMaxAreaRate")
        self.cmbMinCloseRate = QtWidgets.QComboBox(self.groupBox)
        self.cmbMinCloseRate.setGeometry(QtCore.QRect(10, 80, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.cmbMinCloseRate.setFont(font)
        self.cmbMinCloseRate.setObjectName("cmbMinCloseRate")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 60, 121, 16))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(130, 120, 16, 20))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.chkAllowMoreObj = QtWidgets.QCheckBox(self.groupBox)
        self.chkAllowMoreObj.setGeometry(QtCore.QRect(250, 80, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.chkAllowMoreObj.setFont(font)
        self.chkAllowMoreObj.setChecked(True)
        self.chkAllowMoreObj.setObjectName("chkAllowMoreObj")
        self.pgsBar = QtWidgets.QProgressBar(self.centralwidget)
        self.pgsBar.setGeometry(QtCore.QRect(750, 870, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(9)
        self.pgsBar.setFont(font)
        self.pgsBar.setProperty("value", 24)
        self.pgsBar.setObjectName("pgsBar")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(1010, 0, 351, 201))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(9)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(220, 30, 31, 16))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.cmbSubSet = QtWidgets.QComboBox(self.groupBox_2)
        self.cmbSubSet.setGeometry(QtCore.QRect(260, 30, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(9)
        self.cmbSubSet.setFont(font)
        self.cmbSubSet.setObjectName("cmbSubSet")
        self.btnDSFolder = QtWidgets.QPushButton(self.groupBox_2)
        self.btnDSFolder.setGeometry(QtCore.QRect(10, 60, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btnDSFolder.setFont(font)
        self.btnDSFolder.setObjectName("btnDSFolder")
        self.cmbDSType = QtWidgets.QComboBox(self.groupBox_2)
        self.cmbDSType.setGeometry(QtCore.QRect(50, 30, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(9)
        self.cmbDSType.setFont(font)
        self.cmbDSType.setObjectName("cmbDSType")
        self.label_13 = QtWidgets.QLabel(self.groupBox_2)
        self.label_13.setGeometry(QtCore.QRect(10, 30, 37, 24))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.btnForceLoadDS = QtWidgets.QPushButton(self.groupBox_2)
        self.btnForceLoadDS.setGeometry(QtCore.QRect(160, 60, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.btnForceLoadDS.setFont(font)
        self.btnForceLoadDS.setObjectName("btnForceLoadDS")
        self.chkAutoload = QtWidgets.QCheckBox(self.groupBox_2)
        self.chkAutoload.setGeometry(QtCore.QRect(240, 70, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(9)
        self.chkAutoload.setFont(font)
        self.chkAutoload.setChecked(True)
        self.chkAutoload.setObjectName("chkAutoload")
        self.btnRandom = QtWidgets.QPushButton(self.groupBox_2)
        self.btnRandom.setGeometry(QtCore.QRect(10, 100, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(9)
        self.btnRandom.setFont(font)
        self.btnRandom.setObjectName("btnRandom")
        self.btnSaveOriBBoxes = QtWidgets.QPushButton(self.groupBox_2)
        self.btnSaveOriBBoxes.setGeometry(QtCore.QRect(230, 100, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(9)
        self.btnSaveOriBBoxes.setFont(font)
        self.btnSaveOriBBoxes.setObjectName("btnSaveOriBBoxes")
        self.txtMinHvsW = QtWidgets.QLineEdit(self.groupBox_2)
        self.txtMinHvsW.setGeometry(QtCore.QRect(230, 140, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.txtMinHvsW.setFont(font)
        self.txtMinHvsW.setObjectName("txtMinHvsW")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(10, 140, 161, 16))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.txtMaxHvsW = QtWidgets.QLineEdit(self.groupBox_2)
        self.txtMaxHvsW.setGeometry(QtCore.QRect(290, 140, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.txtMaxHvsW.setFont(font)
        self.txtMaxHvsW.setObjectName("txtMaxHvsW")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(10, 170, 181, 16))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(9)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.txtMinGTPerImg = QtWidgets.QLineEdit(self.groupBox_2)
        self.txtMinGTPerImg.setGeometry(QtCore.QRect(230, 170, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(9)
        self.txtMinGTPerImg.setFont(font)
        self.txtMinGTPerImg.setObjectName("txtMinGTPerImg")
        self.txtMaxGTPerImg = QtWidgets.QLineEdit(self.groupBox_2)
        self.txtMaxGTPerImg.setGeometry(QtCore.QRect(290, 170, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(9)
        self.txtMaxGTPerImg.setFont(font)
        self.txtMaxGTPerImg.setObjectName("txtMaxGTPerImg")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(1180, 410, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.btnGenSingleFaceDataSet = QtWidgets.QPushButton(self.groupBox_3)
        self.btnGenSingleFaceDataSet.setGeometry(QtCore.QRect(10, 20, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btnGenSingleFaceDataSet.setFont(font)
        self.btnGenSingleFaceDataSet.setObjectName("btnGenSingleFaceDataSet")
        self.btnGenMultiFaceDataSet = QtWidgets.QPushButton(self.groupBox_3)
        self.btnGenMultiFaceDataSet.setGeometry(QtCore.QRect(60, 20, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btnGenMultiFaceDataSet.setFont(font)
        self.btnGenMultiFaceDataSet.setObjectName("btnGenMultiFaceDataSet")
        self.btnAbort = QtWidgets.QPushButton(self.groupBox_3)
        self.btnAbort.setGeometry(QtCore.QRect(120, 20, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.btnAbort.setFont(font)
        self.btnAbort.setObjectName("btnAbort")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(1180, 480, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(10)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.btnValidateMultiFaceDataSet = QtWidgets.QPushButton(self.groupBox_4)
        self.btnValidateMultiFaceDataSet.setGeometry(QtCore.QRect(60, 20, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(9)
        self.btnValidateMultiFaceDataSet.setFont(font)
        self.btnValidateMultiFaceDataSet.setObjectName("btnValidateMultiFaceDataSet")
        self.btnValidateSingleFaceDataSet = QtWidgets.QPushButton(self.groupBox_4)
        self.btnValidateSingleFaceDataSet.setGeometry(QtCore.QRect(10, 20, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(9)
        self.btnValidateSingleFaceDataSet.setFont(font)
        self.btnValidateSingleFaceDataSet.setObjectName("btnValidateSingleFaceDataSet")
        self.btnOriImg = QtWidgets.QPushButton(self.groupBox_4)
        self.btnOriImg.setGeometry(QtCore.QRect(120, 20, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(9)
        self.btnOriImg.setFont(font)
        self.btnOriImg.setObjectName("btnOriImg")
        self.btnToVoc = QtWidgets.QPushButton(self.centralwidget)
        self.btnToVoc.setGeometry(QtCore.QRect(1260, 580, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(9)
        self.btnToVoc.setFont(font)
        self.btnToVoc.setObjectName("btnToVoc")
        self.btnTagSelInv = QtWidgets.QPushButton(self.centralwidget)
        self.btnTagSelInv.setGeometry(QtCore.QRect(1100, 580, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(9)
        self.btnTagSelInv.setFont(font)
        self.btnTagSelInv.setObjectName("btnTagSelInv")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(1010, 400, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.btnTagSelAll = QtWidgets.QPushButton(self.centralwidget)
        self.btnTagSelAll.setGeometry(QtCore.QRect(1010, 580, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(9)
        self.btnTagSelAll.setFont(font)
        self.btnTagSelAll.setObjectName("btnTagSelAll")
        self.scrollTags = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollTags.setGeometry(QtCore.QRect(1010, 420, 161, 151))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        self.scrollTags.setFont(font)
        self.scrollTags.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollTags.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.scrollTags.setWidgetResizable(True)
        self.scrollTags.setObjectName("scrollTags")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 146, 149))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollTags.setWidget(self.scrollAreaWidgetContents)
        self.btnDelNonCheckedTags = QtWidgets.QPushButton(self.centralwidget)
        self.btnDelNonCheckedTags.setGeometry(QtCore.QRect(1010, 620, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(9)
        self.btnDelNonCheckedTags.setFont(font)
        self.btnDelNonCheckedTags.setObjectName("btnDelNonCheckedTags")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1380, 23))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menuBar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menuBar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menuBar)
        self.actiontrain = QtWidgets.QAction(MainWindow)
        self.actiontrain.setObjectName("actiontrain")
        self.menuDbgGenMultiForCurrent = QtWidgets.QAction(MainWindow)
        self.menuDbgGenMultiForCurrent.setObjectName("menuDbgGenMultiForCurrent")
        self.menuSpecifyImageNdx = QtWidgets.QAction(MainWindow)
        self.menuSpecifyImageNdx.setObjectName("menuSpecifyImageNdx")
        self.menuDelNonCheckedTags = QtWidgets.QAction(MainWindow)
        self.menuDelNonCheckedTags.setObjectName("menuDelNonCheckedTags")
        self.menu_2.addAction(self.menuDbgGenMultiForCurrent)
        self.menu_2.addAction(self.menuSpecifyImageNdx)
        self.menu_3.addAction(self.menuDelNonCheckedTags)
        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menu_2.menuAction())
        self.menuBar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.cmbDSType, self.cmbSubSet)
        MainWindow.setTabOrder(self.cmbSubSet, self.btnDSFolder)
        MainWindow.setTabOrder(self.btnDSFolder, self.btnForceLoadDS)
        MainWindow.setTabOrder(self.btnForceLoadDS, self.chkAutoload)
        MainWindow.setTabOrder(self.chkAutoload, self.btnRandom)
        MainWindow.setTabOrder(self.btnRandom, self.btnSaveOriBBoxes)
        MainWindow.setTabOrder(self.btnSaveOriBBoxes, self.txtMinHvsW)
        MainWindow.setTabOrder(self.txtMinHvsW, self.txtMaxHvsW)
        MainWindow.setTabOrder(self.txtMaxHvsW, self.txtMinGTPerImg)
        MainWindow.setTabOrder(self.txtMinGTPerImg, self.txtMaxGTPerImg)
        MainWindow.setTabOrder(self.txtMaxGTPerImg, self.cmbMinAreaRate)
        MainWindow.setTabOrder(self.cmbMinAreaRate, self.cmbMaxAreaRate)
        MainWindow.setTabOrder(self.cmbMaxAreaRate, self.cmbMinCloseRate)
        MainWindow.setTabOrder(self.cmbMinCloseRate, self.cmbMaxFacesPerCluster)
        MainWindow.setTabOrder(self.cmbMaxFacesPerCluster, self.chkAllowMoreObj)
        MainWindow.setTabOrder(self.chkAllowMoreObj, self.txtOutY)
        MainWindow.setTabOrder(self.txtOutY, self.txtOutX)
        MainWindow.setTabOrder(self.txtOutX, self.txtDatasetSize)
        MainWindow.setTabOrder(self.txtDatasetSize, self.scrollTags)
        MainWindow.setTabOrder(self.scrollTags, self.btnGenSingleFaceDataSet)
        MainWindow.setTabOrder(self.btnGenSingleFaceDataSet, self.btnGenMultiFaceDataSet)
        MainWindow.setTabOrder(self.btnGenMultiFaceDataSet, self.btnAbort)
        MainWindow.setTabOrder(self.btnAbort, self.btnValidateSingleFaceDataSet)
        MainWindow.setTabOrder(self.btnValidateSingleFaceDataSet, self.btnValidateMultiFaceDataSet)
        MainWindow.setTabOrder(self.btnValidateMultiFaceDataSet, self.btnOriImg)
        MainWindow.setTabOrder(self.btnOriImg, self.btnTagSelAll)
        MainWindow.setTabOrder(self.btnTagSelAll, self.btnTagSelInv)
        MainWindow.setTabOrder(self.btnTagSelInv, self.btnToVoc)
        MainWindow.setTabOrder(self.btnToVoc, self.btnDelNonCheckedTags)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "数据集化简分割工具"))
        self.lblImg.setText(_translate("MainWindow", "TextLabel"))
        self.groupBox.setTitle(_translate("MainWindow", "子块数据集配置"))
        self.label_2.setText(_translate("MainWindow", "合并到至少几个物体"))
        self.label_5.setText(_translate("MainWindow", "生成数量"))
        self.txtDatasetSize.setText(_translate("MainWindow", "300"))
        self.label_4.setText(_translate("MainWindow", "子块 H"))
        self.txtOutX.setText(_translate("MainWindow", "128"))
        self.txtOutY.setText(_translate("MainWindow", "128"))
        self.label_10.setText(_translate("MainWindow", "单物体面积占比范围"))
        self.label_6.setText(_translate("MainWindow", "物体区域最小占比"))
        self.label_12.setText(_translate("MainWindow", "W"))
        self.chkAllowMoreObj.setText(_translate("MainWindow", "允许更多"))
        self.groupBox_2.setTitle(_translate("MainWindow", "源数据集选择"))
        self.label.setText(_translate("MainWindow", "子集"))
        self.btnDSFolder.setText(_translate("MainWindow", "选择目录..."))
        self.label_13.setText(_translate("MainWindow", "类型"))
        self.btnForceLoadDS.setText(_translate("MainWindow", "装载"))
        self.chkAutoload.setText(_translate("MainWindow", "自动装载"))
        self.btnRandom.setText(_translate("MainWindow", "随机显示"))
        self.btnSaveOriBBoxes.setText(_translate("MainWindow", "导出标注"))
        self.txtMinHvsW.setText(_translate("MainWindow", "1/6"))
        self.label_7.setText(_translate("MainWindow", "边框高/宽的范围"))
        self.txtMaxHvsW.setText(_translate("MainWindow", "6/1"))
        self.label_8.setText(_translate("MainWindow", "每张图中边框个数的范围"))
        self.txtMinGTPerImg.setText(_translate("MainWindow", "1"))
        self.txtMaxGTPerImg.setText(_translate("MainWindow", "50"))
        self.groupBox_3.setTitle(_translate("MainWindow", "生成子块数据集"))
        self.btnGenSingleFaceDataSet.setText(_translate("MainWindow", "单框"))
        self.btnGenMultiFaceDataSet.setText(_translate("MainWindow", "多框"))
        self.btnAbort.setText(_translate("MainWindow", "中止"))
        self.groupBox_4.setTitle(_translate("MainWindow", "验证子块数据集"))
        self.btnValidateMultiFaceDataSet.setText(_translate("MainWindow", "多框"))
        self.btnValidateSingleFaceDataSet.setText(_translate("MainWindow", "单框"))
        self.btnOriImg.setText(_translate("MainWindow", "原图"))
        self.btnToVoc.setText(_translate("MainWindow", "-> VOC tar"))
        self.btnTagSelInv.setText(_translate("MainWindow", "反选"))
        self.label_9.setText(_translate("MainWindow", "类别筛选"))
        self.btnTagSelAll.setText(_translate("MainWindow", "全选"))
        self.btnDelNonCheckedTags.setText(_translate("MainWindow", "删除未选中的类别"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_2.setTitle(_translate("MainWindow", "调试"))
        self.menu_3.setTitle(_translate("MainWindow", "工具"))
        self.actiontrain.setText(_translate("MainWindow", "train"))
        self.menuDbgGenMultiForCurrent.setText(_translate("MainWindow", "Generate Multi-patch dataset for current image"))
        self.menuDbgGenMultiForCurrent.setShortcut(_translate("MainWindow", "Ctrl+D"))
        self.menuSpecifyImageNdx.setText(_translate("MainWindow", "Specify image number"))
        self.menuSpecifyImageNdx.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.menuDelNonCheckedTags.setText(_translate("MainWindow", "Delete non-checked categories"))
