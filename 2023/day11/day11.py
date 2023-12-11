import re
import math
import sys
import numpy as np
import copy 
import networkx as nx

ans1 = 0
ans2 = 0

F = open(sys.argv[1], "r")
lines = [l.strip() for l in F.readlines()]
lines2 = []

cols = []
rows = []


for l in lines:
    lines2.append(l)
    if len(set(l)) == 1 :
        lines2.append(l)
lines = lines2
lines2 = []
for y in range(len(lines[0])):
    l = "".join([lines[x][y] for x in range(len(lines))])
    lines2.append(l)
    if len(set(l)) == 1: 
        lines2.append(l)

    #print(y,l)

lines = np.array(lines2).T
M = []
G = []
i = 0
for l in lines:
    M.append([c for c in l])
    for k in range(len(l)):
        if M[i][k] == "#":
            G.append((i,k))
    i+=1

#for g in G:
#    graph.add_node(g)
pairs = []
for i in range(len(G)):
    for k in range(i+1,len(G)):
        x1,y1 = G[i]
        x2,y2 = G[k]
        w = abs(x1-x2) + abs(y1-y2)
        ans1+=w

print("------")
print("ans1:", ans1)
ans2 = 0

F = open(sys.argv[1], "r")
lines = [l.strip() for l in F.readlines()]
cols = []
rows = []
for i in range(len(lines)):
    l = lines[i]
    if len(set(l)) == 1:
        rows.append(i)
for y in range(len(lines[0])):
    l = "".join([lines[x][y] for x in range(len(lines))])
    if len(set(l)) == 1: 
        cols.append(y)

M = []
G = []
i = 0
for l in lines:
    M.append([c for c in l])
    for k in range(len(l)):
        if M[i][k] == "#":
            G.append((i,k))
    i+=1
pairs = []
factor = 1000000
for i in range(len(G)):
    for k in range(i+1,len(G)):
        x1,y1 = G[i]
        x2,y2 = G[k]
        w = abs(x1-x2)+abs(y1-y2)
        for c in cols:
            if c in range(min(y1,y2),max(y1,y2)+1):
                w += factor - 1 
        for r in rows:
            if r in range(min(x1,x2),max(x1,x2)+1):
                w += factor -1 
        ans2+=w

print("ans2:", ans2)
