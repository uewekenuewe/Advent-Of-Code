import re
import math
import sys
import numpy as np
import copy
from itertools import combinations
import copy
import networkx as nx
import shapely
import matplotlib.pyplot as plt
import geopandas as gpd
from shapely.geometry import Point


F = open(sys.argv[1], "r")
lines = [l.strip() for l in F.readlines()]

# up (U), down (D), left (L), or right (R)

ans1 = 0
ans2 = 0
m = []
dig = []
for l in lines:
    dig.append(l.split())

digger = [0,0]
cords = [(0,0)]
s = 0
for d in dig:
    direction,length,color = d 
    length = int(length)
    if direction == "R":    
        digger[1] += length
    if direction == "D":
        digger[0] += length 
    if direction == "L":
        digger[1] -= length 
    if direction == "U":
        digger[0] -= length
    s+=length
    cords.append((digger[0],digger[1]))

def edgePara(edge1,edge2):
    (s1x,s1y),(e1x,e1y) = edge1 
    (s2x,s2y),(e2x,e2y) = edge2 
    return ((s1x == e1x) and (s2x == e2x)) or ((s1y == e1y) and (s2y == e2y))

#
# the formula to find the area of a polygon with n sides is:(n * s^2) / (4 * tan(π/n))
# Where:
#  n  is the number of sides of the polygon.
# s is the length of each side of the polygon.This formula is known as the Heron's formula. It is only valid for convex polygons. If the polygon is not convex, the area can not be calculated using this formula.
# n Formula is Area=∣∣∣(x1y2−y1x2)+(x2y3−y2x3)...(xny1−ynx1)2∣∣∣
# where xn
#  is the x
#  coordinate of the vertex n
# , yn
#  is the y
#  coordinate of the vertex n

edges = []
ans = 0 
for i in range(1,len(cords)):
    edges.append((cords[i-1],cords[i]))
    (x1,y1) = cords[i-1] 
    (x2,y2) = cords[i]
    ans += (x1*y2-y1*x2)

ans = abs(ans/2) 


# n = len(edges)
# s = 6
# ans = (n * s^2) / (4 * math.tan(math.pi/n))
print(ans)