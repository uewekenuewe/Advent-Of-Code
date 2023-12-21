
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

que = [s]

vis = []
i = 0
rang = 64
gridValue = 0
main = [0,0]
def expand(matrix,steps):
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
            m2 = matrixCopy
            return np.count_nonzero(matrixCopy=="O")

for l in m2:
    print("".join(l))



ans1 = expand(m,64)


print("------")
print("ans1:", ans1)
print("ans2:", ans2)
