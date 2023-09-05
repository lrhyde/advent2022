infile = open("advent of code 2022/input_day1.txt", "r")
maxnum = 0
maxnum2 = 0
maxnum3 = 0
curnum = 0
for line in infile:
    if(not(line=="\n")):
        curnum+=int(line)
    else:
        if(curnum>maxnum):
            maxnum3 = maxnum2
            maxnum2 = maxnum
            maxnum = curnum
        elif(curnum>maxnum2):
            maxnum3 = maxnum2
            maxnum2 = curnum
        elif(curnum>maxnum3):
            maxnum3 = curnum
        curnum = 0
total = maxnum + maxnum2 + maxnum3
print(total)