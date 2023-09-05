infile = open("advent of code 2022/input_day2.txt", "r")
score = 0
for line in infile:
    opp = line[0]
    win = line[2]
    if(win=="X"):
        if(opp=="A"):
            score+=3
        if(opp=="B"):
            score+=1
        if(opp=="C"):
            score+=2
    elif(win=="Z"):
        score+=6
        if(opp=="A"):
            score+=2
        if(opp=="B"):
            score+=3
        if(opp=="C"):
            score+=1
    else:
        score+=3
        if(opp=="A"):
            score+=1
        if(opp=="B"):
            score+=2
        if(opp=="C"):
            score+=3
print(score)