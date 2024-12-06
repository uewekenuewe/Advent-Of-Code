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
    f = open("06", "r")

lines = [l.strip() for l in f.readlines()]
m = []
for l in lines:
    m.append([x for x in l])

m = np.array(m)

s = [0,0]
for i in range(len(m)):
    for k in range(len(m[i])):
        if m[i][k] == '^':
            s = [i,k]
            break

dots = []
for i in range(len(m)):
    for k in range(len(m)):
        if m[i,k] == '.':
            dots.append((i,k))

def runGrind(m,s, limit):
    running = True
    ind = 0
    dd = [(-1,0),(0,1),(1,0),(0,-1)]
    xo = 0
    while(running):
        m[s[0],s[1]] = 'X'
        x,y = dd[ind]
        dx = s[0]+x
        dy = s[1]+y
        if 0<=dx<len(m) and 0<=dy<len(m):
            if m[dx,dy] == '#':
                ind = (ind+1) % 4
            else:
                s = [dx,dy]
        else:
            running = False
        xo += 1
        if xo > limit:
            return -1
    return np.count_nonzero(m == 'X')


for d in dots:
    mcpy = copy.deepcopy(m)
    mcpy[d[0],d[1]] = '#'
    if runGrind(mcpy,s,10000) == -1:
        ans2+= 1



ans1 = runGrind(m,s,10000)

print("------")
print("ans1:", ans1)
print("ans2:", ans2)


