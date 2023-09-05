infile = open("advent of code 2022/input_day12.txt", "r")
arr = []
start = [0, 0]
end = [0, 0]
alpha = "Sabcdefghijklmnopqrstuvwxyz"
alist = []
for line in infile:
    arr.append("")
    slash = False
    for char in line:
        if(char.isalpha() and not slash):
            arr[len(arr)-1]+=char
            if(char=="S"):
                start = [len(arr)-1, len(arr[len(arr)-1])-1]
            elif(char=="E"):
                end = [len(arr)-1, len(arr[len(arr)-1])-1]
            elif(char=="a"):
                alist.append([len(arr)-1, len(arr[len(arr)-1])-1])
        else:
            slash = True

def runalist(n):
    locales = [n]
    count = 0
    found = False
    visited = set()
    while(1):
        count+=1
        if(count==31):
            print("hi debugger")
        for i in range(len(locales)):
            current = locales.pop(0)
            if(tuple(current) not in visited):
                visited.add(tuple(current))
                letter = arr[current[0]][current[1]]
                if(letter=="S"):
                    letter="a"
                if(letter=="E"):
                    found = True
                    print(count)
                    break
                try:
                    if(current[0]>0 and alpha.index(arr[current[0]-1][current[1]])-alpha.index(letter)<=1):
                        locales.append([current[0]-1, current[1]])
                except:
                    if(letter=="z" or letter=="y"):
                        return count
                        found = True
                    else:
                        print(current)
                        print(arr[current[0]][current[1]])
                try:
                    if(current[0]<len(arr)-1 and alpha.index(arr[current[0]+1][current[1]])-alpha.index(letter)<=1):
                        locales.append([current[0]+1, current[1]])
                except:
                    if(letter=="z" or letter=="y"):
                        return count
                        found = True
                    else:
                        print(current)
                        print(arr[current[0]][current[1]])
                try:
                    if(current[1]>0 and alpha.index(arr[current[0]][current[1]-1])-alpha.index(letter)<=1):
                        locales.append([current[0], current[1]-1])
                except:
                    if(letter=="z" or letter=="y"):
                        return count
                        found = True
                    else:
                        print(current)
                        print(arr[current[0]][current[1]])
                try:
                    if(current[1]<len(arr[0])-1 and alpha.index(arr[current[0]][current[1]+1])-alpha.index(letter)<=1):
                        locales.append([current[0], current[1]+1])
                except:
                    if(letter=="z" or letter=="y"):
                        return count
                        found = True
                    else:
                        print(current)
                        print(arr[current[0]][current[1]])
        if(len(locales)==0):
            #print("uh oh", count)
            return 506
        if(found):
            break
maxk = 506
for a in alist:
    k = runalist(a)
    if(k<maxk):
        maxk = k
print(maxk)