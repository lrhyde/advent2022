infile = open("advent of code 2022/input_day7.txt", "r")
#node format: (name, parent index, [child, child, child])
parents = [["START", 0, set()]]
linecount = 0
parind = 0
for line in infile:
    linecount+=1
    if(not(linecount==1047)):
        line = line[0:len(line)-1]
    if(not( '$' in line)):
        if("dir" in line):
            parents[parind][2].add(line.split(" ")[1])
        else:
            parents[parind][2].add(line.split(" ")[0])
    else:
        pieces = line.split(" ")
        if(pieces[1] == "cd"):
            if(pieces[2] == ".."):
                parind = parents[parind][1]
            elif(pieces[2]=="/"):
                parind = 0
            else:
                found = False
                for i in range(parind, len(parents)):
                    if(parents[i][0]==pieces[2] and parents[i][1]==parind):
                        parind = i
                        found = True
                if (not found):
                    parents.append([pieces[2], parind, set()])
                    parind = len(parents)-1

def findvalue(k, myc):
    count = 0
    for value in k[2]:
        if(not(value.isnumeric())):
            for i in range(myc, len(parents)):
                if(parents[i][0]==value and parents[i][1]==myc):
                    count+=findvalue(parents[i], i)
        else: 
            count+=int(value)
    return count
total = 0
myc = 0
min = 6666666666666666666666666
total = findvalue(parents[0], 0)
alrfree = 70000000-total
for k in parents:
    v = findvalue(k, myc)
    myc+=1
    if(v>30000000-alrfree and min>v):
        min = v
print(min)