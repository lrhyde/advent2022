#do 3 iterations
#then manually figure it out
import numpy as np
input = open("advent of code 2022/input_day17.txt", "r")
ind = 0
pieces = [[[3,2], [3,3], [3,4], [3,5]], [[4, 2], [4, 3], [4, 4], [3, 3], [5, 3]], [[3, 2], [3, 3], [3, 4], [4, 4], [5, 4]], [[3, 2], [4, 2], [5, 2], [6, 2]], [[3, 2], [3,3], [4, 2], [4, 3]]]
dirs = ""
for line in input:
    dirs = line
pastpieces = []
ind = 0
dir = 0
right4 = np.array([[0, 1] for i in range(4)])
right5 = np.array([[0, 1] for i in range(5)])
left4 = np.array([[0, -1] for i in range(4)])
left5 = np.array([[0, -1] for i in range(5)])
up4 = np.array([[1, 0] for i in range(4)])
up5 = np.array([[1, 0] for i in range(5)])
for i in range(2022):
    ind = i%5
    piece = np.array(pieces[ind])
    placed = False
    while(not placed):
        if(dir==">"):
            if(len(piece)==4):
                piece+=right4
            else:
                piece+=right5