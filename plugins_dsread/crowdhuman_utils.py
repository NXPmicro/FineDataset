# Copyright 2016-2022 NXP
# SPDX-License-Identifier: MIT
import os.path as path
import json
try:
    import abstract_utils
except:
    import plugins_dsread.abstract_utils as abstract_utils
import zipfile
import io
import random
import time

def GetUtilClass():
    return CrowdHumanUtils
def GetDSTypeName():
    return "Crowd Human"
class CrowdHumanUtils(abstract_utils.AbstractUtils):
    def __init__(self, dsFolder = '.', setSel='train', dctCfg = {}, callback=None, maxCnt=50000, isShuffle=True):
        super(CrowdHumanUtils, self).__init__(dsFolder, setSel, dctCfg, callback, maxCnt, isShuffle)
        self.dctFiles = {}
        self.setSel = setSel
        self.dctFile2Zf = {}
        self.lstZfs = []
        self.lstFiles = []
        self.lstAnnos = []
        self.dctTags = {'person':0, 'mask':0}
        self._unsureCnt = 0
        self._ignoreCnt = 0
        self._noHeadCnt = 0
        isSkipDirtyImg = False
        minHvsW, maxHvsW = 0.1, 10.0
        minGTPerImg, maxGTPerImg = 1, 50
        try:
            minHvsW = dctCfg['minHvsW']
            maxHvsW = dctCfg['maxHvsW']
            minGTPerImg = dctCfg['minGTPerImg']
            maxGTPerImg = dctCfg['maxGTPerImg']
            isSkipDirtyImg = dctCfg['isSkipDirtyImg']
        except:
            pass

        lstLines = []
        if setSel == 'any':
            lstSetSel = ['train', 'val', 'test']
        else:
            lstSetSel = [setSel]
        for setSel in lstSetSel:
            print('扫描zip数据集之%s部分' % (setSel))
            sPrefix = dsFolder + '/CrowdHuman_' + setSel
            for i in range(100):
                if i != 0 or setSel != 'val':
                    sZipFile = sPrefix + '{:02}'.format(i + 1) + '.zip'
                else:
                    sZipFile = sPrefix + '.zip'
                if not path.exists(sZipFile):
                    continue
                zf = zipfile.ZipFile(sZipFile)
                self.lstZfs.append(zf)
                for (i, obj) in enumerate(zf.filelist):
                    self.dctFile2Zf[obj.filename] = zf
                    self.lstFiles.append((obj.filename, obj.file_size))
            if len(self.lstFiles) > 0:
                break

        print('共扫描到%d张图片' % (len(self.lstFiles)))
        annoFile = dsFolder + '/annotation_%s.odgt' % (setSel)
        print('读取标注数据')
        with open(annoFile) as fd:
            lstLines = fd.readlines()
            for (i, sLine) in enumerate(lstLines):
                dct = json.loads(sLine)
                self.lstAnnos.append(dct)
        if isShuffle:
            # 根据当前时间产生随机种子
            random.seed(time.time())
            random.shuffle(self.lstAnnos)
        if maxCnt != 0 and len(self.lstAnnos) > maxCnt:
            self.lstAnnos = self.lstAnnos[:maxCnt]
        imgCnt = min(maxCnt, len(self.lstAnnos))
        for i in range(imgCnt):
            if i % 100 == 0:
                if callback is not None:
                    callback(i * 100 / imgCnt)
            dctIn = self.lstAnnos[i]
            lstBBoxes = []
            dctAreas = []
            areaAverage = 0
            for gtIn in dctIn['gtboxes']:
                dirty = 0
                xywh = gtIn['vbox'] # fbox会把遮挡的部分也算进去
                area = xywh[3] * xywh[2] / 100.0
                tag = gtIn['tag']

                # 我们在检测人体，所以滤除过小的
                if xywh[2] == 0:
                    continue
                if xywh[2]  * xywh[3] < 12*12:
                    continue
                aspect = xywh[3]  / xywh[2]
                if aspect < minHvsW or aspect > maxHvsW:
                    dirty = 1
                    if isSkipDirtyImg:
                        lstBBoxes = []
                        break

                dctItem = {
                    'x1' : xywh[0],
                    'y1' : xywh[1],
                    'w': xywh[2],
                    'h': xywh[3],
                    'area': area,
                    'tag': gtIn['tag'],
                    'blur': 0,
                    'isExaggerate': 0,
                    'isOverIllumination': 0,
                    'occlusion' : 0,
                    'pose': 0,
                    'isInvalid' : 0,
                    'dirty': dirty
                }

                areaAverage += area
                if 'head_attr' in gtIn.keys():
                    dctHead = gtIn['head_attr']
                    if 'occ' in dctHead.keys():
                        dctItem['occlusion'] = dctHead['occ']
                    if 'unsure' in dctHead.keys():
                        unsure = dctHead['unsure']
                        dctItem['isInvalid'] |= unsure
                        self._unsureCnt += unsure
                    if 'ignore' in dctHead.keys():
                        ignore = dctHead['ignore']
                        dctItem['isInvalid'] |= ignore
                        self._ignoreCnt += ignore
                else:
                    self._noHeadCnt += 1 
                    print('无head_attr: %s' % (dctIn['ID']))                               
                #if dctItem['occlusion'] != 0:
                #    continue
                lstBBoxes.append(dctItem)
            if len(lstBBoxes) == 0:
                continue
            areaAverage /= len(lstBBoxes)
            # 删除面积过小的
            lstPassed = []
            for dctItem in lstBBoxes:
                #if dctItem['area'] * 3 < areaAverage or dctItem['area'] > areaAverage * 3:
                #    continue
                lstPassed.append(dctItem)
            lstPassed.sort(key=lambda x: x['area'],reverse=True)

            if len(lstPassed) >= minGTPerImg and len(lstPassed) <= maxGTPerImg:
                for xyxy in lstPassed:
                    self.dctTags[xyxy['tag']] += 1
                self.dctFiles['Images/' + dctIn['ID'] + '.jpg'] = {
                    'cnt0' : len(dctIn['gtboxes']),
                    'cnt' : len(lstPassed),
                    'xywhs' : lstPassed
                }
        
        k2 = sorted(self.dctFiles.keys())

        dctRet = {}
        for (i,k) in enumerate(k2):
            dctRet[k] = self.dctFiles[k]
        self.dctFiles = dctRet
        bkpt = 0
        
    def MapFile(self, strFile:str):
        zf = self.dctFile2Zf[strFile]
        fd = zf.open(strFile)
        data = fd.read()
        fd.close()
        ret = io.BytesIO(data)
        return ret

    def GetTagDict(self):
        return self.dctTags
    
    '''
        根据 fileKey反查在 dctFiles中的key
    '''
    def MapFileKey(self, fileKey):
        mapped = 'Images/' + fileKey
        exts = ['.jpg', '.jpeg']
        for ext in exts:
            if mapped + ext in self.dctFiles.keys():
                return mapped + ext
        return ''
if __name__ == '__main__':
    print('Not meant to run as main! done!')

