
import re
import math
import sys
import numpy as np
import copy 
ans1 = 0
ans2 = 0

F = open(sys.argv[1], "r")
lines = [l.strip() for l in F.readlines()]
m = []
s = (0,0)
for i,l in enumerate(lines):
    m.append([x for x in l])
    for k in range(len(l)):
        if l[k] == "S":
            s = (i,k)

m = np.array(m)
m2 = copy.deepcopy(np.array(m))
d = [(1,0),(0,1),(-1,0),(0,-1)]

print("START:",s)

que = [s]

vis = []
i = 0
rang = 64
gridValue = 0
main = [0,0]
def expand(matrix,steps,p=False):
    matrixCopy = copy.deepcopy(matrix)

    for _ in range(steps):
        while(len(que)>0):
            x,y = que.pop(0)
            if matrix[x][y] != "#":
                for dx,dy in d:
                    if 0<=dx+x<len(matrix) and 0<=dy+y<len(matrix[0]) and matrixCopy[dx+x][dy+y] != "O" and matrix[dx+x][dy+y] != "#":
                        matrixCopy[dx+x][dy+y] = "O"
        for i in range(len(matrixCopy)):
            for k in range(len(matrixCopy[0])):
                if matrixCopy[i][k] == "O":
                    que.append((i,k))
        if _ != steps-1:
            matrixCopy = copy.deepcopy(matrix)
        else:
            if p:
                for l in matrixCopy:
                    print("".join(l))
            return np.count_nonzero(matrixCopy=="O")

def countExpand(matrix,steps,s):
    mxo  = [["." for x in range(100)] for y in range(100)]
    offX,offY = s

    r = 1
    k = 0
    k2 = 0
    up = steps+1
    down = -1*steps
    points = []
    for _ in range(int(steps+1)):
        for i in range(down,up,2):
            x = (offX + i) 
            y = (offY + k) 
            r += 1            
            points.append((x,y))
            if k2 <= -1: 
                y = (offY + k2)
                points.append((x,y))
                r += 1

        k += 1 
        up -= 1 
        down += 1 
        k2 -= 1



    # print(len(points),len(list(set(points))))
    # print(points)
    for x,y in points:
            mxo[x][y] = "X"
    mxo[s[0]][s[1]] = "S"

    s2 = (0,0)
    for i in range(len(m)):
        for k in range(len(m[0])):
            if m[i][k] == "S":
                s2 = (i,k)
                break 
        if s2 != (0,0):
            break 
    
    offX = abs(s2[0]-s[0])
    offY = abs(s2[1]-s[1])

    for i in range(len(m)):
        for k in range(len(m[0])):
            if m[i][k] == "#":
                mxo[i+offX][k+offY] = "#"

    for l in mxo:
        print("".join(l))
    mxo = np.array(mxo)
    print("np cnt:" , np.count_nonzero(mxo == "X"))
    return r


s = [50,50]
#ans1 = expand(m,64)

print(countExpand(m,6,s))

print("------")
print("ans1:", ans1)
print("ans2:", ans2)
