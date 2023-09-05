infile = open("advent of code 2022/testerinput.txt", "r")
q = []
grid = []
mc = 0
for line in infile:
    l = ""
    mc+=1
    for char in line:
        if(not(char=="^" or char=="<" or char==">" or char=="v" or char==".")):
            cc = 0
        else:
            cc+=1
            #if(not(mc==1) and not mc==37):
            if(not(mc==1) and not mc==6):
                l+=char
    if(len(l)>0):
        grid.append(l)
ups = []
dps = []
lps = []
rps = []
for r in range(len(grid)):
    for c in range(len(grid[0])):
        try:
            if(grid[r][c]=="^"):
                ups.append([r, c])
            elif(grid[r][c]=="v"):
                dps.append([r, c])
            elif(grid[r][c]=="<"):
                lps.append([r, c])
            elif(grid[r][c]==">"):
                rps.append([r, c])
        except:
            print(r, c)
def funkybfs(initialq):
    count=0
    q = initialq.copy()
    while(1):
        count+=1
        #update poses
        #check queue against updated poses
        #go through approved queue memebrs and add all their results to q
        #if its at bottom right, return min+1
        for x in ups:
            x[0]-=1
            x[0] = (x[0] + len(grid))%len(grid)
        for x in dps:
            x[0]+=1
            x[0] = (x[0] + len(grid))%len(grid)
        for x in rps:
            x[1]+=1
            x[1] = (x[1] + len(grid[1]))%len(grid[1])
        for x in lps:
            x[1]-=1
            x[1] = (x[1] + len(grid[1]))%len(grid[1])
        k = len(q)
        q2 = []
        for i in range(k):
            item = q.pop(0)
            if(item in ups or item in dps or item in rps or item in lps):
                a=5
            else:
                if(initialq == [[-1, 0]] and item==[len(grid)-1, len(grid[1])-1]):
                    for x in ups:
                        x[0]-=1
                        x[0] = (x[0] + len(grid))%len(grid)
                    for x in dps:
                        x[0]+=1
                        x[0] = (x[0] + len(grid))%len(grid)
                    for x in rps:
                        x[1]+=1
                        x[1] = (x[1] + len(grid[1]))%len(grid[1])
                    for x in lps:
                        x[1]-=1
                        x[1] = (x[1] + len(grid[1]))%len(grid[1])
                    return count+1 
                if(initialq== [[len(grid), len(grid[1])-1]] and item==[0, 0]):
                    for x in ups:
                        x[0]-=1
                        x[0] = (x[0] + len(grid))%len(grid)
                    for x in dps:
                        x[0]+=1
                        x[0] = (x[0] + len(grid))%len(grid)
                    for x in rps:
                        x[1]+=1
                        x[1] = (x[1] + len(grid[1]))%len(grid[1])
                    for x in lps:
                        x[1]-=1
                        x[1] = (x[1] + len(grid[1]))%len(grid[1])
                    return count+1
                p = item
                if([p[0]+1, p[1]] in dps):
                    a = 5
                elif([p[0]-1, p[1]] in ups):
                    a = 5
                else:
                    if(item not in q2): q2.append(item)
                if(item[0]+1<len(grid)):
                    if([item[0]+1, item[1] ] not in q2 and [item[0]+1, item[1] ] not in ups): q2.append([item[0] + 1 , item[1]])
                if(item[0]-1>=0):
                    if([item[0]-1, item[1] ] not in q2 and [item[0]-1, item[1] ] not in dps): q2.append([item[0] - 1 , item[1]])
                if(item[1]+1<len(grid[1])):
                    if([item[0], item[1] + 1 ] not in q2 and [item[0], item[1] + 1 ] not in lps): q2.append([item[0], item[1] + 1 ])
                if(item[1]-1>=0):
                    if([item[0], item[1] - 1 ] not in q2 and [item[0], item[1] - 1 ] not in rps): q2.append([item[0], item[1] - 1 ])
        q = q2
print(funkybfs([[-1, 0]]))
print(funkybfs([[len(grid), len(grid[1])-1]]))
print(funkybfs([[-1, 0]]))