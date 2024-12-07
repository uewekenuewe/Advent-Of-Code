import re
import sys
import numpy as np
import copy 

ans1 = 0
ans2 = 0

if len(sys.argv) > 1:
    filename = sys.argv[1]
    f = open(sys.argv[1], "r")
else:
    f = open("07", "r")

lines = [l.strip() for l in f.readlines()]

def evalLineA(l):
    if type(l[1]) == int or len(l[1]) == 1:
        if l[0] == l[1][0]:
            return True
        else:
            return False 
    m = copy.deepcopy(l[1])
    m = [m[0]*m[1]] + m[2:]
    a = copy.deepcopy(l[1])
    a = [a[0]+a[1]] + a[2:]


    if evalLineA([l[0],a]) or evalLineA([l[0],m]):
        return True
    else:
        return False

def evalLineB(l):
    if type(l[1]) == int or len(l[1]) == 1:
        if l[0] == l[1][0]:
            return True
        else:
            return False 
    m = copy.deepcopy(l[1])
    m = [m[0]*m[1]] + m[2:]
    a = copy.deepcopy(l[1])
    a = [a[0]+a[1]] + a[2:]
    c = copy.deepcopy(l[1])
    c = [int(str(c[0])+str(c[1]))]+c[2:]


    if evalLineB([l[0],a]) or evalLineB([l[0],m]) or evalLineB([l[0],c]):
        return True
    else:
        return False

for i,l in enumerate(lines):
    l2 = [int(l.split(":")[0]) , [int(x) for x in l.split(":")[1].split()]]
    if evalLineA(l2):
        ans1 += l2[0]
    if evalLineB(l2):
        ans2 += l2[0]



print("------")
print("ans1:", ans1)
print("ans2:", ans2)
