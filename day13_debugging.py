infile1 = open("output_day13.txt", "r")
infile2 = open("output (2).txt", "r")
arr = []
arr2 = []
for line in infile1:
    if("0" in line or "1" in line):
        arr.append(line[0])
for line in infile2:
    if("0" in line or "1" in line):
        arr2.append(line[0])
print(arr)
print(arr2)
for i in range(len(arr)):
    if(not(arr[i]==arr2[i])):
        #print(str(3*(i+1)))
        #print(arr[i])
        arr2=arr