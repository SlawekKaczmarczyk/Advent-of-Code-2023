import re

f = open("day2/input.txt", "r")

sumAll = 0
for i, x in enumerate(f):
    
    minRed, minGreen, minBlue = 0,0,0 
    for y in re.findall(r'\d+ red',x):
        red = int(re.sub(r' red',"",y))
        if(red > minRed):
            minRed = red

    for y in re.findall(r'\d+ green',x):
        green = int(re.sub(r' green',"",y))
        if(green > minGreen):
            minGreen = green
            

    for y in re.findall(r'\d+ blue',x):
        blue = int(re.sub(r' blue',"",y))
        if(blue > minBlue):
            minBlue = blue
            
    sumAll += minRed * minBlue * minGreen

print(sumAll)
