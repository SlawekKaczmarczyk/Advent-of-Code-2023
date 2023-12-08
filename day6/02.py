import math
import re


f = open("day6/input.txt","r")
lines = f.read().splitlines()

lines[0] = re.sub(r'[\s]+', '', lines[0]) #remove whitespaces
lines[1] = re.sub(r'[\s]+', '', lines[1])
time = int(re.search(r'[\d]+', lines[0]).group())
dist = int(re.search(r'[\d]+', lines[1]).group())

total = 1

x = 14 #lowest time that meets the requirements, increasing, starting from 14
for x in range(math.ceil(time/2)): #it's simetrical so we check half of range
    if x * (time-x) > dist: # break when x time beats record
        break

total *= (time - 2*x)+1
print(total)