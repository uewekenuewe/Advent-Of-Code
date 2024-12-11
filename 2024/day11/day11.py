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


cachee = {}

def stone_cachee(num):
    if num in cachee.keys():
        return cachee[num]
    if num == 0:
        cachee[num] = [1]
        return [1]
    if len(str(num)) % 2 == 0:
        num = str(num)
        cachee[num] = [int(num[:int(len(str(num))/2)]), int(num[int(len(str(num))/2):])]
        return [int(num[:int(len(str(num))/2)]), int(num[int(len(str(num))/2):])]
    cachee[num] = [num*2024]
    return [num*2024]

def stone(num):
    if num == 0:
        return [1]
    if len(str(num)) % 2 == 0:
        num = str(num)
        return [int(num[:int(len(str(num))/2)]), int(num[int(len(str(num))/2):])]
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


def calcCache():
    r = 0
    for x in cache:
        if cache[x][0] > 0:
            r += cache[x][0]
    return r


ans1 = len(s)

levels = [0 for _ in range(75)]
s = sorg
cache = {}
for x in s:
    cache[x] = [1,stone(x)]
#s = [[1,x] for x in s]
for _ in range(75):
    cache_cpy = {}
    for c in cache:
        v = stone(c)
        if cache[c][0] > 0:
            for x in cache[c][1]:
                if x in cache_cpy.keys():
                    cache_cpy[x][0] += cache[c][0]
                else:
                    cache_cpy[x] = [cache[c][0],stone(x)]

    cache = cache_cpy



for c in cache:
    if cache[c][0] > 0:
        ans2 += cache[c][0]



print("------")
print("ans1:", ans1)
print("ans2:", ans2)
