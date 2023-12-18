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

def expand1(p,l,r):
    if l == 0 or r == len(p)-1:
        return True 
    else:
        for i in range(min(abs(l),abs(r-len(p)+1))):
            l-=1 
            r+=1 
            if (p[l] != p[r]).any():
                return False 
    return True

def expand2(p,l,r):
    smug = 0
    for i in range(min(abs(l),abs(r-len(p)+1))):
        l-=1 
        r+=1 
        if np.count_nonzero(p[l] != p[r]) > 1:
            return False 
        elif np.count_nonzero(p[l] != p[r]) == 1:
            smug+=1 
        if smug > 1:
            return False 
    if smug != 1:
        return False 
    return True


colsAns1 = 0
colsAns2 = 0
rowsAns1 = 0
rowsAns2 = 0


for x,p in enumerate(pat):
    p_T = np.transpose(p)
    rr = []
    cc = []

    # PART -- 1
    for i in range(len(p)-1):
        if (p[i] == p[i+1]).all() and expand1(p,i,i+1):
            rowsAns1 += i+1
    for i in range(len(p_T)-1):
        if (p_T[i] == p_T[i+1]).all() and expand1(p_T,i,i+1):
            colsAns1 += i+1

    # PART -- 2
    for i in range(len(p)-1):
        if( np.count_nonzero(p[i] != p[i+1]) == 1) and expand1(p,i,i+1):
            rr.append(i+1)
            rowsAns2 += i+1
        elif( (p[i] == p[i+1]).all() and expand2(p,i,i+1)):
            rr.append(i+1)
            rowsAns2 += i+1

    for i in range(len(p_T)-1):
        if( np.count_nonzero(p_T[i] != p_T[i+1]) == 1) and expand1(p_T,i,i+1):
            cc.append(i+1)
            colsAns2 += i+1
        elif( (p_T[i] == p_T[i+1]).all() and expand2(p_T,i,i+1)):
            cc.append(i+1)
            colsAns2 += i+1        
    
    print(rr,cc)
ans1 = colsAns1 + 100 * rowsAns1
ans2 = colsAns2 + 100 * rowsAns2
print("------")
print("ans1:", ans1, ans1==27664)
print("ans2:", ans2, ans2==30842)

# ans2 = 33608 falsch
# ans2 = 45013 falsch
# ans2 = 45487 falsch