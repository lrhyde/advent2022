infile = open("advent of code 2022/input_day9.txt", "r")
head = [0, 0]
snake = []
for i in range(9):
    snake.append([0, 0])
positions = set()
positions.add((0, 0))
count = 0
for line in infile:
    count+=1
    if(not(count==2000)):
        line = line[0:len(line)-1]
    pieces = line.split(" ")
    direction = pieces[0]
    magnitude = pieces[1]
    for i in range(int(magnitude)):
        if(direction=="U"):
            head[1]+=1
        if(direction=="D"):
            head[1]-=1
        if(direction=="L"):
            head[0]-=1
        if(direction=="R"):
            head[0]+=1
        head2 = head
        for j in range(9):
            tail = snake[j]
            if(abs(head2[0]-tail[0])>1 or abs(head2[1]-tail[1])>1):
                if(not(head2[0]==tail[0])): snake[j][0]+=int((head2[0]-tail[0])/abs(head2[0]-tail[0]))
                if(not(head2[1]==tail[1])): snake[j][1]+=int((head2[1]-tail[1])/abs(head2[1]-tail[1]))
                if(j==8):
                    positions.add(tuple(tail))
            head2 = snake[j]
print(len(positions))