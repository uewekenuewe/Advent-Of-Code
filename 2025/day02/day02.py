import re
import sys
import numpy as np
import copy 
import math

ans1 = 0
ans2 = 0

if len(sys.argv) > 1:
    filename = sys.argv[1]
    f = open(sys.argv[1], "r")
else:
    f = open("02", "r")

lines = [l.strip() for l in f.readlines()]
ranges = lines[0].split(",")

def asdf(s):
    s = str(s)
    if len(s) %2 != 0:
        return False
    if s[:math.floor(len(s)/2)] != s[math.floor(len(s)/2):]:
        return False
    return True
def asdf2(s):
    s = str(s)
    for i in range(math.ceil(len(s)/2)):
        if s.count(s[0:i])*len(s[0:i]) == len(s):
            return True
    if s[:math.floor(len(s)/2)] != s[math.floor(len(s)/2):]:
        return False
    return True

def part1(lower,upper):
    result = []
    for x in range(lower,upper+1):
        if asdf(x):
            result.append(x)
    return result
def part2(lower,upper):
    result = []
    for x in range(lower,upper+1):
        if asdf2(x):
            result.append(x)
    return result

ranges2 = []
for r in ranges:
    arr = r.split("-")
    arr = [int(x) for x in arr]
    ranges2.append(arr)

for u,l in ranges2:
    ans1 += sum(part1(u,l))
    ans2 += sum(part2(u,l))

print("------")
print("ans1:", ans1) 
print("ans2:", ans2) # 46769308530
