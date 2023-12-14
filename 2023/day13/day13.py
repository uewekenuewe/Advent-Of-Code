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
colsAns2 = 0
rowsAns1 = 0
rowsAns2 = 0

def expand(p,l,r):
    if l == 0 or r == len(p)-1:
        return True 
    else:
        for i in range(min(abs(l),abs(r-len(p)+1))):
            l-=1 
            r+=1 
            if (p[l] != p[r]).any():
                return False 
    return True

def findSmudge(inp):
    inp_T = np.transpose(inp)
    xo = 0
    # zeilen
    for i in range(len(inp)-1):
        if np.count_nonzero((inp[i] != inp[0])) == 1:
            xo += 1 
    for i in range(len(inp_T)-1):
        if np.count_nonzero((inp_T[i] != inp_T)) == 1:
            xo += 1

    return(xo )


for x,p in enumerate(pat):
    p_T = np.transpose(p)
    smudge = 0
    for i in range(len(p)-1):
        if (p[i] == p[i+1]).all() and expand(p,i,i+1):
            rowsAns1 += i+1
    for i in range(len(p_T)-1):
        if (p_T[i] == p_T[i+1]).all() and expand(p_T,i,i+1):
            colsAns1 += i+1

    
ans1 = colsAns1 + 100 * rowsAns1
ans2 = colsAns2 + 100 * rowsAns2
print("------")
print("ans1:", ans1, ans1==27664)
print("ans2:", ans2)