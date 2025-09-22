import re
import sys
import numpy as np
import copy 
from itertools import permutations

ans1 = 0
ans2 = 0

if len(sys.argv) > 1:
    filename = sys.argv[1]
    f = open(sys.argv[1], "r")
else:
    f = open("13", "r")

lines = [l.strip() for l in f.readlines()]
people = {}
people2 = {}
def parse_line(line:str):
    l_spl = line.split()
    x = l_spl[0]
    y = l_spl[-1].replace(".","")
    value = int(re.findall(r'\d+',line)[0])
    people[x] = 1
    people[y] = 1
    if 'lose' in line:
        value *= -1
    people2[(x,y)] = value
    return(x,y,value)

def value_from_list(sitting,pp):
    result = 0
    for i in range(len(sitting)):
        if i != len(sitting)-1:
            result += (pp[(sitting[i],sitting[i+1])])
            result += (pp[(sitting[i+1],sitting[i])])
        else:
            result += (pp[(sitting[i],sitting[0])])
            result += (pp[(sitting[0],sitting[i])])
    return result



for l in lines:
    print(l,parse_line(l))

for p in permutations(people.keys()):
    value = value_from_list(list(p),people2)
    ans1 = max(ans1,value)

people3 = {}
for p in people2.keys():
    people3[p] = people2[p]
    p1,p2 = p
    people3[("you",p1)] = 0
    people3[("you",p2)] = 0
    people3[(p1,"you")] = 0
    people3[(p2,"you")] = 0

people["you"] = 1

for p in permutations(people.keys()):
    value = value_from_list(list(p),people3)
    ans2 = max(ans2,value)


print("------")
print("ans1:", ans1)
print("ans2:", ans2)


