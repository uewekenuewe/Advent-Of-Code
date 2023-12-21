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
    return len(r)

def count_arrangements(conditions, rules):
    if not rules:
        return 0 if "#" in conditions else 1
    if not conditions:
        return 1 if not rules else 0

    result = 0

    if conditions[0] in ".?":
        result += count_arrangements(conditions[1:], rules)
    if conditions[0] in "#?":
        if (
            rules[0] <= len(conditions)
            and "." not in conditions[: rules[0]]
            and (rules[0] == len(conditions) or conditions[rules[0]] != "#")
        ):
            result += count_arrangements(conditions[rules[0] + 1 :], rules[1:])
    return result

 
  

for l in lines:
    s,arrangements = l.split()
    arrangements = [int(x) for x in arrangements.split(",")]
    
    # PART 1
    #ans1+= len(getPermut(s,arrangements))

    # PART 2 
    s = s + "?" + s + "?" + s + "?" + s + "?" + s
    arrangements = arrangements + arrangements + arrangements + arrangements + arrangements

    ans2+= (count_arrangements(s,arrangements))

print("------")
print("ans1:", ans1,ans1 == 6871)
print("ans2:", ans2)