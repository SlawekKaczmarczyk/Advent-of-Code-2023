import re

f = open("day3/input.txt", "r")
numPositions = []
inputList = []

lines = f.read().splitlines()

# FindSymbol looks for symbol adjecent to digits
def FindSymbol(startX: int, startY: int, lenght: int):
    flag = False

    for i in range(-1,2):
        for j in range(-1,lenght+1): #check surrounding of j
            if(startY+i >= 0 and startY+i<len(inputList) and startX+j >= 0 and startX+j < len(inputList[startY+i])):
                if(re.match(r'[^\d\.\n]',inputList[startY+i][startX+j])): #search for symbol that are not . and digits:
                    flag = True
    return flag

for x in lines:
    inputList.append(x)
    tempList = []
    for y in re.finditer(r"\d+",x): #find all digits sequences
        z = [y.start(), int(y.end()-y.start()), int(y.group())] #looks for: positionX when number starts, length of number, value
        tempList.append(z)
    numPositions.append(tempList) #array of lists



validNumbers = 0
for i, posRow in enumerate(numPositions):
    for numInfo in posRow:
        if(FindSymbol(numInfo[0], i, numInfo[1])): # if symbol is found for number in positionX(numInfo[0]) and lenght(numInfo[1]) add it's value to result
            validNumbers+=numInfo[2]

print(validNumbers)