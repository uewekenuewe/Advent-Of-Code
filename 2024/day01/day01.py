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
    f = open("01", "r")

lines = [l.strip() for l in f.readlines()]
l1 = []
l2 = []
for i,l in enumerate(lines):
    lines[i] = l.replace("\n","")
    l1.append(int(lines[i].split()[0]))
    l2.append(int(lines[i].split()[1]))

l1 = sorted(l1)
l2 = sorted(l2)

for i in range(len(l1)):
    ans1 += abs(l1[i]-l2[i])

l22 = {}
for x in l2:
    if x in l22.keys():
        l22[x] += 1
    else:
        l22[x] = 1
for x in l1:
    if x in l22.keys():
        ans2 += x * l22[x]

print("------")
print("ans1:", ans1)
print("ans2:", ans2)
