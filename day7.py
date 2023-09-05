infile = open("advent of code 2022/input_day7.txt", "r")
myd = {}
#parent_current: ([file, file, file], value)
#node format: (parent index, [child, child, child])
nowparent = "START"
nowparentname = "START"
linecount = 0
myd["START"] = [[], 0]
for line in infile:
    linecount+=1
    if(not(linecount==1047)):
        line = line[0:len(line)-1]
    if(not( '$' in line)):
        if("dir" in line):
            name = nowparent + "_" + line[4:len(line)]
            if(not(name in myd)):
                myd[name] = [[], 0, False]
                myd[nowparentname][0].append(name)
        else:
            pieces = line.split(" ")
            if(not("file__" + pieces[1] in myd[nowparentname][0])):
                myd[nowparentname][0].append("file__" + pieces[1])
                myd[nowparentname][1]+=int(pieces[0])
    else:
        pieces = line.split(" ")
        if(pieces[1] == "cd"):
            if(pieces[2] == ".."):
                nowparent = nowparentname.split("_")[0]
                for k in myd.keys():
                    if(k=="START"):
                        if(nowparent=="START"):
                            nowparentname= "START"
                    elif(k.split("_")[1]==nowparent and nowparentname in myd[k][0]):
                        nowparentname = k 
            elif(pieces[2]=="/"):
                nowparent = "START"
                nowparentname = "START"
            else:
                nowparentname = nowparent + "_" + pieces[2]
                nowparent = pieces[2]

def findvalue(k):
    for value in k[0]:
        if(not(value.isnumeric())):
            k[1]+=findvalue(k[0])
    return k[1]
total = 0
for k in myd.keys():
    v = findvalue(k)
    if(v<100000):
        total+=v