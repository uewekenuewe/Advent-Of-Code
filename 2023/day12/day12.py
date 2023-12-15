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
        kk = getKey(inp,arrangements)
        if kk in CACH.keys():
            return CACH[kk]
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
            if len(r) == 0:
                CACH[kk] = 1
                return 1 
            else:
                CACH[kk] = len(r)
                return len(r)

def resolve(inp,arrangements):
    r = 0
    print(inp,arrangements)
    if inp.count("#") > 0 and len(arrangements) == 0:
        return 0 
    if inp == "":
        return 0 
    if len(arrangements) == 0: # and inp == "":
        # rechene möglichkeiten ?? + 1 ==> 
        return 1


    if inp[0] in ["#","?"]:
        if len(arrangements) > 1:
            r += resolve(inp[:arrangements[0]+1],[arrangements[0]])
            r += resolve(inp[arrangements[0]+1:],arrangements[1:])

    else:
        r += resolve(inp[1:],arrangements)


    return r

def nth_repl(s, sub, repl, n):
    find = s.find(sub)
    # If find is not -1 we have found at least one match for the substring
    i = find != -1
    # loop util we find the nth or we find no match
    while find != -1 and i != n:
        # find + 1 means we start searching from after the last match
        find = s.find(sub, find + 1)
        i += 1
    # If i is equal to n we found nth match so replace
    if i == n:
        return s[:find] + repl + s[find+len(sub):]
    return s      

for l in lines:
    s,arrangements = l.split()
    arrangements = [int(x) for x in arrangements.split(",")]
    
    # PART 1
    #ans1+= len(getPermut(s,arrangements))
    print(s,arrangements,resolve(s,arrangements))

    # PART 2 
    s = s + "?" + s + "?" + s + "?" + s + "?" + s
    arrangements = arrangements + arrangements + arrangements + arrangements + arrangements

    #ans2+= len(getPermut(s,arrangements))

print("------")
print("ans1:", ans1,ans1 == 6871)
print("ans2:", ans2)