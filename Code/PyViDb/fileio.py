# use as logger
# use for settings

import json, os, sys, time

logfile = "auvi.log"
settingfile = "auvi.json"
directory = os.path.dirname(sys.argv[0])+"/" if len(os.path.dirname(sys.argv[0]))>0 else ""

def getSettingObj():
    try:
        f = open(directory + settingfile, "r")
        s = json.loads(f.read)
        f.close()
    except:
        f = open(directory + settingfile, "w")
        s = {}
        f.write(json.dumps(s))
        f.close()
    return s

def changeSetting(key, value):
    s = getSettingObj()
    s[key]=value
    writeSettings(s)
    return s

def writeSettings(sobj):
    f = open(directory + settingfile, "w")
    f.write(json.dumps(sobj))
    f.close()

def getSetting(key):
    s = getSettingObj()
    return s[key] # raises KeyError

def main():
    print("generating settings file")
    s = getSettingObj()
    s = changeSetting("dir", directory)
    s = changeSetting("log", logfile)

def log(dest, message):
    g = time.gmtime()
    t = str(g[0])+"/"+str(g[1])+"/"+str(g[2])+" "+str(g[3])+":"+str(g[4])
    l = "[{type:^5}] {time} >> {message}".format(**{"type":dest,"time":t,"message":message})
    f = open(directory + logfile, "a")
    f.write(l+"\n")
    f.close()
    return l

def error(message, prints=True):
    l = log("ERROR", message)
    if prints:
        print(l)
    return l

if __name__ == '__main__':
    main()
