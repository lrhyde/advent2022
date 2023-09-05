infile = open("advent of code 2022/input_day4.txt", "r")
count = 0
num = 1
for line in infile:
    if(not(num==300)):
        line = line[0:len(line)-1]
    firstsplit = line.split(",")
    elf1 = firstsplit[0].split("-")
    elf2 = firstsplit[1].split("-")
    elf1 = (int(elf1[0]), int(elf1[1]))
    elf2 = (int(elf2[0]), int(elf2[1]))
    if(elf2[0]<=elf1[0] and elf2[1]>=elf1[0]):
        count+=1
    elif(elf1[0]<=elf2[0] and elf1[1]>=elf2[0]):
        count+=1
    elif(elf2[0]<=elf1[1] and elf2[1]>=elf1[1]):
        count+=1
    elif(elf1[0]<=elf2[1] and elf1[1]>=elf2[1]):
        count+=1
    num+=1
print(count)