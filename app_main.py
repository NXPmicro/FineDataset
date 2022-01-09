import sys
from PyQt5 import QtGui, QtCore
import PyQt5
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QCheckBox, QWidget, QApplication, QMainWindow, QMessageBox, QStatusBar, QFileDialog
from PyQt5.QtCore import Qt
import widertools
import json
import os.path as path
import os
import numpy as np
import widerface2voc as w2v
import time
import shutil
import wf_utils
import crowdhuman_utils as ch_utils
import voc_utils
from patcher import DelTree
import patcher
class MainAppLogic():
    def __init__(self, ui:widertools.Ui_MainWindow, mainWindow):
        self.ui = ui
        self.mainWindow = mainWindow
        self.oriImage = ''
        self.dsFolder = ''
        self.nextDSFolder = ''
        self.isToAbort = False
        ui.cmbDSType.addItems(['wider_face', 'crowd_human', 'voc', 'coco'])
        ui.cmbDSType.setCurrentIndex(0)
        ui.cmbSubSet.addItems(['train','val', 'any'])
        ui.cmbMaxFacesPerCluster.addItems(['10', '9', '8', '7', '6','5', '4', '3', '2'])
        #ui.cmbMinCloseRate.addItems(['0.5', '0.4', '0.32', '0.25', '0.2', '0.16', '0.125', '0.1', '0.08'])
        #ui.cmbMinCloseRate.setCurrentIndex(3)
        
        def CalcCmbValues(minVal, maxVal, step, isSquare=False):
            curVal = maxVal
            lstRet = []
            while curVal >= minVal:
                if isSquare:
                    outVal = curVal**0.5 * 100
                    sUnit = '% ^2'
                else:
                    outVal = curVal * 100
                    sUnit = '%'
                curVal /= step
                strVal = '%0.5f' % (outVal)
                lstRet.append(strVal[:4] + sUnit)
            return lstRet

        ui.cmbMinAreaRate.addItems(CalcCmbValues(0.00008, 0.99, 2**0.5, True))
        ui.cmbMaxAreaRate.addItems(CalcCmbValues(0.00008, 0.99, 2**0.5, True))
        ui.cmbMinCloseRate.addItems(CalcCmbValues(0.01, 0.6, 1.25, False))
        ui.cmbMinAreaRate.setCurrentIndex(12)
        ui.cmbMaxAreaRate.setCurrentIndex(2)
        ui.cmbMinCloseRate.setCurrentIndex(5)
        #ui.cmbSubSet.currentIndexChanged.connect(lambda: LoadDataset(ui))
        self.SetEnableStateBaseedOnDatasetAvailibiblity(False)
        def _SetAbort(self):
            self.isToAbort = True
        ui.btnAbort.clicked.connect(lambda: _SetAbort(self))
        ui.btnAbort.setEnabled(False)
        ui.btnForceLoadDS.clicked.connect(lambda: self.LoadDataset(self.nextDSFolder))
        ui.cmbSubSet.textActivated.connect(lambda: self.LoadDataset(self.nextDSFolder))
        #ui.cmbSubSet.highlighted.connect(lambda: LoadDataset(ui)) 
        ui.btnRandom.clicked.connect(self.OnClicked_Random)
        ui.btnGenSingleFaceDataSet.clicked.connect(self.OnClicked_GenSingleFaceDataset)
        ui.btnValidateSingleFaceDataSet.clicked.connect(self.OnClicked_ValidateSingleFaceDataset)
        ui.btnValidateMultiFaceDataSet.clicked.connect(self.OnClicked_ValidateMultiFaceDataset) 
        ui.btnOriImg.clicked.connect(self.OnClicked_OriImage)       
        ui.btnGenMultiFaceDataSet.clicked.connect(self.OnClicked_GenMultiFaceDataset)
        ui.btnTagSelAll.clicked.connect(self.OnClicked_TagSelAll)
        ui.btnTagSelInv.clicked.connect(self.OnClicked_TagSelInv)        
        ui.btnDSFolder.clicked.connect(self.OnClicked_DSFolder)
        ui.btnToVoc.clicked.connect(self.OnClicked_ToVOC)
        ui.pgsBar.setVisible(False)
        ui.tmrToHidePgsBar = QtCore.QTimer(self.mainWindow)
        ui.tmrToHidePgsBar.setInterval(300)
        ui.tmrToHidePgsBar.setSingleShot(True)
        ui.tmrToHidePgsBar.timeout.connect(self.OnTimeout_tmrToHidePgsBar)
        ui.statusBar = QStatusBar()
        mainWindow.setStatusBar(ui.statusBar)
        ui.statusBar.addPermanentWidget(ui.pgsBar)
        #ui.btnValidateMultiFaceDataSet.clicked.connect(self.OnClicked_ValidateSingleFaceDataset)

        # ui.btnGenMultiFaceDataSet.setEnabled(False)
        # ui.btnValidateMultiFaceDataSet.setEnabled(False)
        # ui.cmbMaxFacesPerCluster.setEnabled(False)
        ui.btnSaveOriBBoxes.clicked.connect(self.OnClicked_SaveOriBBoxes)
        self.patchNdx = 0
        self.lstPatches = []
        self.strOutFolder = ''
        self.chkTags = []
        self.nextDSFolder = 'q:/datasets/wider_face'
        #if ui.chkAutoload.isChecked():
        #    self.LoadDataset('q:/datasets/wider_face')

    def SetEnableStateBaseedOnDatasetAvailibiblity(self,isEn):
            self.ui.btnRandom.setEnabled(isEn)
            self.ui.btnSaveOriBBoxes.setEnabled(isEn)
            self.ui.btnGenSingleFaceDataSet.setEnabled(isEn)
            self.ui.btnGenMultiFaceDataSet.setEnabled(isEn) 
            
            self.ui.btnTagSelAll.setEnabled(isEn)
            self.ui.btnTagSelInv.setEnabled(isEn)
            self.ui.btnValidateSingleFaceDataSet.setEnabled(isEn)
            self.ui.btnValidateMultiFaceDataSet.setEnabled(isEn)
            self.ui.btnOriImg.setEnabled(isEn)        

    def OnTimeout_tmrToHidePgsBar(self):
        self.ui.pgsBar.setVisible(False)

    def ShowImage(self, table, strKey):
        item = self.dataObj.dctFiles[strKey]
        c = table.shape
        qImg = QtGui.QImage(bytearray(table), c[1], c[0], c[1]*3, QtGui.QImage.Format_BGR888)
        pix = QPixmap(QPixmap.fromImage(qImg))
        
        #pix2 = pix.scaled(32,32, Qt.KeepAspectRatio)#, Qt.SmoothTransformation)
        rect = ui.lblImg.rect()
        pix3 = pix.scaled(rect.width(),rect.height(), Qt.KeepAspectRatio)     #, Qt.SmoothTransformation)   

        
        # ui.imgWnd.setPixmap(pix2)
        ui.lblImg.setPixmap(pix3)

    def OnClicked_ToVOC(self):
        def callback(pgs):
            self.ui.pgsBar.setValue(pgs)
            QApplication.processEvents()
        
        self.ui.pgsBar.setVisible(True)
        for setSel in ['train', 'val', 'test']:
            for cntSel in ['single', 'multi']:
                self.ui.pgsBar.setValue(1)
                self.ui.statusBar.showMessage('正在转换%s %s' % (setSel, cntSel), 60000)
                QApplication.processEvents()
                voc = w2v.WF2VOC(setSel, cntSel)
                voc.MakeVOC(callback=callback)
        self.ui.statusBar.showMessage('转换完成', 5000)
        self.ui.tmrToHidePgsBar.start()

    def OnClicked_SaveOriBBoxes(self):
        self.ui.statusBar.showMessage('正在保存', 60000)
        QApplication.processEvents()
        sOutFile = 'labels_%s.json' % (self.ui.cmbSubSet.currentText())
        with open(sOutFile, 'w') as fd:
            json.dump(self.dataObj.dctFiles, fd, indent=4)
        # QMessageBox.information(None,'box', '已保存到%s' % sOutFile)
        self.ui.statusBar.showMessage('已保存到%s' % sOutFile, 5000)

    def OnClicked_Random(self):
        [table, strKey] = self.dataObj.ShowRandom(False, allowedTags=self.GetAllowedTags())
        self.ShowImage(table, strKey)

    def OnClicked_DSFolder(self):
        dir_choose = QFileDialog.getExistingDirectory(MainWindow,  
                                    "选取文件夹",  
                                    './') # 起始路径

        if dir_choose == "":
            print("\n取消选择")
            return

        print("\n你选择的文件夹为:")
        print(dir_choose)
        self.nextDSFolder = dir_choose
        if self.ui.chkAutoload.isChecked():
            self.LoadDataset(dir_choose)

    def GetNextFreeFolder(self, strPrimary, isReplace=True):
        sTry = strPrimary
        if isReplace == True:
            if path.exists(sTry):
                shutil.rmtree(sTry)
        else:
            ndx = 1
            while path.exists(sTry):
                now = int(time.time())
                #转换为其他日期格式,如:"%Y-%m-%d %H:%M:%S"
                timeArray = time.localtime(now)
                otherStyleTime = time.strftime("%Y-%m-%d-%H-%M-%S", timeArray)            
                sTry = '%s_%s' % (strPrimary, otherStyleTime)
                ndx += 1
        return sTry

    def _StatUsage(self, dbgSkips):
        totalCnt = dbgSkips[0]
        lstReasons = [
            'total candidates ',            
            'total usage rate ',
            'bad aspect ratio ', 
            'not close enough ',
            'object out bound ',
            'object bad size  ',
            'objects too dense',
            'too many patches ',
        ]
        
        useRate = 1
        lstRets = [0,0,0,0,0,0,0,0]
        
        lstRets[0] = totalCnt
        useRate = 1
        for i in range(1, 7):
            lstRets[i+1] = dbgSkips[i] / totalCnt
            useRate -= lstRets[i+1]
        lstRets[1] = useRate
        strOut = lstReasons[0] + ' : ' + str(lstRets[0])
        for i in range(1, 8):
            strOut += '\n' + lstReasons[i] + ' : ' + '%02.1f%%' % (lstRets[i]*100)
        QMessageBox.information(MainWindow, '生成结果统计', strOut)

    def OnClicked_GenMultiFaceDataset(self):
        cnt = len(self.dataObj.dctFiles.keys())
        ndc = np.arange(cnt)
        np.random.shuffle(ndc)
        strOutFolder = './outs/out_%s_multi' % (self.ui.cmbSubSet.currentText())
        strOutFolder = self.GetNextFreeFolder(strOutFolder)
        self.strOutFolder = strOutFolder
        outX = int(self.ui.txtOutX.text())
        outY = int(self.ui.txtOutY.text())        
        self.patchNdx = 0
        self.lstPatches = []
        self.ui.pgsBar.setValue(1)
        self.ui.pgsBar.setVisible(True)        
        dsSize = int(self.ui.txtDatasetSize.text())
        if not path.exists(strOutFolder):
            os.makedirs(strOutFolder)
        maxObjPerCluster = int(self.ui.cmbMaxFacesPerCluster.currentText())
        minAreaRate = (float(self.ui.cmbMinAreaRate.currentText()[:4]) / 100.0) ** 2
        maxAreaRate = (float(self.ui.cmbMaxAreaRate.currentText()[:4]) / 100.0) ** 2  

        minClose = float(self.ui.cmbMinCloseRate.currentText()[:4]) / 100.0
        self.ui.pgsBar.setValue(1)
        self.ui.pgsBar.setVisible(True)
        lstAllowed = self.GetAllowedTags()
        self.ui.tmrToHidePgsBar.stop()
        dbgSkips = [0,0,0,0,0,0,0]
        mainUI.btnAbort.setEnabled(True)
        for ndx in ndc:
            #[table,ndx, strKey] = self.dataObj.ShowImage(ndx, False)
            #self.ShowImage(table, ndx, strKey)
            self.ui.statusBar.showMessage('制作中, 图片%d' % ndx, 3600000)
            self.patchNdx, lstPatches = self.dataObj.CutClusterPatches(strOutFolder, self.patchNdx, ndx=ndx, 
                minCloseRate=minClose, maxObjPerCluster=maxObjPerCluster, 
                areaRateRange=[minAreaRate, maxAreaRate], outSize=[outX, outY], allowedTags=lstAllowed,
                dbgSkips=dbgSkips)
            self.lstPatches += lstPatches
            if self.patchNdx >= dsSize:
                break
            if self.isToAbort:
                self.isToAbort = False
                break            
            pgs = 100 * self.patchNdx / dsSize
            self.ui.pgsBar.setValue(pgs)
            QApplication.processEvents()
            print('%d/%d completed' % (self.patchNdx, dsSize))

        with open('%s/bboxes.json' % strOutFolder, 'w', encoding='utf-8') as fd:
            json.dump(self.lstPatches, fd, indent=4)
        self.ui.pgsBar.setValue(100)
        mainUI.btnAbort.setEnabled(False)
        self.ui.statusBar.showMessage('制作了%d/%d张图片于%s' % (self.patchNdx, dsSize, strOutFolder), 5000)
        self._StatUsage(dbgSkips)
        self.ui.tmrToHidePgsBar.start()
        #self.ui.pgsBar.setVisible(False)

    def OnClicked_GenSingleFaceDataset(self):
        cnt = len(self.dataObj.dctFiles.keys())
        ndc = np.arange(cnt)
        np.random.shuffle(ndc)
        strOutFolder = './outs/out_%s_single' % (self.ui.cmbSubSet.currentText())
        strOutFolder = self.GetNextFreeFolder(strOutFolder)
        self.strOutFolder = strOutFolder
        outX = int(self.ui.txtOutX.text())
        outY = int(self.ui.txtOutY.text())        
        self.patchNdx = 0
        self.lstPatches = []
        minAreaRate = (float(self.ui.cmbMinAreaRate.currentText()[:4]) / 100.0) ** 2
        maxAreaRate = (float(self.ui.cmbMaxAreaRate.currentText()[:4]) / 100.0) ** 2          
        dsSize = int(self.ui.txtDatasetSize.text())
        if not path.exists(strOutFolder):
            os.makedirs(strOutFolder)
        self.ui.pgsBar.setValue(1)
        self.ui.pgsBar.setVisible(True)
        self.ui.tmrToHidePgsBar.stop()
        lstAllowed = self.GetAllowedTags()
        dbgSkips = [0,0,0,0,0,0,0]
        mainUI.btnAbort.setEnabled(True)
        for ndx in ndc:
            #[table,ndx, strKey] = self.dataObj.ShowImage(ndx, False)
            #self.ShowImage(table, ndx, strKey)            
            self.ui.statusBar.showMessage('制作中, 图片%d' % ndx, 3600000)
            self.patchNdx, lstPatches = self.dataObj.CutPatches(
                strOutFolder, self.patchNdx, ndx=ndx, outSize=[outX, outY], 
                areaRateRange=[minAreaRate, maxAreaRate], allowedTags=lstAllowed,
                dbgSkips=dbgSkips)
            self.lstPatches += lstPatches
            if self.patchNdx >= dsSize:
                break
            if self.isToAbort:
                self.isToAbort = False
                break
            pgs = 100 * self.patchNdx / dsSize
            self.ui.pgsBar.setValue(pgs)
            print('%d/%d completed' % (self.patchNdx, dsSize))
            QApplication.processEvents()
        self.ui.pgsBar.setValue(100)
        mainUI.btnAbort.setEnabled(False)  
        with open('%s/bboxes.json' % (strOutFolder), 'w', encoding='utf-8') as fd:
            json.dump(self.lstPatches, fd, indent=4)
        self.ui.statusBar.showMessage('制作了%d/%d张图片于%s' % (self.patchNdx, dsSize, strOutFolder), 5000)
        self._StatUsage(dbgSkips)
        self.ui.tmrToHidePgsBar.start()
        # self.ui.pgsBar.setVisible(False)

    def OnClicked_ValidateDataset(self, strSel='single'):
        strOutFolder = './outs/out_%s_%s' % (self.ui.cmbSubSet.currentText(), strSel)
        table, ndx, item = self.dataObj.ShowRandomValidate(strOutFolder)
        c = table.shape
        qImg = QtGui.QImage(bytearray(table), c[1], c[0], c[1]*3, QtGui.QImage.Format_BGR888)
        pix = QPixmap(QPixmap.fromImage(qImg))

        rect = self.ui.lblImg.rect()
        pix3 = pix.scaled(rect.width(),rect.height(), Qt.KeepAspectRatio)
        # ui.imgWnd.setPixmap(pix2)
        self.ui.lblImg.setPixmap(pix3)
        self.ui.statusBar.showMessage('图片 %s' % item['filename']) 
        
        fileNameNoPath = item['filename'].split('/')[-1]
        [mainName, ext] = path.splitext(fileNameNoPath)
        mainName = '_'.join(mainName.split('_')[:-2])
        fileNameKey = mainName
        self.oriImage = self.dataObj.provider.MapFileKey(fileNameKey)
        bkpt = 0

    def OnClicked_ValidateSingleFaceDataset(self, strSel='single'):
        self.OnClicked_ValidateDataset('single')

    def OnClicked_ValidateMultiFaceDataset(self, strSel='single'):
        self.OnClicked_ValidateDataset('multi')        
    
    def OnClicked_OriImage(self):
        if len(self.oriImage) > 0:
            try:
                [table, strKey] = self.dataObj.ShowImageFile(self.oriImage, False, allowedTags=self.GetAllowedTags())
                self.ShowImage(table, strKey)        
            except:
                self.ui.statusBar.showMessage('未找到图片 %s' % (strKey)) 

    def OnClicked_TagSelAll(self):
        for item in self.chkTags:
            chk = item[0]
            chk.setChecked(True)

    def OnClicked_TagSelInv(self):
        for item in self.chkTags:
            chk = item[0]
            chk.setChecked(not chk.isChecked())

    def GetAllowedTags(self):
        lstTags = []
        for item in self.chkTags:
            chk = item[0]
            if chk.isChecked():
                oriText = chk.text()
                outText = ' :'.join(oriText.split(':')[:-1])[:-1]
                lstTags.append(outText)
        return lstTags
    def LoadDataset(self, dsFolder):
        # QMessageBox.information(None,'box',ui.cmbSubSet.currentText())
        # ui.cmbSubSet.currentData
        def callback(pgs):
            self.ui.pgsBar.setValue(pgs)
            QApplication.processEvents()
        
        self.ui.pgsBar.setValue(1)
        self.ui.pgsBar.setVisible(True)

        lstHvsW_config = [0.1, 10.0] # min, max
        lstNew = []
        for (i, txt) in enumerate([mainUI.txtMinHvsW.text(), mainUI.txtMaxHvsW.text()]):
            divSym = ''
            if ':' in txt:
                divSym = ':'
            elif '/' in txt:
                divSym = '/'
            
            try:
                if divSym != '':
                    lstVals = [float(x.strip()) for x in txt.split(divSym)]
                    valOut = lstVals[0] / lstVals[1]
                else:
                    valOut = float(txt.strip())
                lstNew.append(valOut)
            except:
                pass
        if len(lstNew) == 2 and lstNew[0] < lstNew[1]:
            lstHvsW_config = lstNew
        dctCfg = {
            'minHvsW' : lstHvsW_config[0],
            'maxHvsW' : lstHvsW_config[1]
        }

        provider = None
        dsType = ui.cmbDSType.currentText()
        self.ui.statusBar.showMessage('数据集读取中...')
        QApplication.processEvents()
        try:
            setSel = self.ui.cmbSubSet.currentText()
            if dsType == 'wider_face':
                provider = wf_utils.WFUtils(dsFolder, setSel, dctCfg, callback)
            elif dsType == 'crowd_human':
                provider = ch_utils.CrowdHumanUtils(dsFolder, setSel, dctCfg, callback)
            elif dsType == 'voc':
                provider = voc_utils.VOCUtils(dsFolder, setSel, dctCfg, callback)
        except Exception as e:
            print(e)
            self.ui.statusBar.showMessage('代码错误：\n' + str(e))

        if provider is None or provider.dctFiles is None or provider.dctFiles == {}:
            self.ui.statusBar.showMessage('%s中的数据集无法按%s解析！' % (dsFolder, dsType) )            
        else:
            self.SetEnableStateBaseedOnDatasetAvailibiblity(True)
            self.dsFolder = dsFolder
            self.provider = provider
            _translate = QtCore.QCoreApplication.translate
            MainWindow.setWindowTitle(_translate("MainWindow", "数据集化简分割工具 - 已加载%s类型的数据集于：%s" % (mainUI.cmbDSType.currentText(), self.dsFolder)))            
            self.dataObj = patcher.Patcher(provider)
            self.ui.statusBar.showMessage('数据集%s (%s)读取成功!' % (dsFolder, dsType))
            for item in self.chkTags:
                chk = item[0]
                chk.hide()
                chk.deleteLater()
            self.chkTags = []
            topFiller = QWidget()
            dctTag = self.provider.GetTagDict()
            for (i, tag) in enumerate(list(dctTag.keys())):
                chk = QCheckBox(topFiller)
                chk.setText(tag + ' : %d' % (dctTag[tag]))
                chk.setChecked(True)
                chk.isChecked()                
                self.chkTags.append([chk, chk.text()])
                self.chkTags.sort(key=lambda x:x[1], reverse=False)
            for (i, item) in enumerate(self.chkTags):
                item[0].move(4, 5 + i * 20)
            topFiller.setMinimumSize(100, len(self.chkTags) * 20)
            mainUI.scrollTags.setWidget(topFiller)
        self.ui.pgsBar.setValue(100)
        self.ui.tmrToHidePgsBar.start()
if __name__ == '__main__':
    QApplication.setAttribute(Qt.AA_DisableHighDpiScaling)
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = widertools.Ui_MainWindow()
    ui.setupUi(MainWindow)
    mainUI = ui
    MainWindow.show()
    mainLogic = MainAppLogic(ui, MainWindow)
    app.exec()
    # sys.exit(app.exec_())
