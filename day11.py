#what to keep track of for each monkey: current items, function, divnum, true, false, total throws
monkeys = []
for i in range(8):
#for i in range(4):
    monkeys.append([])
infile = open("advent of code 2022/input_day11.txt", "r")
inputdex = -1
count = 0
def makefunction(pieces):
    if(pieces[5]=="old"):
        def newfunc(old):
            return old*old
    elif(pieces[4]=="*"):
        def newfunc(old):
            return old*int(pieces[5])
    elif(pieces[4]=="+"):
        def newfunc(old):
            return old + int(pieces[5])
    return newfunc

for line in infile:
    count+=1
    if(line[0:6]=="Monkey"):
        if(not(inputdex==-1)): monkeys[inputdex].append(0)
        inputdex = int(line.split(" ")[1][0])
    elif(not(line=="\n")):
        if(not(count==55)):
        #if(not(count==27)):
            line = line[0:len(line)-1]
        pieces = line.strip().split(" ")
        if(pieces[0]=="Starting"):
            monkeys[inputdex].append([])
            for i in range(2, len(pieces)):
                p = pieces[i].split(",")
                monkeys[inputdex][0].append(int(p[0]))
        elif(pieces[0]=="Operation:"):
            monkeys[inputdex].append(makefunction(pieces))
        elif(pieces[0]=="Test:"):
            monkeys[inputdex].append(int(pieces[3]))
        elif(pieces[0]=="If"):
            monkeys[inputdex].append(int(pieces[5]))
monkeys[inputdex].append(0)
max1 = 0
max2 = 0
#run 200 or something
#track where each item goes to
#see how long each cycle is
lcm = 1
for i in range(len(monkeys)):
    lcm*=monkeys[i][2]
for i in range(10000):
    for j in range(len(monkeys)):
        for obj in monkeys[j][0]:
            obj = monkeys[j][1](obj)
            obj = obj%lcm
            if(obj%monkeys[j][2]==0):
                monkeys[monkeys[j][3]][0].append(obj)
            else:
                monkeys[monkeys[j][4]][0].append(obj)
            monkeys[j][5]+=1
        monkeys[j][0]=[]
for i in range(len(monkeys)):
    print(monkeys[i][5])
    if(monkeys[i][5]>max1):
        max2 = max1
        max1 = monkeys[i][5]
    elif(monkeys[i][5]>max2):
        max2 = monkeys[i][5]
#print(max1, max2)
print((max1*max2))