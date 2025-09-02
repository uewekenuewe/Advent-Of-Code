import re
import sys
import numpy as np
import copy 

ans1 = 0
ans2 = 0
total_value = 0
removed_value = 0

if len(sys.argv) > 1:
    filename = sys.argv[1]
    f = open(sys.argv[1], "r")
else:
    f = open("08", "r")

lines = [l.strip() for l in f.readlines()]
hexchars = ['0','1','2','3','4','5','6','7','8']
def part2(l:str):
    result = 2
    i = 0
    while(i < len(l)):
        if l[i] == '"':
            result += 2
        elif l[i] == '\\':
            result += 2
        else:
            result += 1
        i+=1
    return result

def part1(l:str):
    result = len(l) - 2
    l = l[1:-1]
    i = 0
    while(i < len(l)):
        if l[i] == '\\' and l[i+1] == '"':
            result -= 1
            i += 2
        elif l[i] == '\\' and l[i+1] == '\\':
            result -= 1
            i += 2
        elif l[i] == '\\' and l[i+1] == 'x':
            i += 4
            result -= 3
        else:
            i+=1

    return result
for l in lines:
    total_value += len(l)
    result1 = part1(l)
    ans1 += result1
    result2 = part2(l)
    ans2 += result2

ans1 = total_value - ans1
ans2 = ans2 - total_value
print("------")
print("ans1:", ans1)
print("ans2:", ans2)


