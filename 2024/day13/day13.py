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
    f = open("13", "r")

def possible(p):
    xa,ya = p['A']
    xb,yb = p['B']
    xp,yp = p['Prize']
    return (xa*100 + xb*100) >= xp and (yb*100 + ya*100) >= yp


def addPoint(p1,p2):
    return (p1[0]+p2[0],p1[1]+p2[1])

lines = [l.strip() for l in f.readlines()]
puz = [{}]
for l in lines:
    if l == "\n" or l == "\r" or l == "":
        puz.append({})
    else:
        ll = l.split(":")
        if ll[0] == "Prize":
            nums = re.findall("\d+",ll[1])
            puz[-1]["Prize"] = [int(n) for n in nums]
        else:
            button = ll[0].split()[1]
            nums = re.findall("\d+",ll[1])
            puz[-1][button] = [int(n) for n in nums]

for p in puz:
    ax,ay = p['A']
    bx,by = p['B']
    px,py = p['Prize']
    if possible(p):
        costs = 999999
        for i in range(100):
            for k in range(100):
                if ax*i + bx*k == px and ay*i + by*k == py:
                    costs = min(costs,i*3+k*1)
        if costs != 999999:
            ans1+=costs
            print(p,possible(p),costs)


# less equal 100 each button
# min button pushes
# count win 
#ans1 : 45731 too high
print("------")
print("ans1:", ans1)
print("ans2:", ans2)


