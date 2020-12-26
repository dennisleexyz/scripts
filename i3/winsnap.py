#!/usr/bin/python3

import i3, sys

if len(sys.argv) < 2:
    print("Usage: %s <left | right | top | bottom>" % sys.argv[0])
    sys.exit(1)

window = i3.filter(nodes=[], focused=True)[0]

if window == []:
    print("Got empty window")
    sys.exit(1)

if "off" in window["floating"]:
    print("Not a floating window")
    sys.exit(1)

x = int(window["geometry"]["x"])
y = int(window["geometry"]["y"])
w = int(window["geometry"]["width"])
h = int(window["geometry"]["height"])

if sys.argv[1] == "left":
    newx = 0
    newy = y
elif sys.argv[1] == "right":
    newx = -w
    newy = y
elif sys.argv[1] == "top":
    newx = x
    newy = 0
elif sys.argv[1] == "bottom":
    newx = x
    newy = -h
else:
    print("Invalid direction specified!")
    sys.exit(1)

i3.command("move", "absolute", "position", str(newx) + " px", str(newy) + " px")
