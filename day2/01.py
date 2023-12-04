import re

f = open("day2/input.txt", "r")

count = 0
for i, x in enumerate(f):
    flag = False
    for y in re.findall(r'\d+ red',x):
        red = int(re.sub(r' red',"",y))
        if(red > 12):
            flag = True

    for y in re.findall(r'\d+ green',x):
        green = int(re.sub(r' green',"",y))
        if(green > 13):
            flag = True

    for y in re.findall(r'\d+ blue',x):
        blue = int(re.sub(r' blue',"",y))
        if(blue > 14):
            flag = True

    if(not flag):
        count += i + 1
print(count)
