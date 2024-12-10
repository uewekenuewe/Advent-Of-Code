import re
import sys
import numpy as np
import copy 

ans1 = 0
ans2 = 0

if len(sys.argv) > 1:
    filename = sys.argv[1]
    f = open(sys.argv[1], "r")
else:
    f = open("10", "r")

ends = []
lines = [l.strip() for l in f.readlines()]
m = []
mcpy = []
for l in lines:
    m.append([int(x) for x in l])
    mcpy.append(["." for _ in l])

starts = []
for i in range(len(m)):
    for k in range(len(m[i])):
        if m[i][k] == 0:
            starts.append((i,k))
        if m[i][k] == 9:
            ends.append((i,k))

dd = [(-1,0),(1,0),(0,-1),(0,1)]
ans1arr = []
for s in starts:
    mtemp = copy.deepcopy(mcpy)
    sx,sy = s 
    v = []
    q = [s]
    arr1temp = []
    i = 0
    while(len(q) > 0):
        x,y = q.pop()
        mtemp[x][y] = m[x][y]
        v.append((x,y))
        if i != 0 and m[x][y] == 0:
            continue
        else:
            for d in dd:
                dx,dy = d
                dx += x
                dy += y 
                if 0<= dx < len(m) and 0<=dy  < len(m):
                    if m[dx][dy] != 0:
                        if (m[dx][dy] - m[x][y]) == 1 and (dx,dy) not in v:
                            q.append((dx,dy))
                            if m[dx][dy] == 9 and m[x][y] == 8:
                                ans1arr.append((dx,dy,x,y))
    anstemp = 0
    for x in mtemp:
        anstemp += x.count(9)
    ans1+=anstemp

ans2arr = []
for s in starts:
    mtemp = copy.deepcopy(mcpy)
    sx,sy = s 
    sans = 0
    for e in ends:
        v = []
        q = [s]
        arr2temp = []
        i = 0
        while(len(q) > 0):
            x,y = q.pop()
            mtemp[x][y] = m[x][y]
            v.append((x,y))
            if i != 0 and m[x][y] == 0:
                continue
            if (x,y) == e:
                sans += 1
            else:
                for d in dd:
                    dx,dy = d
                    dx += x
                    dy += y 
                    if 0<= dx < len(m) and 0<=dy  < len(m):
                        if m[dx][dy] != 0:
                            if (m[dx][dy] - m[x][y]) == 1 and (dx,dy) not in v:
                                q.insert(0,(dx,dy))
    print(s,sans)
    ans2+=sans



# 281
print("------")
print("ans1:", ans1)
print("ans2:", ans2)


