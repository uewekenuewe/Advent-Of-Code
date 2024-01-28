import re
import math
import sys
import numpy as np
import copy 

class point():
     def __init__(self, a, b, c):
         self.x = a
         self.y = b
         self.z = c
     def __str__(self):
         return "( "+str(self.x)+" , "+str(self.y)+" , "+str(self.z)+" )"
     def __eq__(self, other): 
        if not isinstance(other, point):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.x == other.x and self.y == other.y # and self.z == other.z


ans1 = 0
ans2 = 0

F = open(sys.argv[1], "r")
lines = [l.strip() for l in F.readlines()]
hail = []
for l in lines:
    p,v = l.split("@")
    px,py,pz = [int(x) for x in p.split(",")]
    vx,vy,vz = [int(x) for x in v.split(",")]
    hail.append((point((vx),(vy),(vz)),point(px,py,pz)))
    #print(hail[-1][0],hail[-1][1])


def inbound2d(point,lowerBound,upperBound):
    return (lowerBound <= point.x <= upperBound) and (lowerBound <= point.y <= upperBound)


def interSect(b1,b2):
    b1v,b1p = b1
    b2v,b2p = b2
    divisor = (b1v.x*b2v.y - b1v.y*b2v.x) 
    if divisor != 0:
        u = ((b1p.y*b2v.x + b2v.y*b2p.x - b2p.y*b2v.x - b2v.y*b1p.x ) / (b1v.x*b2v.y - b1v.y*b2v.x))
        v = (((b1p.x + b1v.x * u - b2p.x) / b2v.x))
        m1 = point(round(b1p.x+b1v.x*u,3) , round(b1p.y+b1v.y*u,3),u)
        m2 = point(round(b2p.x+b2v.x*v,3) , round(b2p.y+b2v.y*v,3),v)
        #print(m1,m2)
        if u < 1 or v < 1:
            return -1

        return m1
    else:
        return -1 

low= 7
low= 200000000000000
up = 27
up = 400000000000000
for i in range(0,len(hail)-1):
    for k in range(i+1,len(hail)):
        interSec = interSect(hail[i],hail[k])
        if interSec != -1:
            if inbound2d(interSec,low,up ): #and interSec.z >= 0:
                ans1+=1

maxV = point(0,0,0)
for i in range(len(hail)):
    if hail[0][i].x > maxV.x:
        maxV.x = hail[i][0].x


print("------")
print("ans1:", ans1)
print("ans2:", ans2)
