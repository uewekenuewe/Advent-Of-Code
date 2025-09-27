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
    f = open("15", "r")

lines = [l.strip() for l in f.readlines()]
cookies = {}
for l in lines:
    l_spl = l.split(":")
    cookie_name = l_spl[0]
    cookies[cookie_name] = [int(x) for x in re.findall(r'\-*\d+',l_spl[1])]
    print(l,cookies[cookie_name])

def get_value_amounts_distribution(amounts,cookies):
    values = [0 for _ in range(4)]
    result = 1 
    i = 0
    for c in cookies:
        k = 0
        for v in cookies[c][:-1]:
            values[k] += v*amounts[i]
            k+=1
        i+=1

    for v in values:
        if v > 1:
            result *= v
    return result



amounts = [100/len(cookies) for _ in range(len(cookies))]
#amounts = [25 for _ in range(len(cookies))]
#amounts[0] = 100


ans1 = get_value_amounts_distribution(amounts,cookies)

combinations = [amounts]
def get_children(parent):
    result = []
    for k in range(len(parent)):
        child = copy.deepcopy(parent)
        child[k] -= 1
        for i in range(len(child)):
            child2 = copy.deepcopy(child)
            if i != k:
                child2[i] += 1
                result.append(child2)
    return result

queue = [combinations[0]]
visited = []
while(len(queue)>0):
    ele = queue[0]
    queue.pop()
    idx = ",".join([str(x) for x in ele])
    if idx in visited:
        continue
    else:
        vv = get_value_amounts_distribution(ele,cookies)
        visited.append(idx)
        ans1 = max(ans1,vv)
        print(visited)
        for c in get_children(ele):
            print(c)
            queue.append(c)
#
print("------")
print("ans1:", ans1)
print("ans2:", ans2)


# 10545000.0 too low 
# 1108800
# 10771200 too low
