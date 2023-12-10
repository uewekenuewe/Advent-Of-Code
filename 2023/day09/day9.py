import re
import copy
import networkx as nx



# file = open("9ex.in", "r")
file = open("9.in", "r")
lines = file.readlines()
ans1 = 0
ans2 = 0

ans1arr = []
ans2arr = []

for l in lines:
    l = l.strip()
    nums = [int(x) for x in l.split()]
    ansans = [nums]
    xo = 0
    while len(set(nums)) != 1 and set(nums) != 0:
        xo += 1
        nums2 = [(nums[i] - nums[i - 1]) for i in range(1, len(nums))]
        ansans.append(nums2)
        nums = nums2
        if xo > 1000000:
            break
    x = ansans[0][-1]
    y = 0
    lastY = 0
    for a in ansans[1:]:
        x += a[-1]
    ansans.append([0 for _ in range(len(ansans[-1]))])
    ansans[-1] = [0] + ansans[-1]
    for i in range(len(ansans) - 1, -1, -1):
        bottom = ansans[i][0]
        right = ansans[i - 1][0]
        left = 0
        if bottom == right:
            left = 0
        elif bottom < right:
            left = right - bottom
        else:
            left = right - bottom
        ansans[i - 1] = [left] + ansans[i - 1]

    print(l, "--", x)
    ans1arr.append(x)
    ans2arr.append(ansans[0][0])

ans1 = sum(ans1arr)
ans2 = sum(ans2arr)
print("-----")
print("ans1:", ans1)
print("ans2:", ans2)

