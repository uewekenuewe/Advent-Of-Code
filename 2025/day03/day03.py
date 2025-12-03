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
    f = open("03", "r")

lines = [l.strip() for l in f.readlines()]
def get_max_with_index(arr,max_len):
    for i in range(9,-1,-1):
        for k in range(0,len(arr)):
            if arr[k] == str(k) and k < max_len:
                return k
    return -1


def get_max2(arr):
    current_arr = arr
    result = ""
    print(arr)
    for xx in range(12,0,-1):
        reminder = xx
        max_value = (0,-1)
        current_arr2 = copy.deepcopy(current_arr)
        for i in range(len(current_arr2 )-reminder,-1,-1):
            if int(current_arr2[i]) >= max_value[0]:
                max_value = (int(current_arr2[i]),i)

        current_arr = current_arr2[max_value[1]+1:]
        result += str(max_value[0])
    return int(result)

def get_max(arr):
    result = 0
    for i in range(len(arr)):
        for k in range(i+1,len(arr)):
            value = int(arr[i]+arr[k])
            if value > result:
                result = value

    return result

for l in lines:
    ans1 += get_max(l)
    r2 = get_max2(l)
    print(l,r2)
    ans2 += int(r2)


print("------")
print("ans1:", ans1)
print("ans2:", ans2)
