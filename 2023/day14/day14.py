import re
import math
import sys
import numpy as np
import copy
from itertools import combinations
import copy

F = open(sys.argv[1], "r")
lines = [l.strip() for l in F.readlines()]


ans2 = 0
global ans1
ans1 = 0
m = []
for l in lines:
    m.append([c for c in l])

m = np.array(m)


def cntLoad(m):
    i = m.shape[0]
    r = 0
    for x in m:
        for c in x:
            if c == "O":
                r += i 
        i-= 1 
    return r 

def printM(m):
    for x in m:
        print(x)
    print("---")    

def shift(inp):
    for i in range(len(inp)):
        if inp[i] == "O" and i != 0:
            k = i-1
            while(inp[k] == "." and k > -1):
                k -= 1 
            if k != i:
                inp[i] = "."
                inp[k+1] = "O"
    return inp 

def my_hash(x,c):
    return str(hash(bytes(x)))+"-#-"+str(c%4)

def my_hash2(x,cnt):
    r = "" 
    for c in x:
        r += "".join(c) + "," + "-" + str(cnt%4)
    return r 

def tiltNorth():
    mCPY = copy.deepcopy(m)
    for i in range(len(mCPY)):
        mCPY[:,i] = shift(mCPY[:,i])
        #printM(m)
    return cntLoad(mCPY)

def cycle():
    for c in range(4):
        if c%4 == 0:
            #print("north")
            for i in range(len(m)):
                m[:,i] = shift(m[:,i])
            #printM(m)

        if c%4 == 1:
            # west 
            #print("west")
            for i in range(len(m)):
                m[i] = shift(m[i]) 
                    
            #printM(m)
        if c%4 == 2:
            # south 
            #print("south")
            for i in range(len(m)):
                m[:,i][::-1] = shift(m[:,i][::-1])      
            #printM(m)
        if c%4 == 3:
            # east 
            #print("east")
            for i in range(len(m)):
                m[i][::-1] = shift(m[i][::-1])                     
            #printM(m)



CACH = {}

ans1 = tiltNorth()
# north, then west, then south, then east.
for c in range(1000000000):
    xoH = my_hash2(m,c)
    if xoH in CACH.keys():
        toDo = (1000000000-CACH[xoH][0])%abs(c-CACH[xoH][0])
        for _ in range(toDo):
            cycle()
        ans2 = cntLoad(m)
        break
    else:
        cycle()
        CACH[xoH] = (c,m)
print("----------")
print("ans1:",ans1)
print("ans2:",ans2)
