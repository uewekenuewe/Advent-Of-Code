import re
import sys
import numpy as np
import copy 

ans1 = 0
ans2 = 0

if len(sys.argv) > 1:
    filename = sys.argv[1]
    f = open(sys.argv[1], "r")
else:
    f = open("01", "r")

lines = [l.strip() for l in f.readlines()]
for l in lines:
    print(l)

print("------")
print("ans1:", ans1)
print("ans2:", ans2)


