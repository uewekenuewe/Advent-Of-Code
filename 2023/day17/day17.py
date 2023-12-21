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
mVis = np.array([["#" for i in range(len(m[0]))] for k in range(len(m))])
mw = np.array([[float("inf") for i in range(len(m[0]))] for k in range(len(m))])
move = [[(0,0) for i in range(len(m[0]))] for k in range(len(m))]
print(m.shape,mw.shape)
D = [(1,0),(-1,0),(0,1),(0,-1)]

def invert(p):
    return [p[0]*-1,p[1]*-1]

que = [(0,0)]
vis = []
mw[0][0] = 0
while(len(que)>0):
    x,y = que.pop(0)
    if not (x,y) in vis:
        for dx,dy in D:
            if 0<=x+dx<len(m) and 0<=y+dy<len(m[0]):
                if mw[x][y] + m[dx+x][dy+y] < mw[dx+x][dy+y]:
                    mw[dx+x][dy+y] =  mw[x][y] + m[dx+x][dy+y]
                    move[dx+x][dy+y] = invert((dx,dy))
                que.append((dx+x,dy+y))
    vis.append((x,y))

for l in mw:
    print(l)
for l in move:
    print(l)

printLook = {
    (-1,0) :"v",
    (1,0) :"^",
    (0,-1) :"<",
    (0,1) :">",
    (0,0) :"#"
}

for i in range(len(mVis)):
    for k in range(len(mVis[0])):
        print(printLook[move[i][k]],"",end="")
    print("")