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
    f = open("09", "r")

lines = [l.strip() for l in f.readlines()]
rana = []
ranb = {}
ind = 0
ind_pos = 0

def getValue(rr,ind):
    for x in rr:
        if ind in range(x[0],x[1]):
            return x 
    return False


total_len = 0
lastOne = 0

for l in lines:
    for i in range(int(len(l))):
        if i %2 == 0:
            rana.append([ind,[ind_pos,int(l[i])+ind_pos]])
            ind += 1
            total_len += abs(ind_pos-(int(l[i])+ind_pos))
        else:
            rana.append(['.',[ind_pos,int(l[i])+ind_pos]])
        ind_pos += int(l[i])
        lastOne = ind_pos


ranaa = copy.deepcopy(rana)
# verschieben
ind = len(rana)-1
i = 0
x = 0
ranb = []

#for i in range(len(rana)):
while(x <= total_len):
    v = rana[i][0]
    s1,e1 = rana[i][1]
    if v != '.':
        ranb.append(rana[i])
        x += abs(s1-e1)
        i += 1
    else:
        s2,e2 = rana[ind][1]
        if abs(s1-e1) == abs(s2-e2):
            ranb.append([rana[ind][0],rana[i][1]])
            x += abs(s1-e1)
            ind -= 2
            i += 1
        elif abs(s1-e1) > abs(s2-e2):
            ranb.append([rana[ind][0],[s1,s1+abs(s2-e2)]])
            rana[i][1] = [s1+abs(s2-e2),e1]
            x += abs(s2-e2)
            ind -= 2
        elif abs(s1-e1) < abs(s2-e2):
            ranb.append([rana[ind][0],[s1,e1]])
            rana[ind][1] = [rana[ind][1][0],rana[ind][1][1]-abs(s1-e1)]
            x += abs(s1-e1)
            i+= 1

    if x >= total_len:
        break



for i in range(len(ranb)):
    s,e = ranb[i][1]
    for k in range(s,e):
        ans1 += k*ranb[i][0]


# part b
rana = copy.deepcopy(ranaa)

for i in range(len(rana)):
    rana[i] = rana[i] + [False]

ranb = [rana[0]]
ranb[0][-1] = True

def reorder(arr):
    found = False
    for i in range(len(arr)-1,-1,-1):
        if arr[i][-1] == False and arr[i][0] != ".":
            #print("moving:",arr[i][0])
            found = True
            arr[i][-1] = True
            s1,e1 = arr[i][1]
            for k in range(1,i):
                s2,e2 = arr[k][1]
                if arr[k][0] == "." and abs(s1-e1)==abs(s2-e2) :
                    v = arr[i][0]
                    temp = copy.deepcopy(arr[i])
                    temp[0] = "."
                    arr[k][0] = v
                    arr[k][-1] = True
                    arr[i] = temp
                    break
                elif arr[k][0] == "." and abs(s1-e1)<abs(s2-e2) :
                    arr[k][1] = [s2+abs(s1-e1),e2]
                    temp = copy.deepcopy(arr[i])
                    arr[i][0] = "."
                    temp[1] = [s2,s2+abs(s1-e1)]
                    temp[-1] = True
                    arr.insert(k,temp)
                    break

        if found: 
            break
    return arr


print("ORG:",rana)
print("----")
for _ in range(20000):
    rana = reorder(rana)
#    print(rana)

#    for i in range(len(rana)):
#        s1,e1 = rana[i][1]
#        for k in range(abs(s1-e1)):
#            print(rana[i][0],end="")
#    print("")
for i in range(len(rana)):
    if rana[i][0] != ".":
        s,e = rana[i][1]
        for k in range(s,e):
            ans2 += k*int(rana[i][0])


print("------")
print("ans1:", ans1)
print("ans2:", ans2)


