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
    f = open("04", "r")

m = []
lines = [l.strip() for l in f.readlines()]
for l in lines:
    m.append([x for x in l])

m = np.array(m)


# PART A
def cntXMAS(arr):
    return "".join(arr).count("XMAS") + "".join(arr[::-1]).count("XMAS")

for i in range(len(m)):
    ans1 += cntXMAS(m[i])
    ans1 += cntXMAS(m[:,i])
for i in range(-1*len(m),len(m)):
    ans1 += cntXMAS(m.diagonal(i))
    ans1 += cntXMAS(np.fliplr(m).diagonal(i))

# PART B
d1 = [(-1,-1),(-1,1),(1,1),(1,-1)]
for i in range(len(m)):
    for k in range(len(m[i])):
        if m[i][k] == 'A':
            test = []
            for x,y in d1:
                dx = i+x
                dy = k+y
                if 0<= dx < len(m) and 0<= dy < len(m):
                    test.append(m[dx,dy])

            if len(test) == 4 and  "".join(test) in ["MSSM","MMSS","SMMS","SSMM"]:
                    ans2+=1

print("------")
print("ans1:", ans1)
print("ans2:", ans2)


