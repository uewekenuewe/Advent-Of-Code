import re
import math
import sys
import numpy as np
import copy 
from itertools import combinations 
ans1 = 0
ans2 = 0

F = open(sys.argv[1], "r")
lines = [l.strip() for l in F.readlines()]

pat = []
arr = []
for l in lines:
    l = [c for c in l]
    if "#" in l or "." in l:
        arr.append(l)
    else:
        pat.append(np.array(arr))
        arr = []
pat.append(np.array(arr))


rows = 0
cols = 0

for x,p in enumerate(pat):
    p_T = np.transpose(p)
    #print(x,p)
    # print(x,p_T)

    colsToAdd = 0
    rowsToAdd = 0

    vert = (-1,-1)
    hori = (-1,-1)

    found = False
    for i in range(len(p_T)):
        for k in range(i+1,len(p_T)):
            if (p_T[i] == p_T[k] ).all() and abs(i-k) == 1:
                # print(i,k,p_T[i])
                vert = (i,k)
                cols += abs(i-k)
                found = True 
            if found:
                break 
        if found: 
            break 
    
    found = False 
    for i in range(len(p)):
        for k in range(i+1,len(p)):
            if (p[i] == p[k] ).all() and abs(i-k) == 1:
                # print(i,k,p_T[i])
                hori = (i,k)
                rows += abs(i-k)
                found = True 
            if found:
                break 
        if found: 
            break         

print(rows,cols)
ans1 = cols + 100* rows
print("------")
print("ans1:", ans1)
print("ans2:", ans2)
