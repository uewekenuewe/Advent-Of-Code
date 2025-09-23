import re
import sys
import numpy as np
import math
import copy 

ans1 = 0
ans2 = 0

if len(sys.argv) > 1:
    filename = sys.argv[1]
    f = open(sys.argv[1], "r")
else:
    f = open("14", "r")

deers = {}
lines = [l.strip() for l in f.readlines()]
for l in lines:
   deer = l.split()[0]
   speed,t1,t2 = [int(x) for x in re.findall(r'\d+',l)]
   deers[deer] = [speed,t1,t2,'active',t1,0,0]
   total = math.floor(2503/(t1+t2)) * t1*speed
   total += min(t1,2503%(t1+t2)) * speed
   #print(l,deer,speed,t1,t2, total)
   ans1 = max(ans1,total)


for i in range(2503):
    max_total = 0
    for d in deers:
        speed,t1,t2,state,cnt,total,points = deers[d]
        cnt -= 1
        if cnt == 0:
            if state == 'active':
                total += speed 
                state = 'rest'
                cnt = t2
            else:
                state = 'active'
                cnt = t1
        else:
            if state == 'active':
                total += speed
        max_total = max(max_total,total)
        deers[d] = [speed,t1,t2,state,cnt,total,points]
    for d in deers:
        speed,t1,t2,state,cnt,total,points = deers[d]
        if total == max_total:
            points += 1
            ans2 = max(points,ans2)
        deers[d] = [speed,t1,t2,state,cnt,total,points]



        

print("------")
print("ans1:", ans1)
print("ans2:", ans2)

