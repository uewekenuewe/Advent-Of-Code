import re
import copy
import networkx as nx


file = open("9ex.in", "r")
file = open("9.in", "r")
lines = file.readlines()
ans1 = 0
ans2 = 0

for l in lines:
    l = l.strip()

print("-----")
print("ans1:", ans1)
print("ans2:", ans2)

