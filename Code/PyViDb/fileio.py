#/usr/bin/python3
# use as logger
# use for settings

import json
import os
import sys
import time
import os.path

logfile = "auvi.log"
settingfile = "auvi.json"
directory = os.path.dirname(
    sys.argv[0]) + "/" if len(os.path.dirname(sys.argv[0])) > 0 else ""


def getSettingObj():
    try:
        f = open(directory + settingfile, "r")
        s = json.loads(f.read())
        f.close()
    except:
        f = open(directory + settingfile, "w")
        s = {}
        f.write(json.dumps(s))
        log("FILES", "creating new settings file")
        f.close()
    return s


def changeSetting(key, value):
    s = getSettingObj()
    s[key] = value
    writeSettings(s)
    return s


def writeSettings(sobj):
    f = open(directory + settingfile, "w")
    f.write(json.dumps(sobj))
    f.close()


def getSetting(key):
    s = getSettingObj()
    return s[key]  # raises KeyError


def log(dest, message):
    g = time.gmtime()
    t = str(g[0]) + "/" + str(g[1]) + "/" + \
        str(g[2]) + " " + str(g[3]) + ":" + str(g[4])
    l = "[{type:^5}] {time} >> {message}".format(
        **{"type": dest, "time": t, "message": message})
    f = open(directory + logfile, "a")
    f.write(l + "\n")
    f.close()
    return l


def error(message, prints=True):
    l = log("ERROR", message)
    if prints:
        print(l)
    return l


def default():
    sqldir = "SQL/"
    cities = "cities.sql"
    changeSetting("sqldir", sqldir)
    changeSetting("citiessql", cities)
    changeSetting("log", logfile)

changeSetting("dir", directory)

if __name__ == '__main__':
    default()
else:
    try:
        # Has a filled JSON file
        s = getSetting("log")
    except:
        # Create new JSON file
        default()
