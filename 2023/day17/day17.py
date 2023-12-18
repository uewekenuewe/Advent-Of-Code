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

ans1 = 0
ans2 = 0
m = []
for l in lines:
    m.append([int(x) for x in l])

m = np.array(m)
m2 = [[(float("inf"),(0,0)) for x in range(len(m[0]))] for _ in range(len(m))]
D = [(1,0),(-1,0),(0,1),(0,-1)]

def calcPath(path):
    r = 0
    for point in path:
        x,y = point
        r += m[x][y]
    return r 

edges = []
points = []
for i in range(len(m)):
    for k in range(len(m[0])):
        points.append((i,k))
        for dd in D:
            dx,dy = dd 
            if 0<=i+dx<len(m) and 0<=k+dy<len(m[0]):
                w = m[i+dx][k+dy]
                edges.append(((i,k),(i+dx,k+dy),m[i+dx][k+dy]))

def getAllEdges(p):
    r = []
    for e in edges:
        u,v,w = e
        if u == p:
            r.append(e)
    return r

m2[0][0] = (0,(0,0))


queue = [(0,0)]
visited = []


def getLastFour(point):
    prevX,prevY = point 
    r = []
    for i in range(4):
        r.append(m2[prevX][prevY][1])
        prevX,prevY = m2[prevX][prevY][1]
        if((prevX,prevY) == (0,0)):
            r.append((0,0))
            break 
    return r

def evalPrev(inp):
    dd = (0,0)
    ddCnt = 1
    for i in range(1,len(inp)):
        ddN = (inp[i][0]-inp[i-1][0],inp[i][1]-inp[i-1][1])
        print(ddN,dd)
        if dd == ddN:
            ddCnt += 1
        else:
            dd = ddN 
            ddCnt = 1
    return (ddCnt >= 3)

i = 0
while(len(queue) != 0):
    p = queue.pop(0)
    eds = getAllEdges(p)
    if not p in visited:
        for u,v,w in eds:
            vx,vy = v 
            ux,uy = u 
            wToSet = w+m2[ux][uy][0]
            if m2[vx][vy][0] > wToSet:
                print("backtracking")
                print(u,getLastFour(u),evalPrev(getLastFour(u)))
                m2[vx][vy] = (wToSet,u) 
            queue.append(v) 
    visited.append(p)

for x in m2:
    print(x)


path = []
queue = [m2[12][12][1]]
while(len(queue) > 0):
    x,y = queue.pop(0) 
    if (x,y) == (0,0):
        break
    else:
        path.append((x,y))
        queue.append(m2[x][y][1])

m3 = [["." for i in range(len(m[0]))] for k in range(len(m))]
for p in path:
    x,y = p 
    m3[x][y] = "#"

for l in m3:
    print(l)

print(evalPrev([(4, 10), (3, 10), (2, 10), (2, 9)]))
print(evalPrev([(9, 10), (8, 10), (7, 10), (6, 10)]))