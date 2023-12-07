import re

f = open("day4/input.txt","r")

lines = f.read().splitlines()
wNumbers = []
cardNums = []

def GetMatches(winNums, cNums):
    matches = 0 
    for x in cNums:
        if x in winNums:
            matches += 1
    return matches
    
for x in lines:
    y = re.sub(r'Card[\s]+[\d]+: ',"",x). split(" | ") # Replacing Card `number` with ""
    wNumbers.append(list(map(int,re.findall(r'[\d]+', y[0])))) #append list of winning numbers
    cardNums.append(list(map(int,re.findall(r'[\d]+', y[1])))) #append list of your numbers

matchNum = []
copyNum = [1] * len(wNumbers)

for i, x in enumerate(cardNums):
    matchNum.append(GetMatches(wNumbers[i],x))

for i, x in enumerate(matchNum):
    for k in range (0, copyNum[i]):
        for j in range(i,x+i):
            copyNum[j+1] += 1


print(sum(copyNum))
