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
springs = []
order = []
SO = []

def valid(inp,o):
    if inp.count("#") != sum(o):
        return False 
    

def solve(inp):
    s,o = inp 
    segs = []
    temp = ""
    r = []
    for c in s:
        if c != ".":
            temp += c 
        else: 
            if temp != "":
                segs.append(temp)
                temp = ""
    if temp != "":
        segs.append(temp)
    for c in combinations("ABCD",2):
        print(c)

    print(segs,r)

        

for l in lines:
    print(l)
    S,O = l.split()
    springs.append(S)
    order.append(O.split())
    (solve((S,O)))
    SO.append((springs[-1],order[-1]))

for s in SO:
    print(s)

print("------")
print("ans1:", ans1)
print("ans2:", ans2)
