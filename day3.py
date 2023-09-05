infile = open("advent of code 2022/input_day3.txt", "r")
import string
letters = string.ascii_lowercase
#letters = "abcdefghijklmnopqrstuvwxyz"
lettersup = letters.upper()
letters+=lettersup
score = 0
count = 1
collector = []
for line in infile:
    if(not(count==300)):
        line = line[0:len(line)-1]
    collector.append(line)
    if(len(collector)==3):
        score+=1
        found = False
        for char in collector[0]:
            if(char in collector[1] and char in collector[2]):
                found = True
                score+=letters.index(char)
                break
        if(found==False):
            print(line)
        count+=1
        collector = []
print(score)