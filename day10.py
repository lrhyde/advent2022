infile = open("advent of code 2022/input_day10.txt", "r")
cycle = 0
total = 0
x = 1
lines = []
for i in range(6):
    lines.append("")
for line in infile:
    if(line[0:4]=="noop"):
        cycle+=1
        if(abs((cycle-1)%40-x)<=1):
            lines[int((cycle-1)/40)]+="#"
        else:
            lines[int((cycle-1)/40)]+="."
    else:
        pieces = line.split(" ")
        v = int(pieces[1][0:len(pieces[1])-1])
        #cycle+=2
        cycle+=1
        if(abs((cycle-1)%40-x)<=1):
            lines[int((cycle-1)/40)]+="#"
        else:
            lines[int((cycle-1)/40)]+="."
        cycle+=1
        if(abs((cycle-1)%40-x)<=1):
            lines[int((cycle-1)/40)]+="#"
        else:
            lines[int((cycle-1)/40)]+="."
        x+=v
for line in lines:
    print(line)