import re
import math

f = open("day8/input.txt", "r")
lines = f.read().splitlines()
f.close()

# Getting directions, turning L to 0 and R to 1
directions = re.sub(r'L','0',lines[0])
directions = re.sub(r'R','1',directions)


lines = lines[2:]
# Getting key: [value1, value2] from each line
mapDict = {}
starting = []
for x in lines:
    key = re.search(r'[A-Z]+',x).group()
    mappings = re.search(r'\(.+\)',x).group()
    mappings = re.findall(r'[A-Z]+', mappings)
    mapDict[key] = mappings

    #Change - get keys ..A
    if re.match(r'..A',key):
        starting.append(key)
    
print(starting)

# Iterating through the map with the directions
steps = 0
currKeys = starting #Change of starting position
mod = len(directions)
stepL = [None] * len(currKeys) #Without [None] result is 1
while(True):
    for i,k in enumerate(currKeys):
        currKey = mapDict[k][int(directions[steps%mod])]
        currKeys[i] = currKey
        if re.match(r'..Z',currKey):
             stepL[i] = steps + 1
    steps += 1
    if None not in stepL:
        break


total = math.lcm(*stepL) #least common multiplier
print(total)
