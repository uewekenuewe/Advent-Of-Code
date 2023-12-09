# Using readlines()
import re
import math
import sys
import numpy as np

ans1 = 0
ans2 = 0

F = open(sys.argv[1], "r")
lines = [l.strip() for l in F.readlines()]
for l in lines:
    print(l)

print("------")
print("ans1:", ans1)
print("ans2:", ans2)
