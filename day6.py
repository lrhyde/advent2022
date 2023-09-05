def today():
    infile = open("advent of code 2022/input_day6.txt", "r")
    st = ""
    count = 0
    for line in infile:
        for char in line:
            count+=1
            st+=char
            if(len(st)>=14):
                tempst = st[len(st)-14:len(st)]
                found=True
                for ch in tempst:
                    if(tempst.count(ch)>1):
                        found=False
                if(found):
                    print(count)
                    return
today()