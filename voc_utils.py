import tarfile
import os.path as path
import zipfile
import io
import glob
import xmltodict
import xml.dom.minidom
import traceback
import time
def ParseNode(node):
    if node.firstChild == node.lastChild:
        return node.firstChild.nodeValue
    else:
        dct2 = dict()
        for child in node.childNodes:
            keyName = child.localName
            if keyName is None:
                continue
            dct2[keyName] = ParseNode(child)
        return dct2

def Xml2Dict(xmlData):
    dom1=xml.dom.minidom.parseString(xmlData)
    root=dom1.documentElement
    dct = dict()
    for node in root.childNodes:
        if node.nodeType == 3 and node.firstChild is None:
            # 字符串节点
            if node.localName is None:
                # 缩进节点
                continue
        elif node.nodeType == 1:
            # element节点
            key = node.localName
            parsed = ParseNode(node)
            if key in dct.keys():
                if isinstance(dct[key], list):
                    dct[key].append(parsed)
                else:
                    dct[key] = [dct[key], parsed]
            else:
                dct[node.localName] = parsed
    return dct


class VOCUtils():

    def ParseAnno(self, an, dctNewCfg):

        imgWH = [int(an['size']['width']), int(an['size']['height'])]
        imgArea = imgWH[0] * imgWH[1]
        lstXywhs = []
        for obj in an['object']:
            bndBox = obj['bndbox']
            x = int(float(bndBox['xmin']))
            y = int(float(bndBox['ymin']))
            w = int(float(bndBox['xmax'])) - x
            h = int(float(bndBox['ymax'])) - y
            hVSw = h / w
            if hVSw < dctNewCfg['minHvsW'] or hVSw > dctNewCfg['maxHvsW']:
                continue
            self.setTags.add(obj['name'])
            dctItem = {
                'x1' : x,
                'y1' : y,
                'w': w,
                'h': h,
                'tag': obj['name'],
                'blur': 0,
                'difficult' : int(obj['difficult']),
                'isOverIllumination': 0,
                'isAtypicalPose': 1 if obj['pose'] != 'Frontal' else 0,
                'isInvalid' : 0,
            }
            if 'truncated' in obj.keys():
                dctItem['occlusion'] = int(obj['truncated'])
            else:
                dctItem['occlusion'] = 0
            lstXywhs.append(dctItem)
        return lstXywhs

    def __init__(self, dsFolder = '.', setSel='train', dctCfg={}):
        self.dsFolder = dsFolder
        self.setTags = set()
        self.dctFiles = dict()
        self.setSel = setSel
        self.dctCfg = {}
        self.isTarMode = True
        self.tarRoots = []
        minHvsW, maxHvsW = 0.1, 10.0
        try:
            minHvsW = dctCfg['minHvsW']
            maxHvsW = dctCfg['maxHvsW']
        except:
            pass
        dctNewCfg = {
            'minHvsW' : minHvsW,
            'maxHvsW' : maxHvsW
        }
        t1 = time.time()
        # 扫描所有数据集
        if path.exists(dsFolder + '/Annotations') and path.exists(dsFolder + '/JPEGImages'):
            self.isTarMode = False
            lstFiles = glob.glob(dsFolder + '/Annotations/*.xml')
            lstFiles = [x.replace('\\', '/') for x in lstFiles]
            for sFile in lstFiles:
                fd = open(sFile)
                an = xmltodict.parse(fd.read())['annotation']
                fd.close()
                if isinstance(an['object'],list) == False:
                    an['object'] = [an['object']]
                lstBBoxes = self.ParseAnno(an, dctNewCfg)
                if len(lstBBoxes) > 0:
                    fileKey = path.splitext(path.split(sFile)[-1])[0]
                    self.dctFiles[fileKey] = {
                        'cnt0' : len(an['object']),
                        'cnt' : len(lstBBoxes),
                        'xywhs' : lstBBoxes
                    }

        else:
            # 扫描所有符合setSel要求的VOC tar文件
            lstFiles = list(set(glob.glob('%s/*voc*.tar' % (dsFolder))).union(glob.glob('%s/*VOC*.tar' % (dsFolder))))
            if len(lstFiles) == 0:
                lstFiles = list(set(glob.glob('%s/*.tar' % (dsFolder))).union(glob.glob('%s/*.tar' % (dsFolder))))                
            if setSel != 'any':
                lstFiles = list(filter(lambda x: setSel in x, lstFiles))
            lstFiles = [ x.replace('\\', '/') for x in lstFiles ]
            self.lstTars = [tarfile.open(x) for x in lstFiles]
            if len(self.lstTars) == 0:
                return
            try:
                for (tarNdx, tar) in enumerate(self.lstTars):
                    lstTarInfos = tar.getmembers()
                    #查前缀
                    for info in lstTarInfos:
                        if info.name[-3:] == 'jpg':
                            self.tarRoots.append(path.split(info.name)[0])
                            break                
                    for info in lstTarInfos:
                        if info.name[-3:] == 'xml':
                            fd = tar.extractfile(info)
                            datBlock = fd.read()
                            an = xmltodict.parse(datBlock)['annotation']                            
                            #an = Xml2Dict(datBlock)
                            fd.close()
                            if isinstance(an['object'],list) == False:
                                an['object'] = [an['object']]
                            lstBBoxes = self.ParseAnno(an, dctNewCfg)
                            if len(lstBBoxes) > 0:
                                fileKey = '{:02}_'.format(tarNdx) + info.name.split('/')[-1][:-4]
                                self.dctFiles[fileKey] = {
                                    'cnt0' : len(an['object']),
                                    'cnt' : len(lstBBoxes),
                                    'xywhs' : lstBBoxes
                                }
            except Exception as e:
                print(e)
                traceback.print_exc()
                raise e
        t2 = time.time()
        dt = (t2 - t1)
        bkpt = 0
        
    def MapFile(self, strFileKey:str):
        if self.isTarMode:
            ndx = int(strFileKey[:2])
            strFileKey = strFileKey[3:]
            tarf = self.lstTars[ndx]
            strFile = self.tarRoots[ndx] + '/' + strFileKey + '.jpg'
            fd = tarf.extractfile(strFile)        
            data = fd.read()
            fd.close()
            ret = io.BytesIO(data)
        else:
            ret = self.dsFolder + '/JPEGImages/' + strFileKey + '.jpg'
        return ret

        sFilePath = self.dctFileKeyMapper[strFile]
        if path.exists(sFilePath):
            return sFilePath
        if self.zfDataFile is not None:
            self.zfDataFile = zipfile('%s/WIDER_%s.zip' % (self.dsFolder, self.setSel))
        fd = self.zfDataFile.open(strFile)
        data = fd.read()
        fd.close()
        ret = io.BytesIO(data)
        return ret        

    
    def GetTagSet(self):
        return self.setTags

    '''
        根据 fileKey反查在 dctFiles中的key
    '''
    def MapFileKey(self, fileKey):
        if fileKey in self.dctFiles.keys():
            return fileKey
        return ''
if __name__ == '__main__':
    import patcher
    obj = patcher.Patcher(VOCUtils(dsFolder = 'Q:/gitrepos',setSel='any'))
    print(len(obj.dctFiles))
    obj.ShowClusterRandom()
    print('done!')

