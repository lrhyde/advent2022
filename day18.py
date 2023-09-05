infile = open("advent of code 2022/input_day18.txt", "r")
xysort = []
yzsort = []
zxsort = []
numitems = 0
for line in infile:
    numitems+=1
    pieces = line.split(",")
    xysort.append((int(pieces[0]), int(pieces[1]), int(pieces[2])))
    yzsort.append((int(pieces[1]), int(pieces[2]), int(pieces[0])))
    zxsort.append((int(pieces[2]), int(pieces[0]), int(pieces[1])))
xysort.sort()
yzsort.sort()
zxsort.sort()
sides = numitems*6
for i in range(len(xysort)-1):
    if(xysort[i][0]==xysort[i+1][0] and xysort[i][1]==xysort[i+1][1] and abs(xysort[i][2]-xysort[i+1][2])<=1):
        sides-=2
for i in range(len(zxsort)-1):
    if(zxsort[i][0]==zxsort[i+1][0] and zxsort[i][1]==zxsort[i+1][1] and abs(zxsort[i][2]-zxsort[i+1][2])<=1):
        sides-=2
for i in range(len(yzsort)-1):
    if(yzsort[i][0]==yzsort[i+1][0] and yzsort[i][1]==yzsort[i+1][1] and abs(yzsort[i][2]-yzsort[i+1][2])<=1):
        sides-=2
for x in range(min(xysort)[0], max(xysort)[0]):
    for y in range(min(yzsort)[0], max(yzsort)[0]):
        for z in range(min(zxsort)[0], max(zxsort)[0]):
            coords = (x, y, z)
            if(not(coords in xysort)):
                iscenter = [False for i in range(6)]
                for i in range(max(xysort)[0]-min(xysort)[0]):
                    if((x-i, y, z) in xysort):
                        iscenter[0]=True
                    if((x+i, y, z) in xysort):
                        iscenter[1]= True
                for i in range(max(yzsort)[0]-min(yzsort)[0]):
                    if((x, y-i, z) in xysort):
                        iscenter[2]=True
                    if((x, y+i, z) in xysort):
                        iscenter[3]= True
                for i in range(max(zxsort)[0]-min(zxsort)[0]):
                    if((x, y, z-i) in xysort):
                        iscenter[4]=True
                    if((x, y, z+i) in xysort):
                        iscenter[5]= True
                if(not(False in iscenter)):
                    if((coords[0]-1, coords[1], coords[2]) in xysort):
                        sides-=1
                    if((coords[0]+1, coords[1], coords[2]) in xysort):
                        sides-=1
                    if((coords[0], coords[1]-1, coords[2]) in xysort):
                        sides-=1
                    if((coords[0], coords[1]+1, coords[2]) in xysort):
                        sides-=1
                    if((coords[0], coords[1], coords[2]-1) in xysort):
                        sides-=1
                    if((coords[0], coords[1], coords[2]+1) in xysort):
                        sides-=1
print(sides)