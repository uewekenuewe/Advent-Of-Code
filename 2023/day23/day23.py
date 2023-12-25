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
m = []
s = (1,0)
for l in lines:
    m.append([c for c in l])

d = [(1,0),(-1,0),(0,1),(0,-1)]

def getPath(matrix,start,vis):
    que = [start]
    matrix = np.array(matrix)
    while(len(que) > 0):
        x,y = que.pop()
        if (x,y) not in vis:
            if matrix[x][y] != "#":
                matrix[x][y] = "O"
            for dx,dy in d:
                if 0<=dx+x<len(matrix) and 0<=dy+y<len(matrix[0]):
                    if matrix[dx+x][dy+y] in ">v":
                        que = []
                        matrix[dx+x][dy+y] = "O"
                        vis.append((dx+x,dy+y))
                        start = (2*dx+x,2*dy+y)
                        break
                    if matrix[dx+x][dy+y] == ".":
                        que.append((dx+x,dy+y))
            vis.append((x,y))
    return (matrix,start,vis)

def printM(matrix):
    for l in matrix:
        print("".join(l))


v = []
m,v,s = getPath(m,s,v)
printM(m)
# que2 = [(m,s,v)]
# ans1Arr = []
# end = (len(m)-1,len(m[0])-2)



# while(len(que2) > 0):
#     m,s,v = que2.pop(0)
#     x,y = s 
#     if end in v:
#         print(len(set(v)))
#         ans1Arr.append(len(set(v)))
#     else:
#         m[x][y] = "O"
#         v.append((x,y))
#         for dx,dy in d:
#             if 0<=dx+x<len(m) and 0<=dy+y<len(m[0]):   
#                 if m[dx+x][dy+y] in ">v":
#                     mcpy = copy.deepcopy(m)
#                     vcpy = copy.deepcopy(v)
#                     scpy = (x+dx,y+dy)
#                     m2,v2,s2 = getPath(mcpy,scpy,vcpy)
#                     printM(m2)
#                     que2.append((m2,v2,s2))



print("------")
print("ans1:", ans1)
print("ans2:", ans2)
