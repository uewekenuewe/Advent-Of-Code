
import re
import sys
import numpy as np
import copy 
from math import sqrt
from collections import deque
import shapely.geometry
import cv2

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
dd2 = ((-1,0),(0,1),(1,0),(0,-1))
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

def checkDirection(dd,pp):
    xx,yy = pp
    dx,dy = dd
    dx+=xx
    dy+=yy
    return 0<=dx<len(m) and 0<=dy<len(m[0]) and m[dx][dy] == m[xx][yy]

def getCorner(a):
    x,y = a[0]
    r = 0
    for x,y in a:
        corners = 0
        for ind in range(len(dd2)):
            d1 = dd2[ind]
            d2 = dd2[(ind+1) %4]
            if not checkDirection(d1,(x,y)) and not checkDirection(d2,(x,y)):
                corners += 1
            d3 = d1[0]+d2[0],d1[1]+d2[1]
            if checkDirection(d1,(x,y)) and checkDirection(d2,(x,y)) and not checkDirection(d3,(x,y)):
                corners += 1
        r+= corners

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






for a in area:
    for x in area[a]:
        ans2 += len(x) * getCorner(x)

print("------")
print("ans1:", ans1)
print("ans2:", ans2)
