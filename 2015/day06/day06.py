import re
import sys
import numpy as np
import copy 

#turn on 887,9 through 959,629
#turn on 454,398 through 844,448

ans1 = 0
ans2 = 0

if len(sys.argv) > 1:
    filename = sys.argv[1]
    f = open(sys.argv[1], "r")
else:
    f = open("01", "r")

lines = np.array([l.strip() for l in f.readlines()])

lights = [[False for i in range(1000)] for k in range(1000)]
lights2 = [[0 for i in range(1000)] for k in range(1000)]
#lights = [[0 for i in range(10)] for k in range(10)]

def light_mode(cmd:str, current_value:bool) -> bool:
    if "turn on" in cmd:
        return True
    elif "turn off" in cmd:
        return False
    else:
        return not current_value

def part1(l:str):
    x1,y1,x2,y2 = re.findall("\d+",l)
    command = re.findall("(turn on|turn off|toggle)",l)[0]
    y1 = int(y1)
    x1 = int(x1)
    y2 = int(y2)+1
    x2 = int(x2)+1
    for x in range(x1,x2):
        for y in range(y1,y2):
            lights[x][y] = light_mode(command,lights[x][y])

def part2(l:str):
    x1,y1,x2,y2 = re.findall("\d+",l)
    command = re.findall("(turn on|turn off|toggle)",l)[0]
    y1 = int(y1)
    x1 = int(x1)
    y2 = int(y2)+1
    x2 = int(x2)+1
    for x in range(x1,x2):
        for y in range(y1,y2):
            if command == "turn on":
                lights2[x][y] += 1
            elif command == "turn off":
                lights2[x][y] = max(lights2[x][y]-1,0)
            elif command == "toggle":
                lights2[x][y] += 2
            else:
                print("COMMAND NOT FOUND")


for l in lines:
    print(l)
    part1(l)
    part2(l)

ans1 = np.count_nonzero(lights)

for x in range(1000):
    for y in range(1000):
        ans2 += lights2[x][y]
        if lights2[x][y] < 0:
            print("ERR")

print("------")
print("ans1:", ans1)
print("ans2:", ans2)

# NOT
# 485167
# 377891?
# part2 
# 10829412 too low 
