infile = open("advent of code 2022/input_day8.txt", "r")
arr = []
linecount = 0
for line in infile:
    linecount+=1
    arr.append([])
    if(linecount<99):
    #if(linecount<5):
        line = line[0:len(line)-1]
    charcount=0
    for char in line:
        charcount+=1
        if(charcount==1 or charcount==len(line) or linecount==1 or linecount==99):
            arr[linecount-1].append([int(char), 1])
        else:
            arr[linecount-1].append([int(char), 0])
count = 0
def findscore(r, c):
    rightcount = 0
    leftcount = 0
    foundright = False
    foundleft = False
    val = arr[r][c][0]
    for i in range(1, len(arr)):
        try:
            if(not(foundright) and r+i<len(arr) and arr[r+i][c][0]>=val):
                rightcount+=1
                foundright = True
            elif(not(foundright) and r+i>=len(arr)):
                foundright = True
            elif(not(foundright)):
                rightcount+=1
        except:
            print("oopsies rr")
        try:
            if(not(foundleft) and (r-i<0 or arr[r-i][c][0]>=val)):
                if(r-i>=0):
                    leftcount+=1
                foundleft = True
            elif(not(foundleft)):
                leftcount+=1
        except:
            print("oopsies rl")
    multi = leftcount*rightcount
    rightcount = 0
    leftcount = 0
    foundright = False
    foundleft = False
    val = arr[r][c][0]
    for i in range(1, len(arr)):
        try:
            if(not(foundright) and c+i<len(arr) and arr[r][c+i][0]>=val):
                foundright = True
                rightcount+=1
            elif(not(foundright) and c+i>=len(arr)):
                foundright = True
            elif(not(foundright)):
                rightcount+=1
        except:
            print("oopsies cr")
        try:
            if(not(foundleft) and (c-i<0 or arr[r][c-i][0]>=val)):
                if(c-i>=0):
                    leftcount+=1
                foundleft = True
            elif(not(foundleft)):
                leftcount+=1
        except:
            print("oopsies cl")
    return multi*leftcount*rightcount
vmax = 0
for row in range(len(arr)):
    for thing in range(len(arr)):
        v = findscore(row, thing)
        if(v>vmax):
            vmax = v
findscore(3, 2)
print(vmax)