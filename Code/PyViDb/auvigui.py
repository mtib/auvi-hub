#!/usr/bin/python3
# TODO optional GUI

# python 2.7 < 3
import tkinter as tk
import json
import re
import sys
import os
from PIL import Image, ImageDraw  # Python Image Library ?
from fileio import log
import math

ospath = os.path.dirname(sys.argv[0])
scriptDir = ospath + "/" if len(ospath) else ""


def main():
    root = tk.Tk()
    components(root)
    root.mainloop()


def components(frame):
    quit = tk.Button(frame)
    quit["text"] = "Generate PlotMap"
    quit["fg"] = "red"
    quit["command"] = plotmapButton
    quit.pack({"side": "left"})

    global label
    label = tk.Label(frame)
    label["text"] = "<--- try!"
    label.pack({"side": "right"})


def plotmapButton():
    label["text"] = "You did it!"
    plotmap()


def plotmap(w=1920, h=-1, s=0, connect=False, connectfact=150):
    if h == -1:
        h = int(w / 16.0 * 9.0)
    img = Image.new("RGB", (w, h), (s, s, s))
    draw = ImageDraw.Draw(img)
    citiesFile = open("import/cities.json", "r")
    cities = json.load(citiesFile)
    length = len(cities)
    debug = False
    if debug:
        coordVal = {"max0": -1, "min0": 1, "max1": -1, "min1": 1}
        reltoVal = {"max0": -1, "min0": 1, "max1": -1, "min1": 1}

    lines = 0
    for x in range(length):
        try:
            coord = cityCoords(cities[x])
            relto = [intmap(-1 * coord[1], -180.0, 180.0, float(w), float(0)),
                     intmap(coord[0], -90.0, 90.0, float(h), float(0))]
            if debug:
                if coord[0] > coordVal["max0"]:
                    coordVal["max0"] = coord[0]
                if coord[0] < coordVal["min0"]:
                    coordVal["min0"] = coord[0]
                if coord[1] > coordVal["max1"]:
                    coordVal["max1"] = coord[1]
                if coord[1] < coordVal["min1"]:
                    coordVal["min1"] = coord[1]

                if relto[0] > reltoVal["max0"]:
                    reltoVal["max0"] = relto[0]
                if relto[0] < reltoVal["min0"]:
                    reltoVal["min0"] = relto[0]
                if relto[1] > reltoVal["max1"]:
                    reltoVal["max1"] = relto[1]
                if relto[1] < reltoVal["min1"]:
                    reltoVal["min1"] = relto[1]

            if connect:
                fact = connectfact # smaller = more!
                mindist = dist([w,h],[0,0])/fact
                for y in range(x, length):
                    ndcoord = cityCoords(cities[y])
                    ndrelto = [intmap(-1 * ndcoord[1], -180.0, 180.0, float(w), float(0)), intmap(ndcoord[0], -90.0, 90.0, float(h), float(0))]
                    if dist(relto, ndrelto) < mindist:
                        print("Point {:>5x}x{:<5x} == {:7.2%}".format(x,y,math.sqrt(x+(y/length))/math.sqrt(length+1)))
                        draw.line( (relto[0], relto[1], ndrelto[0], ndrelto[1]) ,fill="rgb(0, 255, 23)")
                        lines += 1
            for point in neighbor(relto):
                img.putpixel((point[0], point[1]), (255, 100, 100))
        except Exception:
            pass
    try:
        print("Lines:  {:>6}".format(lines))
        print("Cities: {:>6}".format(length))
        print("L/C:    {:>6}".format(int(lines/length))
        print("ConF:   {:>6}".format(connectfact))
        log("GEN", "Plotmat: l={:} c={:} l/c={:} cf={:}".format(lines,length,int(lines/length),connectfact))
    except Exception:
        pass
    try:
        os.mkdir(scriptDir + "gui")
    except FileExistsError:
        pass
    log("GUI", "Created PlotMap (gui/plotmap.png)")
    del draw
    img.save(scriptDir + "gui/plotmap.png")

def dist(p1, p2):
    return math.sqrt(math.pow(p1[0]-p2[0],2)+math.pow(p1[1]-p2[1],2))

def map(value, f1, f2, v1, v2):
    return (value - f1) * (v2 - v1) / (f2 - f1) + v1

def realDist(p1,p2,w,h):
    # TODO implement this in plotmap()..
    uw = 40075e3 # [m]
    dl = dist((0,0),(w,h)) # [p]
    dr = dist((0,0),(uw,uw/2)) # [m]
    # dl [p] = dr [m]
    # m = d * dl/dr [p * m/p]
    dp = dist(p1,p2) # [p]
    print(str(dr/dl)+ " Meter/Pixel")
    rl = dp * dr/dl
    return rl


def intmap(value, f1, f2, v1, v2):
    return int(map(float(value), float(f1), float(f2), float(v1), float(v2)))

# For generating the Map Plot


def cityCoords(city):
    point = city["coordinates_wkt"]
    coord = re.findall("[-]{0,1}[0-9]{1,3}\.[0-9]{0,}", point)
    coord = [float(coord[1]), float(coord[0])]
    return coord


def neighbor(point):
    neighbors = []
    for x in [-1, 0, 1]:
        for y in [-1, 0, 1]:
            if (x == y) or (x == -y):
                continue
            neighbors.append([point[0] + x, point[1] + y])
    return neighbors

if __name__ == '__main__':
    main()
