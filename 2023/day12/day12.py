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

def getPermut(inp,arrangements):
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
    return r


for l in lines:
    # PART 1
    s,arrangements = l.split()
    arrangements = [int(x) for x in arrangements.split(",")]
    ans1+= len(getPermut(s,arrangements))


    # PART 1 
    # MAP = {}
    # s = s + "?" + s + "?" + s + "?" + s + "?" + s
    # arrangements = arrangements + arrangements + arrangements + arrangements + arrangements

    # ans2+= len(getPermut(s,arrangements))



print("------")
print("ans1:", ans1)
print("ans2:", ans2)
