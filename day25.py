infile = open("advent of code 2022/input_day25.txt", "r")
count = 0
rsum = 0
for line in infile:
    count+=1
    if(not(count==105)):
        line=line[0:len(line)-1]
    num = 0
    for x in range(len(line)):
        p = pow(5, len(line)-1-x)
        if(line[x]=="="):
            num+=-2*p
        if(line[x]=="-"):
            num+=-1*p
        if(line[x]=="1"):
            num+=p
        if(line[x]=="2"):
            num+=2*p
    rsum+=num
print(rsum)
def conv(num):
    #s = str(num)
    tens = num
    news = ""
    while(not(tens==0)):
        item = tens
        ones = str(item%5)
        tens = item//5
        news = ones + news
    return news
def conv2(num):
    #s = str(num)
    tens = num*2
    news = ""
    while(not(tens==0)):
        item = tens
        ones = str(item%5)
        tens = item//5
        news = ones + news
    news2 = ""
    for i in range(len(news)):
        if(news[i] == "0"):
            news2+="="
        elif(news[i]=="1"):
            news2+="-"
        elif(news[i]=="2"):
            news2+="0"
        elif(news[i]=="3"):
            news2+="1"
        elif(news[i]=="4"):
            news2+="2"
    return news2
print(conv(1))
print(conv(2))
print(conv(3))
print(conv(4))
print(conv(5))
print(conv2(1))
print(conv2(2))
print(conv2(3))
print(conv2(4))
print(conv2(5))