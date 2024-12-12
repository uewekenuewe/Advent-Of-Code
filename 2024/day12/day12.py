
import re
import sys
import numpy as np
import copy 
from math import sqrt
from shapely import Polygon


ans1 = 0
ans2 = 0


if len(sys.argv) > 1:
    filename = sys.argv[1]
    f = open(sys.argv[1], "r")
else:
    f = open("12", "r")

lines = [l.strip() for l in f.readlines()]
m = []
area = {}
for l in lines:
    print(l)
    m.append([x for x in l])
    for x in l:
        area[x] = []
m = np.array(m)


dd1 = ((-1,-1),(1,1),(-1,1),(1,-1),(0,-1),(0,1),(1,0),(-1,0))
dd2 = ((0,-1),(0,1),(1,0),(-1,0))
def findArea(p):
    x,y = copy.deepcopy(p)
    vv = m[x][y]
    q = [p]
    v = []
    while(len(q) > 0):
        x,y = q.pop()
        if (x,y) not in v:
            v.append((x,y))
            for d in dd2:
                dx,dy = d
                dx += x
                dy += y
                if 0<=dx<len(m) and 0<=dy<len(m[0]):
                    if m[dx][dy] == vv and (dx,dy) not in v:
                        q.append((dx,dy))
    return v 



def getPerimeter(a):
    x,y = a[0]
    v = m[x][y]
    a = sorted(a)
    r = 0
    for x,y in a:
        sides = 0
        for dx,dy in dd2:
            dx += x
            dy += y
            if 0<=dx<len(m) and 0<=dy<len(m[0]):
                if m[dx][dy] != v:
                    sides += 1
            else:
                sides += 1
        if sides > 0:
            r+= sides

    return r



globVis = []
for i in range(len(m)):
    for k in range(len(m[i])):
        if m[i][k] in area.keys():
            if (i,k) not in globVis:
                a = findArea((i,k))
                area[m[i][k]].append(a)
                globVis += a


for a in area:
    r= 0
    for x in area[a]:
        ans1 += (getPerimeter(x)*len(x))
        r += (getPerimeter(x)*len(x))
    print(a,r,area[a])
print("------")
print("ans1:", ans1)
print("ans2:", ans2)


