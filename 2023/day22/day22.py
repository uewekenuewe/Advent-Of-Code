
import re
import math
import sys
import numpy as np
import copy 
from operator import itemgetter

ans1 = 0
ans2 = 0

F = open(sys.argv[1], "r")
lines = [l.strip() for l in F.readlines()]
bricks = []
for i,l in enumerate(lines):
    #print(l)
    b1,b2 = l.split("~")
    bricks.append(([int(x) for x in b1.split(",")],[int(x) for x in b2.split(",")]))


def overLap(e1,e2):
    e1s,e1e = e1
    e2s,e2e = e2

    print(min(e1s[0],e1e[0]) , "-->",max(e1s[0],e1e[0]))
    print(min(e1e[1],e1s[1]) , "-->",max(e1e[1],e1s[1]))

    


    return False 




maxZ = -1
vis = []
levels = [[] for _ in range(305)]
for b in bricks:
    x1,y1,z1 = b[0]
    x2,y2,z2 = b[1]
    if z1 == 1 or z2 == 1:
        vis.append(b)
        print(b)
        levels[0].append((b))

    maxZ = max([maxZ,z1,z2])



print(maxZ)
print(levels[0])

#1,0,1~1,2,1   <- A
#0,0,2~2,0,2   <- B
#0,2,3~2,2,3   <- C

overLap(((1,0,1),(1,2,1)),((0,0,2),(2,0,2)))
# for b in bricks:
#     x1,y1,z1 = b[0]
#     x2,y2,z2 = b[1]
#     if z1 == 1 or z2 == 1:
#         print(b)
#         vis.append(b)        


print("------")
print("ans1:", ans1)
print("ans2:", ans2)
