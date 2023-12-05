import re

f = open("day3/input.txt", "r")
numPositions = []
inputList = []

lines = f.read().splitlines()
gearsFound = {}

def FindSymbol(startX:int, startY:int, lenght:int, value:int):
    for i in range(-1,2):
        row = ''
        for j in range(-1,lenght+1):
            if(startY+i >= 0 and startY+i < len(inputList) and startX+j >= 0 and startX+j < len(inputList[startY+i])):
                if(re.match(r'[\*]',inputList[startY+i][startX+j])): #search for *
                    key = fr'{startY+i},{startX+j}' # X and Y position in array
                    if key in gearsFound:
                        gearsFound[key].append(value)
                    else:
                        gearsFound[key] = [value]

for x in lines:
    inputList.append(x)
    tempList = []
    for y in re.finditer(r"\d+",x):
        z = [y.start(), int(y.end()-y.start()), int(y.group())] #looks for: positionX when number starts, length of number, value to '*'
        tempList.append(z)
    numPositions.append(tempList)

validGears = []

for i, posRow in enumerate(numPositions):
    for numInfo in posRow:
        FindSymbol(numInfo[0], i, numInfo[1], numInfo[2])


total = 0

for i in gearsFound:
    if len(gearsFound[i]) == 2: # if * has 2 neighbours
        total += gearsFound[i][0] * gearsFound[i][1]
print(total)