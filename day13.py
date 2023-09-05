input = open("advent of code 2022/testerinput.txt", "r")
outfile = open("output_day13.txt", "w")
def arrinterpret(st):
    arr = []
    st2 = st
    if(st.isnumeric()):
        return int(st)
    for i in range(len(st)):
        if(len(st2)==0):
            return arr
        if(st2[0]=="]"):
            return arr
        if(st2[0]=="["):
            arr.append(arrinterpret(st2[1:len(st2)-1]))
            hi = st2.index("]")
            mini = st2[0:hi]
            cs = mini.count("[")
            extras = 0
            st2 = st2[st2.index("]")+1:len(st2)]
            extras2 = cs-1
            while(extras2>0):
                extras = extras2
                extras2 = 0
                for i in range(extras):
                    n = st2.index("]")
                    if(st2[0:n].count("[")>0):
                        extras2+=st2[0:n].count("[")
                    st2 = st2[st2.index("]")+1:len(st2)]
        elif(st2[0].isnumeric()):
            try:
                arr.append(int(st2[0:st2.index(",")]))
            except:
                if("]" in st2):
                    arr.append(int(st2[0:st2.index("]")]))
                else:
                    arr.append(int(st2[0:len(st2)]))
                return arr
            st2 = st2[st2.index(","):len(st2)]
        else:
            st2 = st2[1:len(st2)]
def compare(pair1, pair2):
    if(type(pair1) is int and type(pair2) is int):
        if(pair1==pair2):
            return "inc"
        else: return pair1<pair2
    elif(type(pair1) is list and type(pair2) is list):
        for i in range(len(pair1)):
            if(i>=len(pair2)):
                return False
            k = compare(pair1[i], pair2[i])
            if(not(k=="inc")):
                return k
        if(len(pair1)<len(pair2)):
            return True
        else:
            return "inc"
    elif(type(pair1) is list):
        return compare(pair1, [pair2])
    else:
        return compare([pair1], pair2)
pair1 = None
pair2 = None
count = 0
indices = []
arrs = []
for line in input:
    count+=1
    if(count%3==1):
        line = line[0:len(line)-1]
        pair1 = arrinterpret(line[1:len(line)])
        arrs.append(pair1)
    elif(count%3==2):
        line = line[0:len(line)-1]
        pair2 = arrinterpret(line[1:len(line)])
        arrs.append(pair2)
    else:
        if(count==429):
            print("hi debugger")
        c = compare(pair1, pair2)
        if(c==True):
            outfile.write("1\n\n\n")
            indices.append(count//3)
        else:
            outfile.write("0\n\n\n")
print(sum(indices))
count1 = 1
count2 = 2
for thing in arrs:
    if(compare(thing, [[2]])==True):
        count1+=1
    if(compare(thing, [[6]])==True):
        count2+=1
print(str(count1*count2))