#!/usr/bin/python3
# TODO optional GUI

# python 2.7 < 3
import tkinter as tk
import json
import re
import sys, os
from PIL import Image  # Python Image Library ?
from fileio import log

ospath =  os.path.dirname(sys.argv[0])
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

def plotmap(w=1920, h=-1, s=0):
    if h == -1:
        h = int(w / 16.0 * 9.0)
    img = Image.new("RGB", (w, h), (s, s, s))
    citiesFile = open("import/cities.json", "r")
    cities = json.load(citiesFile)
    length = len(cities)
    coordVal = {"max0": -1, "min0": 1, "max1": -1, "min1": 1}
    reltoVal = {"max0": -1, "min0": 1, "max1": -1, "min1": 1}
    for x in range(length):
        try:
            coord = cityCoords(cities[x])
            relto = [intmap(-1 * coord[1], -180.0, 180.0, float(w), float(0)),
                     intmap(coord[0], -90.0, 90.0, float(h), float(0))]

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

            for point in neighbor(relto):
                img.putpixel((point[0],point[1]), (255,100,100))
        except Exception:
            pass
    try:
        os.mkdir(scriptDir+"gui")
    except FileExistsError:
        pass
    log("GUI", "Created PlotMap (gui/plotmap.png)")
    img.save(scriptDir+"gui/plotmap.png")


def map(value, f1, f2, v1, v2):
    return (value - f1) * (v2 - v1) / (f2 - f1) + v1


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
