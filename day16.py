infile = open("advent of code 2022/testerinput.txt", "r")
#myd[name] = [connections, weight, on/off]
myd = dict()
pq = []
for line in infile:
    pieces = line.split(" ")
    name = pieces[1]
    rate = pieces[4]
    ratenum = int(rate.split("=")[1])
    connections = []
    for i in range(9, len(pieces)):
        try:
            connections.append(int(pieces[i]))
        except:
            connections.append(int(pieces[i][0:len(pieces[i])-1]))
    myd[name] = [connections, ratenum, False]
