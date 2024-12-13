import re
import sys
import numpy as np
import copy 
from sympy import symbols, Eq, solve
from sympy.core.compatibility import _as_int

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

factor = 10000000000000 




def isint(i):
        try: _as_int(i, strict=False)
        except: return False
        return True

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

    px+=factor
    py+=factor

    x, y = symbols('x y')
    eq1 = Eq(ax*x + bx*y , px)
    eq2 = Eq(ay*x + by*y , py)
    sol = solve((eq1,eq2), (x, y))
    if isint(sol[x]) and isint(sol[y]):
        ans2+=(sol[x]*3)+(sol[y])

print("------")
print("ans1:", ans1)
print("ans2:", ans2)


