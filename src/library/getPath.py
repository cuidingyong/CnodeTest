import os


def getRootPath():
    #获取当前文件目录
    rootpath = os.path.dirname(os.path.abspath(__file__))
    readmepath = os.path.join(os.path.dirname(os.path.dirname(rootpath)),'readme.md')
    while rootpath:
        if(os.path.exists(readmepath)):
            break
        #返回上一级目录
        rootpath = rootpath[0:rootpath.rfind(os.path.sep)]
    rootpath = rootpath[0:rootpath.rfind(os.path.sep)]
    return rootpath


def getDataPath(filename):
    rootpath = getRootPath()
    datapath = os.path.join(rootpath,'data',filename)
    return datapath


def getScreenShotsPath(filename):
    rootpath = getRootPath()
    screenshotspath = os.path.join(rootpath, 'screenshots', filename)
    return screenshotspath


def getUploadPath(filename):
    rootpath = getRootPath()
    uploadpath = os.path.join(rootpath, 'upload', filename)
    return uploadpath


