import re

f = open("day4/input.txt","r")

lines = f.read().splitlines()
wNumbers = []
cardNums = []
total = 0

for x in lines:
    y = re.sub(r'Card[\s]+[\d]+: ',"",x). split(" | ")
    wNumbers.append(list(map(int,re.findall(r'[\d]+', y[0])))) #append list of winning numbers
    cardNums.append(list(map(int,re.findall(r'[\d]+', y[1])))) #append list of your numbers

for i, x in enumerate(cardNums):
    winners = 0
    points = 0
    for y in x:
        if y in wNumbers[i]:
            winners+=1
    if winners > 0:
        points = pow(2,winners-1)
    total += points

print(total)