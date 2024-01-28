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
s = [0,1]
e = [0,0]
for l in lines:
    m.append([c for c in l])

m = np.array(m)
for i,c in enumerate(m[-1]):
    if c == '.':
        e = [m.shape[0]-1,i]
        break

d = [(1,0),(-1,0),(0,1),(0,-1)]

def BFS(s,m,v):
    q = [s]
    while(len(q) > 0):
        p = q.pop()
        if p not in v:
            x,y = p
            m[x][y] = 'O'
            v.append([x,y])
            for xx,yy in d:
                dx = x+xx
                dy = y+yy
                if 0<=dx<m.shape[0] and 0<=dy<m.shape[1]:
                    if m[dx][dy] == '.' and [dx,dy] not in v:
                        q.append([dx,dy])

    return (s,m,v)

q2 = [(s,m,[])]
vQue = []
ans1 = [0]


ii  = 0
while(len(q2)>0):
    ii += 1
    s1,m1,v1 = q2.pop()
    if e not in v1: #s1 not in vQue:
        vQue.append(s1)
        s2,m2,v2 = BFS(s1,m1,v1)
        if e in v2:
            ans1.append(len(v2))
        p = v2[-1]
        x,y = p 
        for xx,yy in d:
            dx = xx+x
            dy = yy+y 
            if 0<=dx<m.shape[0] and 0<=dy<m.shape[1] and m2[dx][dy] in ['v','<','>']:
                v2.append([dx,dy])
                m2[dx][dy] = 'O'
                dx += xx
                dy += yy 
                v2.append([dx,dy])
                m2[dx][dy] = 'O'
                break
        p = v2[-1]
        x,y = p 
        #for xx,yy in [(1,0),(0,1)]:
        for xx,yy in d:
            s3 = copy.deepcopy(s2)
            m3 = copy.deepcopy(m2)
            v3 = copy.deepcopy(v2)
            dx = xx+x
            dy = yy+y 
            if 0<=dx<m.shape[0] and 0<=dy<m.shape[1] and m3[dx][dy] in ['v','<','>']:
                m3[dx][dy] = '.'
                s3 = [dx,dy]
                q2.append((s3,m3,v3))
        

                    









print('------------')
print('ans1: ', max(ans1)-1)
print('ans2: ', ans2)
