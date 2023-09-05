infile = open("advent of code 2022/input_day21.txt", "r")
myd = dict()
def recur(node):
    if(node=="humn"):
        print("human")
    if(type(myd[node][0]) is int):
        return myd[node][0]
    else:
        if(myd[node][3]=="/"):
            myd[node][0] = recur(myd[node][1])/recur(myd[node][2])
            return myd[node][0]
        if(myd[node][3]=="+"):
            myd[node][0] = recur(myd[node][1])+recur(myd[node][2])
            return myd[node][0]
        if(myd[node][3]=="-"):
            myd[node][0] = recur(myd[node][1])-recur(myd[node][2])
            return myd[node][0]
        if(myd[node][3]=="*"):
            myd[node][0] = recur(myd[node][1])*recur(myd[node][2])
            return myd[node][0]
def markhuman(node):
    if(node=="humn"):
        myd[node] = ["?", "?", "?", "?", "h"]
        return "h"
    if(len(myd[node])==1):
        return "m"
    else:
        if(markhuman(myd[node][1])=="h" or markhuman(myd[node][2])=="h"):
            print("hi")
            myd[node][4]="h"
            return "h"
        return "m"
def recur2(node, num):
    if(node=="pppw"):
        print("hi debugger")
    if(node=="humn"):
        print(num)
    else:
        print(node)
        try:
            if(myd[node][3]=="/"):
                #1/2 = num
                if((len(myd[myd[node][1]])==1) or myd[myd[node][1]][4]=="m"):
                    recur2(myd[node][2], myd[myd[node][1]][0]/num)
                else:
                    recur2(myd[node][1], myd[myd[node][2]][0]*num)
        except:
            print("oops", node)
        if(myd[node][3]=="+"):
            if((len(myd[myd[node][1]])==1) or myd[myd[node][1]][4]=="m"):
                recur2(myd[node][2], num-myd[myd[node][1]][0])
            else:
                recur2(myd[node][1], num-myd[myd[node][2]][0])
        if(myd[node][3]=="-"):
            #1-2 = num
            if((len(myd[myd[node][1]])==1) or myd[myd[node][1]][4]=="m"):
                recur2(myd[node][2], myd[myd[node][1]][0]-num)
            else:
                recur2(myd[node][1], num+myd[myd[node][2]][0])
        if(myd[node][3]=="*"):
            if((len(myd[myd[node][1]])==1) or myd[myd[node][1]][4]=="m"):
                recur2(myd[node][2], num/myd[myd[node][1]][0])
            else:
                recur2(myd[node][1], num/myd[myd[node][2]][0])
for line in infile:
    pieces = line.split(":")
    name = pieces[0]
    if("/" in pieces[1]):
        chunks = pieces[1].split("/")
        myd[name] = ["?", chunks[0].strip(), chunks[1].strip(), "/", "m"]
    elif("+" in pieces[1]):
        chunks = pieces[1].split("+")
        myd[name] = ["?", chunks[0].strip(), chunks[1].strip(), "+", "m"]
    elif("-" in pieces[1]):
        chunks = pieces[1].split("-")
        myd[name] = ["?", chunks[0].strip(), chunks[1].strip(), "-", "m"]
    elif("*" in pieces[1]):
        chunks = pieces[1].split("*")
        myd[name] = ["?", chunks[0].strip(), chunks[1].strip(), "*", "m"]
    else:
        myd[name] = [int(pieces[1])]
#print(recur(myd["root"][1]))
recur("root")
markhuman("root")
num = recur(myd["root"][2])
recur2(myd["root"][1], num)