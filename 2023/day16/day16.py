import re
import math
import sys
import numpy as np
import copy
from itertools import combinations
import copy

F = open(sys.argv[1], "r")
lines = [l.strip() for l in F.readlines()]

ans1 = 0
ans2 = 0
m = []
beams = [(0,0,(0,1))]
for l in lines:
    m.append([c for c in l])
    
m = np.array(m)
m2 = copy.deepcopy(m)

dMap = {
    "/" : { (1,0) : (0,-1),
            (-1,0) : (0,1),
            (0,1) : (-1,0),
            (0,-1) : (1,0)
        },
    "\\" : {
            (1,0) : (0,1),
            (-1,0) : (0,-1),
            (0,1) : (1,0),
            (0,-1) : (-1,0)        
    },
    "-" : {
            (1,0) : (1,0), 
            (-1,0) : (-1,0),
            (0,1) : (0,1),
            (0,-1) : (0,-1)        
    },
    "|" : {
            (1,0) : (1,0),
            (-1,0) : (-1,0),
            (0,1) : (0,1),
            (0,-1) : (0,-1)        
    }

}

m = np.array(m)

def enlight(beam):
    queue = [beam]
    branches = []
    m2 = copy.deepcopy(m)
    while(len(queue) > 0):
        x,y,(dx,dy) = queue.pop(0)
        if not (x,y,(dx,dy)) in branches:
            branches.append((x,y,(dx,dy)))
            while(-3<x<len(m)+2 and -3< y <len(m[0])+2):
                if 0<=x<len(m) and 0<=y<len(m[0]):
                    m2[x][y] = "#"
                    if m[x][y] in ["|","/","\\","-"]:
                        dx,dy = dMap[m[x][y]][(dx,dy)]
                        if m[x][y] == "-":
                            if (dx,dy) == (1,0) or (dx,dy) == (-1,0):
                                queue.append((x,y,(0,1)))
                                queue.append((x,y,(0,-1)))
                                break
                        elif m[x][y] == "|":
                            if (dx,dy) == (0,1) or (dx,dy) == (0,-1):
                                queue.append((x,y,(1,0)))
                                queue.append((x,y,(-1,0)))
                                break 
                x += dx 
                y += dy
    return np.count_nonzero(m2=="#")

ans2Arr = [-1]
for i in range(len(m[0])):
    ans2Arr.append(enlight((i,0,(0,1))))
    ans2Arr.append(enlight((0,i,(-1,0))))    
    ans2Arr.append(enlight((i,m.shape[1]-1,(0,-1))))
    ans2Arr.append(enlight((m.shape[0]-1,i,(1,0))))
ans1 = enlight((0,0,(0,1)))
ans2 = max(ans2Arr)
print("-----")
print("ans1",ans1,ans1==7482)
print("ans2",ans2)
