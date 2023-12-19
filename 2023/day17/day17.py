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

que = [(0,0)]
m2[0][0] = (0,(0,0))
vis = []
while(len(que) > 0):
    p = que.pop(0)
    x,y = p 
    if not p in vis:
        vis.append(p)
        for dd in D:
            dx,dy = dd 
            dx += x 
            dy += y 
            if 0<=dx<len(m) and 0<=dy<len(m[0]):
                wToadd = m2[x][y][0] + m[dx][dy]
                if m2[dx][dy][0] > wToadd:
                    m2[dx][dy] = (wToadd,(x,y))
                que.append((dx,dy))


for l in m2:
    print(l)