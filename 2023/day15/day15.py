import re
import math
import sys
import numpy as np
import copy
from itertools import combinations
import copy

F = open(sys.argv[1], "r")
lines = [l.strip() for l in F.readlines()]

exex = "HASH"
currVal = 0

def hashAlgo(inp,currVal):
    return ((currVal+ord(inp))*17)%256
    
HASHMAP = [({},[]) for _ in range(256)]

def remove(box,lense):
    l,f = lense
    if l in HASHMAP[box][0].keys():
        ind = HASHMAP[box][0][l]
        for i in range(len(HASHMAP[box][1])):
            x,y = HASHMAP[box][1][i]
            if y == l:
                ind = i 
                break
        del HASHMAP[box][1][ind]
        del HASHMAP[box][0][l]
        

def add(box,lense):
    l,f = lense
    if l in HASHMAP[box][0].keys():
        for i in range(len(HASHMAP[box][1])):
            x,y = HASHMAP[box][1][i]
            if y == l:
                HASHMAP[box][1][i] = (f,l)
                break        
    else:
        HASHMAP[box][1].append((f,l))
        HASHMAP[box][0][l] = 1

ans2 = 0
ans1 = 0
for l in lines:
    arr = l.split(",")
    for x in arr:
        for c in x:
            currVal = hashAlgo(c,currVal)
        ans1 += currVal

        boxId = 0
        for c in x[:2]:
            boxId = hashAlgo(c,boxId)

        if "-" in x:
            l,f = x.split("-")
            remove(boxId,(l,f))
        elif "=" in x:
            l,f = x.split("=")
            add(boxId,(l,f))

        print("---")
        print(HASHMAP[0])
        print(HASHMAP[1])
        print(HASHMAP[2])
        print(HASHMAP[3])
# ans2 = 0

# print(HASHMAP[0])
# print(HASHMAP[1])
# print(HASHMAP[2])
# print(HASHMAP[3])

for i in range(256):
    boxId = i + 1 
    for k in range(len(HASHMAP[i][1])):
        f,l = HASHMAP[i][1][k]
        f = int(f)
        r = boxId * (k+1) * f 
        print(l,f,boxId,(k+1),r)
        ans2 += r

print("-----")
print("ans1",ans1)
print("ans2",ans2)
