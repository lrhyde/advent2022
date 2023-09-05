infile = open("advent of code 2022/input_day5.txt", "r")
arr = []
for i in range(10):
    arr.append([])
count = 1
for line in infile:
    if(count==1):
        arr[1].append("C")
        arr[4].append("S")
        arr[5].append("H")
    elif(count==2):
        arr[1].append("F")
        arr[2].append("B")
        arr[4].append("C")
        arr[5].append("S")
        arr[7].append("W")
    elif(count==3):
        arr[1].append("B")
        arr[2].append("W")
        arr[4].append("W")
        arr[5].append("M")
        arr[6].append("S")
        arr[7].append("B")
    elif("[" in line):
        line = line[0:len(line)-1]
        parts = line.split("[")
        parts = parts[1:len(parts)]
        for i in range(len(parts)):
            arr[i+1].append(parts[i][0])
    # elif("move" in line):
    #     parts = line.split(" ")
    #     numtaken = int(parts[1])
    #     placetaken = int(parts[3])
    #     placegoing = int(parts[5])
    #     for i in range(numtaken):
    #         arr[placegoing] = [arr[placetaken].pop(0)] + arr[placegoing]
    elif("move" in line):
        parts = line.split(" ")
        numtaken = int(parts[1])
        placetaken = int(parts[3])
        placegoing = int(parts[5])
        temparr = []
        for i in range(numtaken):
            temparr.append(arr[placetaken].pop(0))
        arr[placegoing] = temparr + arr[placegoing]
    count+=1
for i in range(9):
    print(arr[i+1][0], end="")