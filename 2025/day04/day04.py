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
    f = open("04", "r")

lines = [l.strip() for l in f.readlines()]
matrix = []
for l in lines:
    print(l)
    matrix.append([x for x in l])

matrix = np.array(matrix)
dd = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,1),(1,-1),(-1,-1)]

def is_count(aain):
    x,y = aain
    result = 0
    for xx,yy in dd:
        dx = x+xx
        dy = y+yy
        if 0<=dx<len(matrix) and 0<=dy<len(matrix):
            if matrix[dx][dy] == '@':
                result += 1
    if result < 4:
        return True
    return False

def is_count2(aain,m):
    x,y = aain
    result = 0
    for xx,yy in dd:
        dx = x+xx
        dy = y+yy
        if 0<=dx<len(m) and 0<=dy<len(m):
            if m[dx][dy] == '@':
                result += 1
    if result < 4:
        return True
    return False




for i in range(len(matrix)):
    for k in range(len(matrix[0])):
        if matrix[i][k] == '@':
            ans1+= is_count((i,k))

removed=True
first = np.count_nonzero(matrix == "@")
current_count = np.count_nonzero(matrix == "@")
for _ in range(30000):
    matrix_tmp = copy.deepcopy(matrix)
    org_count = np.count_nonzero(matrix == "@")
    for i in range(len(matrix_tmp)):
        for k in range(len(matrix_tmp[0])):
            if matrix_tmp[i][k] == '@':
                if is_count2((i,k),matrix_tmp):
                    matrix[i][k] = '.'
                    current_count -= 1
                    ans2 +=1

    if org_count == current_count:
        removed = False
    else:
        current_count = org_count
    print(ans2)

print(matrix)
last = np.count_nonzero(matrix == "@")
#ans2 = abs(first-last)

print("------")
print("ans1:", ans1)
print("ans2:", ans2)


