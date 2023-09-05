infile = open("advent of code 2022/input_day19.txt", "r")
#totals = [ore, clay, obsidian]
#r, c, b, g
def dectree(orebot, claybot, obsbot, geobot, path, score, totals, maxabove):
    if(len(path)==24):
        return score
    r = 1 + path.count("r")
    c = path.count("c")
    b = path.count("b")
    g = path.count("g")
    newarr = [totals[0]+r, totals[1]+c, totals[2]+b]
    #purchase bots THEN add ores
    p1 = 0
    p2 = 0
    p3 = 0
    p4 = 0
    p5 = 0
    if(totals[0]>geobot[0] and totals[2]>geobot[1]):
        p5 = dectree(orebot, claybot, obsbot, geobot, path+"g", score+g, [newarr[0]-geobot[0], newarr[1], newarr[2]-geobot[1]])
    else:
        if(not(totals[1]==0 and totals[2]==0 and (totals[0]>claybot or totals[0]>orebot))):
            p1 = dectree(orebot, claybot, obsbot, geobot, path+"0", score+g, newarr, max([p1, p2, p3, p4, p5]))
        if(totals[0]>orebot):
            p2 = dectree(orebot, claybot, obsbot, geobot, path+"r", score+g, [newarr[0]-orebot, newarr[1], newarr[2]], max([p1, p2, p3, p4, p5]))
        if(totals[0]>claybot):
            p3 = dectree(orebot, claybot, obsbot, geobot, path+"c", score+g, [newarr[0]-claybot, newarr[1], newarr[2]], max([p1, p2, p3, p4, p5]))
        if(totals[0]>obsbot[0] and totals[1]>obsbot[1]):
            p4 = dectree(orebot, claybot, obsbot, geobot, path+"b", score+g, [newarr[0]-obsbot[0], newarr[1]-obsbot[1], newarr[2]], max([p1, p2, p3, p4, p5]))
    return max([p1, p2, p3, p4, p5])
total = 0
for line in infile:
    pieces = line.split(" ")
    blueprint = int(pieces[1][0:pieces[1].index(":")])
    orebot = int(pieces[6])
    claybot = int(pieces[12])
    obsbot = [int(pieces[18]), int(pieces[21])]
    geobot = [int(pieces[27]), int(pieces[30])]
    geodesproduced = dectree(orebot, claybot, obsbot, geobot, "", 0, [0, 0, 0], 0)
    total+= blueprint*geodesproduced
print(total)