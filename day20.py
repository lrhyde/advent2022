infile = open('advent of code 2022/input_day20.txt', 'r')
arr = []
for line in infile:
    arr.append(int(line))
q = arr
for item in q:
    current = arr.index(item)
    value = item + current
    if(not(item==0)):
        if(value<=0):
            while(value<=0):
                value+=len(arr)
            value-=1
        while(value>=len(arr)):
            value = value%len(arr) + 1
    if(value==current):
        arr = arr
    elif(value>current):
        arr = arr[0:current] + arr[current+1:value+1] + [item] + arr[value+1:]
    else:
        arr = arr[0:value] + [item] + arr[value:current] + arr[current+1:]
total = arr[1000-1] + arr[2000-1] + arr[3000-1]
print(total)
#print(arr)