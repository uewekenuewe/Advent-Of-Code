
import re 
import copy 
import networkx as nx


file = open('8ex.in', 'r')
file = open('8.in', 'r')
lines = file.readlines()
ans1 = 0
ans2 = 0

inp = lines[0].strip()
points = {}
for l in lines[2:]:
    l = l.strip()
    p,lr = l.split("=")
    ll,rr = lr.replace("(","").replace(")","").split(",")
    p = p.strip()
    ll = ll.strip()
    rr = rr.strip()
    points[p] = (ll,rr)


currPoint = "AAA"
i = 0
while(currPoint != "ZZZ"):
    if inp[i] == "L":
        currPoint = points[currPoint][0]
    else:
        currPoint = points[currPoint][1]
    i+=1
    if i >= len(inp):
        i = 0
    ans1+=1

starts = {}
i = 0
for p in points:
    if(p[2] == "A"):
        starts[p] = str(i)+str(i)+p[2]
        print(str(i)+str(i)+p[2],p)
        i+=1

points2 = {}
for p in points:
    if p in starts.keys():
        points2[starts[p]] = points[p]
    else:
        points2[p] = points[p]     

points = points2
ans2arr = []
print(starts)


print("----------")
print("ans1:",ans1)
print("ans2:",ans2,max(ans2arr),ans2arr)
