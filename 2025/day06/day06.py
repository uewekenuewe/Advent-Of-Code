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

lines = copy.deepcopy(lines[:-1])
ll_tmp = []
for i in range(len(lines)):
    ll_tmp.append([x for x in lines[i]])

operations = operations[0].split()
ll_tmp = np.array(ll_tmp)
ind = 0
rr = 0
if operations[ind] == "*":
    rr = 1
for i in range(len(ll_tmp[0])):
    value = "".join(ll_tmp[:,i])
    if value.count(" ") == len(value):
        ind += 1
        ans2 += rr
        rr = 0
        if operations[ind] == "*":
            rr = 1
    else:
        if operations[ind] == "*":
            rr *= int(value)
        else:
            rr+= int(value)
ans2+=rr
print("------")
print("ans1:", ans1,ans1 == 4580995422905)
print("ans2:", ans2,ans2 == 10875057285868)
