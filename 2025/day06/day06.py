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
    f = open("06", "r")

lines = [l.strip() for l in f.readlines()]
num = []
operations = []
for l in lines:
    num.append([int(x) for x in re.findall(r"\d+",l)])
    if "*" in l:
        operations.append(l)

operations = operations[0].split()
num = num[:-1]
for i in range(len(num[0])):
    rr = 0
    if operations[i] == "*":
        rr = 1
        for k in range(len(num)):
            rr *= num[k][i]
    else:
        for k in range(len(num)):
            rr += num[k][i]

    ans1+=rr


f.close()

if len(sys.argv) > 1:
    filename = sys.argv[1]
    f = open(sys.argv[1], "r")
else:
    f = open("06", "r")

lines = [l.replace("\n","") for l in f.readlines()]

def spl(line):
    rr =[]
    current = ""
    for x in range(len(line)-1):
        if x != " ":
            current += line[x]
        else:
            if line[x+1] == " ":
                current += " "
            else:
                rr.append(current)
                current = "" 
    current += line[-1]
    rr.append(current)
    return rr

nn = []
operations = []
num = []
for l in lines:
    if "*" in l:
        operations.append(l)
    else:
        num.append(re.findall(r"\d+",l))
lines2 = copy.deepcopy(lines[:-1])


lines3 = []
inds = []
for i in range(len(lines2[0])):
    curr = ""
    for k in range(len(lines2)):
        curr += lines2[k][i]
    lines3.append(curr)
    if curr.count(" ") == len(curr):
        inds.append(i)

lines4 = []
for l in lines2:
    xo = [x for x in l]
    for i in inds:
        xo[i] = "|"
    print("".join(xo).replace(" ","0"))
    lines4.append("".join(xo).replace(" ","0"))

operations= operations[0].split()
print(operations)
kk = len(operations)-1
rr = 0
if operations[kk] == "*":
    rr = 1

for i in range(1,len(lines4[0])+1):
    curr = ""
    for k in range(len(lines4)):
        curr += lines4[k][-1*i]
    if not "|" in curr:
        if "0" in curr:
            curr= curr.replace("0","")
        print(int(curr))
        if operations[kk] == "*":
            rr *= int(curr)
        else:
            rr += int(curr)
    else:
        ans2 += rr
        print("--",rr,operations[kk])
        kk -= 1
        rr = 0
        if operations[kk] == "*":
            rr = 1

ans2 += rr
print("--",rr,operations[kk])






print(lines4)
print("------")
print("ans1:", ans1)
print("ans2:", ans2)
