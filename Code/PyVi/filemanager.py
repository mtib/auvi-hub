#!/usr/bin/python3
import json
import os
from local import *

OUTPUT_DIR = "output"
WEB_DIR = "web"

loc = []
locpara = []
arepara = []


def getJsonContent(file_name):
    file = open(str(file_name), "r")
    jsc = None
    try:
        jsc = json.load(file)
        print("load: " + str(file_name))
    except Exception as e:
        print("failed to load: " + str(file_name))
    file.close()
    return jsc


def getAuViDir():
    filepath = os.path.realpath(__file__)
    while filepath[len(filepath) - 1] != "/":
        filepath = filepath[:len(filepath) - 1]
    return filepath


def getLoc():
    return getJsonContent(LOCALS_FILE)


def getLocPara():
    return getJsonContent(LOCALS_PARAM_FILE)


def getArePara():
    return getJsonContent(AREA_PARAM_FILE)


def getOutputDirs():
    loc = getJsonContent(LOCALS_FILE)
    locpara = getJsonContent(LOCALS_PARAM_FILE)
    arepara = getJsonContent(AREA_PARAM_FILE)
    folders = []
    folders.append(getAuViDir() + OUTPUT_DIR)
    folders.append(getAuViDir() + WEB_DIR)
    for l in loc:
        folders.append(folders[0] + "/" + str(l[0]))
        for lp in locpara:
            folders.append(folders[0] + "/" + str(l[0]) + "/" + str(lp[1]))
        folders.append(folders[0] + "/" + str(l[0]) + "/plot")
        for ap in arepara:
            folders.append(folders[0] + "/" +
                           str(l[0]) + "/plot/" + str(ap[1]))
    return folders


def createOutputDirs():
    os.system("rm -r " + getAuViDir() + OUTPUT_DIR + " >/dev/null 2>/dev/null")
    for folder in getOutputDirs():
        os.system("mkdir " + folder + " >/dev/null 2>/dev/null")


def moveOutputToWeb(delete=True):
    os.system("rm -r " + getAuViDir() + WEB_DIR + " >/dev/null 2>/dev/null")
    os.system("mkdir " + getAuViDir() + WEB_DIR + " >/dev/null 2>/dev/null")
    if delete:
        os.system("mv -f " + getAuViDir() + OUTPUT_DIR + "/* " +
                  getAuViDir() + WEB_DIR + "/. >/dev/null 2>/dev/null")
    else:
        os.system("cp " + getAuViDir() + OUTPUT_DIR + "/* " +
                  getAuViDir() + WEB_DIR + "/. >/dev/null 2>/dev/null")


def convertToGifs():
    for l in getLoc():
        for p in getArePara():
            print("convert (png to gif) " + l[0] + " " + p[1])
            os.system("convert -delay 20 " + getAuViDir() + OUTPUT_DIR + "/" + l[0] + "/plot/" + p[1] + "/*.jpg " + getAuViDir(
            ) + OUTPUT_DIR + "/" + l[0] + "/plot/" + p[1] + "/" + p[1] + ".gif" + " >/dev/null 2>/dev/null")


def convertGifToMp4(framerate, x, y, delete=False):
    for l in getLoc():
        for p in getArePara():
            print("ffmpeg (gif to mp4) " + l[0] + " " + p[1])
            os.system("ffmpeg -y -v 8 -r " + str(framerate) + " -i " + getAuViDir() + OUTPUT_DIR + "/" + l[0] + "/plot/" + p[
                      1] + "/" + p[1] + ".gif " + getAuViDir() + OUTPUT_DIR + "/" + l[0] + "/plot/" + p[1] + "/" + p[1] + ".mp4")
            if delete:
                os.system("rm " + getAuViDir() + OUTPUT_DIR + "/" +
                          l[0] + "/plot/" + p[1] + "/" + p[1] + ".gif")


def printOutputDirs():
    for folder in getOutputDirs():
        print(folder)


if __name__ == '__main__':
    printOutputDirs()
