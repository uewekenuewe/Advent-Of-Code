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


CACH = {}

def getSeg(inp):
    seg = []
    temp = ""
    for c in inp:
        if c != ".":
            temp += c 
        else: 
            if temp != "":
                seg.append(temp)
            temp = ""
    if temp != "":
        seg.append(temp)

    return seg

def getKey(inp,arrangements):
    r = inp + "|" 
    for x in arrangements[:-1]:
        r += str(x) + ","
    r += str(arrangements[-1])
    return r

def getPermut(inp,arrangements):
    key = getKey(inp,arrangements)
    if key in CACH.keys():
        return CACH[key]
    else:
        r = [inp]
        cnt = sum(arrangements)
        for _ in range(inp.count("?")):
            r2 = []
            for x in r:
                x1 = x.replace("?","#",1)
                x2 = x.replace("?",".",1)
                if _ == inp.count("?")-1:
                    if x1.count("#") == cnt:
                        r2.append(x1)
                    if x2.count("#") == cnt:                    
                        r2.append(x2)
                else:
                    r2.append(x1)
                    r2.append(x2)
            r = r2 
        r2 = []
        for res in r:
            segs = getSeg(res) 
            if len(segs) == len(arrangements):
                finalAdd = True
                for i in range(len(segs)):
                    if len(segs[i]) != arrangements[i]:
                        finalAdd = False 
                if finalAdd:
                    r2.append(res)
        r = r2 
        CACH[key] = r
        return r

def solvePrt2(inp,arrangements):
    


for l in lines:
    s,arrangements = l.split()
    arrangements = [int(x) for x in arrangements.split(",")]
    
    # PART 1
    #ans1+= len(getPermut(s,arrangements))

    # PART 2 
    s = s + "?" + s + "?" + s + "?" + s + "?" + s
    arrangements = arrangements + arrangements + arrangements + arrangements + arrangements

    #ans2+= len(getPermut(s,arrangements))

print("----")
print(getPermut("???",[1,1]),len(getPermut("???",[1,1])))
print(getPermut("???",[1]),len(getPermut("???",[1])))

print("------")
print("ans1:", ans1)
print("ans2:", ans2)
