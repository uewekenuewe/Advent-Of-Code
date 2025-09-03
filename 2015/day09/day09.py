import re
import copy
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

def DFS(start,nodes):
    queue =  [start]
    visited = [start]
    while(len(queue) > 0):
        first = queue.pop()
        for c in nodes[first]:
            if not c in visited:
                visited.append(c)
                queue.insert(0,c)
    return visited

def DFS_PATHS(start,nodes):
    paths = [[[start],start]]
    paths_new = []
    for _ in range(len(nodes)-1): #len(nodes)):
        for p in paths:
            current_node = p[-1]
            for c in nodes[current_node]:
                tmp_path = copy.deepcopy(p)
                if not c in tmp_path[0]:
                    tmp_path[0].append(c)
                    tmp_path[1] = c
                    paths_new.append(tmp_path)
        paths = copy.deepcopy(paths_new)

    path_tmp = []
    for p in paths:
        if len(p[0]) >= len(nodes):
            path_tmp.append(p)
    paths = path_tmp
    return paths

def BFS(start,nodes):
    queue =  [start]
    visited = [start]
    while(len(queue) > 0):
        first = queue.pop()
        for c in nodes[first]:
            if not c in visited:
                visited.append(c)
                queue.append(c)
    return visited

cities = {}
weights = {}
def part1(l:str): 
    a,b = l.split("=")[0].split("to")
    a = a.strip()
    b = b.strip()
    d = l.split("=")[1].strip()
    d = int(d)
    weights[(a,b)] = d
    weights[(b,a)] = d
    if a in cities.keys():
        cities[a].append(b)
    else:
        cities[a] = [b]

    if b in cities.keys():
        cities[b].append(a)
    else:
        cities[b] = [a]

for l in lines:
    print(l)
    part1(l)

print(cities)
def get_path_value(path,weights):
    result = 0
    for i in range(len(path)-1):
        result += weights[(path[i],path[i+1])]
    return result

ans1 = 1e12
ans2 = 0
for n in cities:
    all_paths = DFS_PATHS(n,cities)
    for p,s in all_paths:
        value = get_path_value(p,weights)
        ans1 = min(ans1,value)
        ans2 = max(ans2,value)
print("------")
print("ans1:", ans1)
print("ans2:", ans2)


