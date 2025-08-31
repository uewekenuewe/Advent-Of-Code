import re
import sys
import numpy as np
import copy 

ans1 = 0
ans2 = 0

#It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
#It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.

if len(sys.argv) > 1:
    filename = sys.argv[1]
    f = open(sys.argv[1], "r")
else:
    f = open("01", "r")

def get_part1(l:str):
    for i in range(len(l)-1):
        pair = l[i]+l[i+1]
        for k in range(i+2,len(l)-1):
            pair2 = l[k]+l[k+1]
            if pair == pair2:
                return True 
    return False

    
def get_part2(l:str):
    for i in range(len(l)-2):
        if l[i] == l[i+2] and l[i] != l[i+1]:
            return True
    return False

def solve_part2(l:str):
    a = get_part1(l)
    b = get_part2(l)
    if a and b:
        return 1 
    return 0

lines = [l.strip() for l in f.readlines()]
for l in lines:
    print(l,solve_part2(l))
    ans2+= solve_part2(l)

print("------")
print("ans1:", ans1)
print("ans2:", ans2)


