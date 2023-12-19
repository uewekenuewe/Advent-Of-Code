import re
import math
import sys
import numpy as np
import copy
from itertools import combinations

F = open(sys.argv[1], "r")
lines = [l.strip() for l in F.readlines()]


ans1 = 0
ans2 = 0

workflows = {}
items = []
for l in lines:
    if len(l) == 0:
        continue
    elif l[0] == "{":
        # print(l.replace("{","").replace("}","").split(","))
        items.append(l.replace("{","").replace("}","").split(","))
    else:
        name,flow = l.split("{")
        flow = flow.replace("}","")
        workflows[name] = flow.split()

print(items)
print(workflows)