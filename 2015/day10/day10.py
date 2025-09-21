import re
import sys
import numpy as np
import copy 

ans1 = 0
ans2 = 0

l = "1321131112"

def seg(line:str):
    result = [[line[0],1]]
    for i in range(1,len(line)):
        if result[-1][0] == line[i]:
            result[-1][1]+=1
        else:
            result.append([line[i],1])
    return result

def seg_string(segments):
    result = ""
    for value,count in segments:
        result += str(count)+value
    return result

for _ in range(50):
    x = seg(l)
    l = seg_string(x)
    if _ == 39:
        ans1 = len(l)
    if _ == 49:
        ans2 = len(l)



print("------")
print("ans1:", ans1)
print("ans2:", ans2)


