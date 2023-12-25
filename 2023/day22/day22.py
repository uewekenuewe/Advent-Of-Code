import re
import math
import sys
import numpy as np
import copy 
from shapely.geometry import LineString

ans1 = 0
ans2 = 0

F = open(sys.argv[1], "r")
lines = [l.strip() for l in F.readlines()]
bricks = []
cnt = 0
maxZ = -1
for l in lines:
    p1,p2 = l.split("~")
    p1 = [int(x) for x in p1.split(",")]
    p2 = [int(x) for x in p2.split(",")]
    bricks.append((p1,p2))
    maxZ = max([maxZ,p1[2],p2[2]])

levels = [[] for _ in range(maxZ+1)]

def line_intersection(line1, line2):
    # line 1 or line 2 is only a point
    if (line1[0][0],line1[0][1]) == (line1[1][0],line1[1][1]):
        if line1[0][0] in range(line2[0][0],line2[1][0]+1) and line1[0][1] in range(line2[0][1],line2[1][1]+1):
            return True
    elif (line1[0][0],line1[0][1]) == (line1[1][0],line1[1][1]) and (line2[0][0],line2[0][1]) == (line2[1][0],line2[1][1]):
        if (line1[0][0],line1[0][1]) == (line2[0][0],line2[0][1]):
            return True
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])
    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
        return False 
    else:
        return True


for b in bricks:
    bs,be = b 
    if bs[2] == be[2]:
        levels[bs[2]].append(b)
    else:
        levels[bs[2]].append(b)
        levels[be[2]].append(b)

def isVertical(brick):
    p1 = (brick[0][0],brick[0][1])
    p2 = (brick[1][0],brick[1][1])
    return p1 == p2
# laufe von level 2 hoch 
# für jedes b laufe runter 
xxx = 0
def fall(stack,limit=-1):
    change = True 
    if limit == -1:
        while(change):
        # for _ in range(3):
            change = False
            for i in range(2,len(stack)):
                pushDown = []
                for b1 in stack[i]:
                    noIntersect = True 
                    for b2 in stack[i-1]:
                        if line_intersection(b1,b2):
                            noIntersect = False 
                            break 
                    if noIntersect:
                        if isVertical(b1):
                            stack[b1[0][2]-1].append(b1)
                            stack[b1[1][2]].remove(stack[b1[1][2]].index(b1)) #append(b1)
                            change = True 
                        else:
                            pushDown.append(b1)
                if len(pushDown) > 0:
                    change = True 
                stack[i-1] += pushDown
                for x in pushDown:
                    del stack[i][stack[i].index(x)]
        return stack
    else:
        change = False
        for _ in range(limit):
            for i in range(2,len(stack)):
                pushDown = []
                for b1 in stack[i]:

                    noIntersect = True 
                    for b2 in stack[i-1]:
                        if line_intersection(b1,b2):
                            noIntersect = False 
                            break 
                    if noIntersect:
                        pushDown.append(b1)
                if len(pushDown) > 0:
                    change = True 
                stack[i-1] += pushDown
                for x in pushDown:
                    del stack[i][stack[i].index(x)]        
        return change 
    
            
levels = fall(levels)




for i in range(len(levels)):
    print(i,levels[i]) 

# too high 1141
print("------")
print("ans1:", ans1)
print("ans2:", ans2)
