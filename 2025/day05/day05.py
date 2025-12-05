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
    f = open("05", "r")

lines = [l.strip() for l in f.readlines()]
ranges = []
fresh = []
for l in lines:
    if "-" in l:
        ranges.append((int(l.split("-")[0]),int(l.split("-")[1])))
    else:
        try:
            fresh.append(int(l))
        except:
            continue

for f in fresh:
    for l,r in ranges:
        if f >= l and f <= r:
            ans1+=1
            break


def combine_range(rr1,rr2):
    l1,r1 = rr1
    l2,r2 = rr2
    if l1 <= l2 and r1>=r2:
        #print("case1")
        return rr1
    if l2 <= l1 and r2>=r1:
        #print("case2")
        return rr2
    if l1 <= l2 and r1>=l2 and r2>=r1:
        #print("case3")
        return (l1,r2)
    if l2 <= l1 and r2>=l1 and r1>=r2:
        #print("case4")
        return (l2,r1)

    return -1



for _ in range(1000):
    ranges_new = []
    combine = []
    stop = False
    for i in range(len(ranges)):
        for k in range(i+1,len(ranges)):
            xo = combine_range(ranges[i],ranges[k])
            if xo != -1:
                combine.append(i)
                combine.append(k)
                stop = True
                break
        if stop:
            break
    if len(combine) != 2:
        break
    for i in range(len(ranges)):
        if i not in combine:
            ranges_new.append(ranges[i])
    ranges_new.append(combine_range(ranges[combine[0]],ranges[combine[1]]))

    ranges = copy.deepcopy(ranges_new)
    print(ranges_new)


ans2 = 0
for l,r in ranges:
    ans2+= abs(r-l)+1

# examples to test combine range function 
#print(combine_range((1,10),(5,6)))
#print(combine_range((5,6),(1,10)))
#print(combine_range((1,3),(4,5)))
#print(combine_range((5,8),(1,3)))
#print(combine_range((1,5),(3,10)))
#print(combine_range((3,10),(1,5)))
#print(combine_range((10, 18), (12, 18)))
#print(combine_range((10,14),(16,20)))
#print(combine_range((16,20),(12,18)))
print("------")
print("ans1:", ans1)
print("ans2:", ans2) # 440124610699592 falsch


