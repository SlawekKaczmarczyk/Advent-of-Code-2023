import re
import math

f = open("day7/input.txt","r")
lines = f.read().splitlines()

hands= []

for i in lines: 
    temp = []
    temp.append(re.search(r'[\dAKQJT]+', i).group())
    temp.append(int(re.search(r' [\d]+', i).group()))
    hands.append(temp)

valueDict = {'J' : 1,'2' : 2,'3' : 3,'4' : 4,'5' : 5,'6' : 6,'7' : 7,'8' : 8,'9' : 9,'T' : 10,'Q' : 11,'K' : 12,'A' : 13}
strength = [[],[],[],[],[],[],[]]
# literally strength of cards - so strength[0] are five of kind, strength[1] is four of kind etc.

for x in hands:
    count = {}
    # Count each instance of a card
    for i in x[0]:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    # Sort hand into different categories - different number for each category

    if "J" in count:
        # Find which card has the highest count
        highV = 0
        highKey = 'J'
        for y in count:
            if(y != 'J'): # Avoid cases where xyJJz/xJJJy/xJJJJ would keep the Js
                if(count[y] > highV):
                    highKey = y
                    highV = count[y]
                elif(count[y] == highV and valueDict[y] > valueDict[highKey]):
                    highKey = y
        if(highKey != 'J'):
            count[highKey] += count['J']
            count.pop('J')

    # Sort hand into different categories
    # I realized that you can multiply every number of matches and get a different number for each category
    value = 1
    for i in count:
        value *= count[i]



    match value:
        case 1:
            strength[6].append(x)
        case 2:
            strength[5].append(x)
        case 3:
            strength[3].append(x)
        # The only exception is when it's 4, which could be either two pairs or 4 of a kind
        case 4:
            if(len(count) == 2):
                strength[1].append(x)
            else:
                strength[4].append(x)
        case 5:
            strength[0].append(x)
        case 6:
            strength[2].append(x)


convertedStrength = []

for x in strength:
    temp = []
    for i in x:
        # Substituting T J Q K A with A B C D E for ordering later
        y = re.sub(r'A',r'E',i[0])
        y = re.sub(r'T',r'A',y)
        y = re.sub(r'J',r'1',y) #changing J to 1
        y = re.sub(r'Q',r'C',y)
        y = re.sub(r'K',r'D',y)
        temp.append([int(y,16),i[1]])
    temp.sort()
    temp.reverse()
    for i in temp:
        convertedStrength.append(i)


total = 0
for x in range(0,len(convertedStrength)):
    total += (convertedStrength[x][1] * (len(convertedStrength)-x))

print(total)
