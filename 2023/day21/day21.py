
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

que = []
for i in range(1,len(m[0]),2):
    que.append((0,i))
vis = []
i = 0
rang = 500
gridValue = 0
main = [0,0]
for _ in range(rang):
    while(len(que)>0):
        x,y = que.pop(0)
        if m[x][y] != "#":
            for dx,dy in d:
                if 0<=dx+x<len(m) and 0<=dy+y<len(m[0]) and m2[dx+x][dy+y] != "O" and m[dx+x][dy+y] != "#":
                    m2[dx+x][dy+y] = "O"
    for i in range(len(m2)):
        for k in range(len(m2[0])):
            if m2[i][k] == "O":
                que.append((i,k))
    if _ != rang-1:
        gridValue = np.count_nonzero(m2 == "O")
        print(_)
        if _%2 == 1:
            if main[0] != gridValue:
                main[0] = gridValue 
            else:
                break
        else:
            if main[1] != gridValue: 
                main[1] = gridValue
            else:
                break

        m2 = copy.deepcopy(m)
# ----
# %2 == 1 , %2 == 0
print(main)


for l in m2:
    print(l)

for i in range(len(m2)):
    for k in range(len(m2[0])):
        if m2[i][k] == "O":
            ans1 += 1

ans1 = len(que)


print("------")
print("ans1:", ans1)
print("ans2:", ans2)
