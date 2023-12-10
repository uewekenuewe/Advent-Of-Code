import re
import copy
import math
import sys
import numpy as np

ans1 = 0
ans2 = 0

F = open(sys.argv[1], "r")
lines = [l.strip() for l in F.readlines()]
m = []
s = (0,0)
for l in lines:
    m.append([c for c in l])
    print(l)
    for c in l:
        if c == "S":
            s = (lines.index(l),l.index(c))

#| is a vertical pipe connecting north and south.
#- is a horizontal pipe connecting east and west.
#L is a 90-degree bend connecting north and east.
#J is a 90-degree bend connecting north and west.
#7 is a 90-degree bend connecting south and west.
#F is a 90-degree bend connecting south and east.
visited = []
toVisit = []
for dd in [1,-1]:
    x = dd+s[0]
    y = dd+s[1]
    if 0<=x<len(m):
        toVisit.append((x,s[1]))
    if 0<=y<len(m[0]):
        toVisit.append((s[0],y))

def checkbound(point):
    x,y = point
    if 0<=x<len(m) and 0<=y<len(m[0]):
        return True 
    else:
        return False 
while(len(toVisit)>0):
    toVisit2 = []
    for p in toVisit: 
        x,y = p 
        if not p in visited and checkbound(p) and m[x][y] != ".": 
            if m[x][y] == "-":
                toVisit2.append((x,y+1))
                toVisit2.append((x,y-1))
            if m[x][y] == "|":
                toVisit2.append((x+1,y)) 
                toVisit2.append((x-1,y)) 
            if m[x][y] == "J":
                toVisit2.append((x-1,y)) 
                toVisit2.append((x,y-1)) 
            if m[x][y] == "F":
                toVisit2.append((x,y+1))
                toVisit2.append((x+1,y))
            if m[x][y] == "7":
                toVisit2.append((x+1,y))
                toVisit2.append((x,y-1))
            if m[x][y] == "L":
                toVisit2.append((x,y+1))
                toVisit2.append((x-1,y))
            visited.append(p)
    toVisit = toVisit2

print("---")
dotCount = len(m) * len(m[0]) - len(visited) 
ans1 = len(visited)/2
toVisit = []
for x in range(len(m)):
    for y in range(len(m[0])):
        if m[x][y] == ".":
            m[x][y] = " "
        if not (x,y) in visited:
            m[x][y] = "#"
        if m[x][y] == "#":
            toVisit.append((x,y))
def resolveValue(point):
    x,y = point
    return m[x][y]

print("start:" ,s )
m[s[0]][s[1]] = "-"
for i,l in enumerate(m):
    x = []
    for c in l:
        x.append(c)
        x.append(" ")
    m[i] = x

M2 = []
for x in m:
    M2.append(x)
    M2.append([" " for _ in range(len(m[0]))])
m = M2
for x in range(len(m)):
    for y in range(len(m[0])):
        if m[x][y] in ["S","L","F","-"] and m[x][y+1] == " ":
            m[x][y+1] = "-" 
        if m[x][y] in ["S","F","7","|"] and m[x+1][y] == " ":
            m[x+1][y] = "|"


visited = []
toVisit = []
for i in range(len(m[0])):
    if m[0][i] == "#":
        toVisit.append([0,i])
    if m[-1][i] == "#":
        toVisit.append([len(m)-1,i])
for i in range(len(m)):
    if m[i][0] == "#":
        toVisit.append([i,0])
    if m[i][-1] == "#":
        toVisit.append([i,len(m[i])-1])
while(len(toVisit)>0):
    toVisit2 = []
    for p in toVisit: 
        x,y = p 
        if not p in visited:
            for d in [-1,1]:
                help = (x+d,y)
                if checkbound(help):
                    if m[x+d][y] == "#" or m[x+d][y] == " ":
                        toVisit2.append((x+d,y))
            for d in [-1,1]:
                help = (x,y+d)
                if checkbound(help):
                    if m[x][y+d] == "#" or m[x][y+d] == " ":
                        toVisit2.append((x,y+d))
        visited.append(p)
    toVisit = toVisit2

ans2 = dotCount
for p in visited:
    x,y = p
    if m[x][y] == "#":
        ans2-=1 
        m[x][y] = "O"
for l in range(len(m)):
    print("".join(m[l]))




print("---")
print("ans1:", ans1)
print("ans2:", ans2,dotCount)
