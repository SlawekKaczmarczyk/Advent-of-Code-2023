import math
import re


f = open("day6/input.txt","r")
lines = f.read().splitlines()

timesL = list(map(int,re.findall(r'[\d]+', lines[0])))
distancesL = list(map(int, re.findall(r'[\d]+',lines[1])))

total = 1

for totaltime,dist in zip(timesL,distancesL):
    x = 0 #lowest time that meets the requirements
    for x in range(math.ceil(totaltime/2)): #it's simetrical so we check half of range
        if x * (totaltime-x) > dist: # break when x time beats record
            break

    total *= (totaltime - 2*x)+1
print(total)