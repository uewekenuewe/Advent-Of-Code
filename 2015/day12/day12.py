import re
import sys
import numpy as np
import copy 
import json 

ans1 = 0
ans2 = 0

f = open("12","r")
lines = f.readlines()
f.close()

complete_inp = "".join(lines)
inp = json.loads(complete_inp)

numbers = re.findall(r"[-]*\d+",complete_inp)
for n in numbers:
    ans1 += int(n)

def process_element(ele):
    result = 0
    if type(ele) == list:
        for x in ele:
            result += process_element(x)
        return result
    if type(ele) == dict:
        for x in ele:
            if ele[x] == "red":
                return 0
        for x in ele:
            result += process_element(ele[x])
        return result
    if type(ele) == str:
        return 0
    if type(ele) == int:
        return ele

    return result

ans2 = process_element(inp)


print("------")
print("ans1:", ans1)
print("ans2:", ans2)


