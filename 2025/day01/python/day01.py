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
start = 50
for l in lines:
    lr = l[0]
    value = int(re.findall(r"\d+",l)[0])
    if lr == 'R':
        start = (start + value)% 100
    else:
        start = (start - value)% 100

    if start == 0:
        ans1+=1

start = 50
for l in lines:
    lr = l[0]
    value = int(re.findall(r"\d+",l)[0])
    for _ in range(value):
        if lr == 'R':
            start += 1 
        else:
            start -= 1 

        if start == 0:
            ans2+=1
        if start == 100:
            start = 0
            ans2+=1
        if start == -1:
            start = 99
print("------")
print("ans1:", ans1)
print("ans2:", ans2)
