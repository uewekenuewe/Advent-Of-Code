import re
import math
import sys
import numpy as np
import copy
from itertools import combinations
import copy
import networkx as nx


F = open(sys.argv[1], "r")
lines = [l.strip() for l in F.readlines()]

# up (U), down (D), left (L), or right (R)

ans1 = 0
ans2 = 0
m = []
dig = []
for l in lines:
    dig.append(l.split())

digger = [0,0]
maxX = -1
minX = 99999
maxY = -1
minY = 99999
cords = []
for d in dig:
    direction,length,color = d 
    length = int(length)

    if direction == "R":
        for i in range(digger[1],digger[1]+length):
            cords.append((digger[0],i))
        digger[1] += length
    if direction == "D":
        for i in range(digger[0],digger[0]+length):
            cords.append((i,digger[1]))     
        digger[0] += length 
    if direction == "L":
        for i in range(digger[1],digger[1]-length,-1):
            cords.append((digger[0],i))           
        digger[1] -= length 
    if direction == "U":
        for i in range(digger[0],digger[0]-length,-1):
            cords.append((i,digger[1]))           
        digger[0] -= length
    


    maxX = max(maxX,digger[0])
    minX = min(minX,digger[0])
    minY = min(minY,digger[1])
    maxY = max(maxY,digger[1])



print(minX,minY,maxX,maxY)
m2 = np.array([["." for i in range(abs(minY-maxY)+1)] for k in range(abs(minX-maxX)+1)])

m = copy.deepcopy(m2)

print(m.shape)

edge = []

ans1 = 0
for c in cords:
    x,y = c 
    m[x+abs(minX)][y+abs(minY)] = "#"
    edge.append((x+abs(minX),y+abs(minY)))


openClose = False
for i in range(len(m)):
    ind = 0
    x = "".join(m[i])
    while(x.find("#",ind) != -1):
        first = x.find("#",ind)
        last = x.find("#",first+1)
        ans1+= abs(first-last+1)
        ind = last+1
        print(x,first,last,x[first:last+1])
        if last == -1:
            break


for l in m:
    print(l)


# 62114 to high
print(np.count_nonzero(m == "#"))
print("ans1:",ans1)


# -186 -288 88 200
# (275, 489)
# 3662
# ans1: 98253