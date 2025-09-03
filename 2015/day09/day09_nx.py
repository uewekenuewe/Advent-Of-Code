import re
import copy
import sys
import numpy as np
import copy 
import networkx as nx 

ans1 = 1e12
ans2 = 0

if len(sys.argv) > 1:
    filename = sys.argv[1]
    f = open(sys.argv[1], "r")
else:
    f = open("09", "r")

lines = [l.strip() for l in f.readlines()]

G = nx.Graph()
def part1(l:str): 
    a,b = l.split("=")[0].split("to")
    a = a.strip()
    b = b.strip()
    d = l.split("=")[1].strip()
    d = int(d)
    G.add_node(a)
    G.add_node(b)
    G.add_edge(a,b,weight=d)
    G.add_edge(b,a,weight=d)

for l in lines:
    print(l)
    part1(l)

print(G)
def get_path_value(p,G):
    result = 0
    for i in range(len(p)-1):
        result += G.get_edge_data(p[i],p[i-1])['weight']
    return result

for n1 in G.nodes():
    for n2 in G.nodes():
        if n1 != n2:
            for p in nx.all_simple_paths(G,n1,n2):
                if len(p) == len(G.nodes()):
                    path_value = get_path_value(p,G)
                    ans1 = min(ans1,path_value)
                    ans2 = max(ans2,path_value)
print("------")
print("ans1:", ans1)
print("ans2:", ans2)


