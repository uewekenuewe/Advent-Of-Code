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
    f = open("11", "r")


cache = {}

def stone_cache(num):
    if num in cache.keys():
        return cache[num]
    if num == 0:
        cache[num] = [1]
        return [1]
    if len(str(num)) % 2 == 0:
        num = str(num)
        cache[num] = [int(num[:int(len(str(num))/2)]), int(num[int(len(str(num))/2):])]
        return [int(num[:int(len(str(num))/2)]), int(num[int(len(str(num))/2):])]
    cache[num] = [num*2024]
    return [num*2024]

def stone(num):
    if num == 0:
        return [1]
    if len(str(num)) % 2 == 0:
        num = str(num)
        return [int(num[:int(len(str(num))/2)]), int(num[int(len(str(num))/2):])]
    return [num*2024]

def stone2(num):
    if num == 0:
        return 1
    if len(str(num)) % 2 == 0 and len(str(num)) > 1:
        num = str(num)
        return [int(num[:int(len(str(num))/2)]), int(num[int(len(str(num))/2):])]
    if len(str(num)) % 2 == 0 and len(str(num)) == 1:
        return 1
    return [num*2024]

lines = [l.strip() for l in f.readlines()]
s = []
for l in lines:
    s = [int(x) for x in l.split()]

sorg = copy.deepcopy(s)

for _ in range(25):
    scpy = []
    for x in range(len(s)):
        scpy += stone(s[x])
    s = copy.deepcopy(scpy)


ans1 = len(s)

levels = [0 for _ in range(75)]
s = [2024]
for _ in range(75):
    scpy = []
    for x in range(len(s)):
        scpy += stone(s[x])
    s = copy.deepcopy(scpy)
    #print(s)



ans2 = len(s)



print("------")
print("ans1:", ans1)
print("ans2:", ans2)
