infile = open("advent of code 2022/input_day14.txt", "r")
outfile = open("output_day14.txt", "w")
grid = []
for i in range(200):
    grid.append(['.' for k in range(300)])
filled = set()
maxy = 0
for line in infile:
    pieces = line.split("->")
    for i in range(len(pieces)-1):
        coord1 = pieces[i].strip().split(",")
        coord2 = pieces[i+1].strip().split(",")
        coord1[0] = int(coord1[0])
        coord1[1] = int(coord1[1])
        coord2[0] = int(coord2[0])
        coord2[1] = int(coord2[1])
        if(coord1[1]>maxy):
            maxy = coord1[1]
        if(coord2[1]>maxy):
            maxy = coord2[1]
        if(int(coord1[0])==int(coord2[0])):
            if(coord1[1]<coord2[1]):
                for j in range(coord1[1], coord2[1]+1):
                    grid[j][coord1[0]-400]="#"
                    filled.add((j, coord1[0]-400))
            else:
                for j in range(coord2[1], coord1[1]+1):
                    grid[j][coord1[0]-400]="#"
                    filled.add((j, coord1[0]-400))
        else:
            if(coord1[0]<coord2[0]):
                for j in range(coord1[0], coord2[0]+1):
                    grid[coord1[1]][j-400]="#"
                    filled.add((coord1[1], j-400))
            else:
                for j in range(coord2[0], coord1[0]+1):
                    grid[coord1[1]][j-400]="#"
                    filled.add((coord1[1], j-400))
floor = maxy+2
for i in range(-400, 400):
    #grid[floor][i] = "#"
    filled.add((floor, i))
def printgrid():
    for i in range(300):
        outfile.write(str(i%10))
    for line in grid:
        for char in line:
            outfile.write(char)
        outfile.write("\n")
def myfunc():
    blockcount = 0
    foundfinal = False
    while(1):
        blockcount+=1
        sand = [0, 100]
        placed = False
        while(1):
            yval = sand[0]+1
            if((yval, sand[1]) in filled):
                if((yval, sand[1]-1) in filled):
                    if((yval, sand[1]+1) in filled):
                        filled.add(tuple(sand))
                        placed = True
                        grid[sand[0]][sand[1]] = "o"
                        if(sand[0]==0 and sand[1]==100):
                            return blockcount
                        #printgrid()
                    else:
                        sand = [yval, sand[1]+1]
                else:
                    sand = [yval, sand[1]-1]
            else:
                sand = [yval, sand[1]]
            if(placed):
                break
blockcount = myfunc()     
print(blockcount)