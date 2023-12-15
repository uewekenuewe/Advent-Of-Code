import re
import math
import sys
import numpy as np
import copy
from itertools import combinations
import copy
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

def getBest(inp):
    if len(inp) == 0:
        return (0,0)
    maxAbs = -1
    maxAbsInd = -1
    for i,x in enumerate(inp):
        if abs(x[0]-x[1]) > maxAbs:
            maxAbs = abs(x[0]-x[1])
            maxInd = i
    return inp[maxInd]

def checkReflection(inp,l,r):
    if (abs(l-r)+1) % 2 == 1:
        return False
    for i in range(abs(l-r)):
        left = l + i
        right = r - i
        if not (inp[left] == inp[right]).all():
            return False
    return True

def cntDiff(l1,l2):
    r = 0
    for i in range(len(l1)):
        if l1[i] != l2[i]:
            r += 1
    return r

colsAns1 = 0
rowsAns1 = 0
for x,p in enumerate(pat):
    p_T = np.transpose(p)
    #print(x,p)
    # print(x,p_T)

    colsToAdd = 0
    rowsToAdd = 0

    vert = []
    hori = []

    for i in range(1,len(p)):
        k = len(p)-1
        if (p[i] == p[0]).all():
            if checkReflection(p,0,i):
                hori.append((1,i+1))
                break
        if (p[i-1] == p[k]).all():
            if checkReflection(p,i-1,k):
                hori.append((i,k+1))
                break
    for i in range(1,len(p_T)):
        k = len(p_T)-1
        if (p_T[i] == p_T[0]).all():
            if checkReflection(p_T,0,i):
                vert.append((1,i+1))
                break
        if (p_T[i-1] == p_T[k]).all():
            if checkReflection(p_T,i-1,k):
                vert.append((i,k+1))
                break

    if len(hori) > 0:
        i,k = hori[0]
        rowsAns1 += k - (abs(i-k) + 1) / 2
    else:
        i,k = vert[0]
        colsAns1 += k - (abs(i-k) + 1) / 2



colsAns2 = 0
rowsAns2 = 0
for x,p in enumerate(pat):
    p_T = np.transpose(p)

    colsToAdd = 0
    rowsToAdd = 0

    vert = []
    vert2 = []
    hori = []
    hori2 = []

    for i in range(1,len(p)):
        k = len(p)-1
        if (p[i] == p[0]).all():
            if checkReflection(p,0,i):
                hori.append((1,i+1))
        if np.count_nonzero(p[i] != p[0]) == 1 and (checkReflection(p,1,i-1) or abs(0-i) == 1):
                hori2.append((1,i+1))
        if (p[i-1] == p[k]).all():
            if checkReflection(p,i-1,k):
                hori.append((i,k+1))
        if np.count_nonzero(p[i-1] != p[k]) == 1 and (checkReflection(p,i,k-1) or abs(k-i-1) == 1):
                hori2.append((i,k+1))

    for i in range(1,len(p_T)):
        k = len(p_T)-1      
        if (p_T[i] == p_T[0]).all():
            if checkReflection(p_T,0,i):
                vert.append((1,i+1))
        if np.count_nonzero(p_T[i] != p_T[0]) == 1 and checkReflection(p_T,1,i-1):
                vert2.append((1,i+1))                
        if (p_T[i-1] == p_T[k]).all():
            if checkReflection(p_T,i-1,k):
                vert.append((i,k+1))
        # if np.count_nonzero(p_T[i-1] != p_T[k]) == 1 and (checkReflection(p,i+1,k-1) or abs(k-i-1) == 1):
                # vert2.append((i,k+1))

    print(x,hori2,vert2)
    if len(hori) > 0:
        i,k = hori[0]
        rowsAns2 += k - (abs(i-k) + 1) / 2
    elif len(vert) > 0:
        i,k = vert[0]
        colsAns2 += k - (abs(i-k) + 1) / 2

#-------------------
# 30445 to high
# 24219 to high
# 21153 to high
# 25792 to high
# 28955 to high
# 30261 to ????
# 11687 
ans1 = colsAns1 + 100 * rowsAns1
ans2 = colsAns2 + 100 * rowsAns2
print("------")
print("ans1:", ans1)
print("ans2:", ans2)