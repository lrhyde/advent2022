infile = open("advent of code 2022/input_day15.txt", "r")
notbeacon = set()
notbeacon20k = set()
beacons = set()
xsort = []
ysort = []
maxmandis = [0, 0]
possibles = set()
for line in infile:
    pieces = line.split("=")
    xs = int(pieces[1][0:pieces[1].index(",")])
    ys = int(pieces[2][0:pieces[2].index(":")])
    xb = int(pieces[3][0:pieces[3].index(",")])
    yb = int(pieces[4][0:len(pieces[4])])
    mandis = abs(xs-xb) + abs(ys-yb)
    xsort.append((max(0, xs-mandis//2), xs, ys, mandis))
    minx = min(0, xs-mandis)
    miny = min(0, ys-mandis)
    maxx = max(4000000, xs+mandis)
    maxy = max(4000000, ys+mandis)
    print("done")
sensors = xsort.sort()

print(len(notbeacon))