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
edgeLen = 0
for d in dig:
    direction,length,color = d 
    color = color.replace("(","").replace(")","").replace("#","")
    direction = str(color[-1])
    # length = int(length)
    length = int(color[:5], 16)
    if direction == "R" or direction == "0":    
        digger[1] += length
    if direction == "D" or direction == "1":
        digger[0] += length 
    if direction == "L" or direction == "2":
        digger[1] -= length 
    if direction == "U" or direction == "3":
        digger[0] -= length
    ans1+=length
    cords.append((digger[0],digger[1]))
    ans2 += int(color[:5], 16)

def shoelace(x_y):
    x_y = np.array(x_y)
    x_y = x_y.reshape(-1,2)

    x = x_y[:,0]
    y = x_y[:,1]

    S1 = np.sum(x*np.roll(y,-1))
    S2 = np.sum(y*np.roll(x,-1))

    area = .5*np.absolute(S1 - S2)
    print(S1,S2)
    return area

ans1 = (shoelace(cords)+ (ans2/2)) + 1
print(ans1)
print((ans2/2))