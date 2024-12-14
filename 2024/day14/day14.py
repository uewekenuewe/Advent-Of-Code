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
    f = open("14", "r")

lines = [l.strip() for l in f.readlines()]
p = []
m = []

dim = (101,103)
#dim = (11,7)

for x in range(dim[0]):
    xo = []
    for k in range(dim[1]):
        xo.append(0)
    m.append(xo)

m = np.array(m)

mzero = copy.deepcopy(m)

seconds = 100

for l in lines:
    print(l)
    p.append([int(x) for x in re.findall("\-?\d+",l)])
    x,y,dx,dy = p[-1]
    x = (x + seconds*dx) % dim[0]
    y = (y + seconds*dy) % dim[1]
    m[x][y] += 1
    
m = np.array(m.T)
y,x = (int((dim[0]-1) / 2), int((dim[1]-1) / 2))
ans1 = 1
mx =  np.array(m[:x,:y])
ans1 *= (np.sum(mx))
mx = np.array(m[x+1:,:y])
ans1 *= (np.sum(mx))
mx = np.array(m[x+1:,y+1:])
ans1 *= (np.sum(mx))
mx = np.array(m[:x,y+1:])
ans1 *= (np.sum(mx))


#PART B

dd = ((1,0),(0,1),(-1,0),(0,-1))
# len p / 2 > len(struct)
def isTree():
    vglob = []
    q = []
    area = []
    for i in range(len(p)):
        x,y,dx,dy = p[i]
        if (x,y) not in vglob:
            q.append((x,y))
        v = []
        while(len(q)>0):
            fp = q.pop()
            if fp not in v:
                xx,yy = fp
                v.append(fp)
                for dx,dy in dd:
                    xx = dx+x
                    yy = dy+y 
                    if 0<=xx<len(m) and 0<=yy<len(m[0]):
                        if m[xx][yy] != 0:
                            q.append((xx,yy))
        vglob += v
        area.append(v)

    a_max = 0
    return area
    for x in area:
        a_max = max(a_max,len(x))

    if a_max >= 10:
        return True
    else:
        return False


def step():
    for i in range(len(p)):
        x,y,dx,dy = p[i]
        m[x][y] = 0
        x = (x+dx) % dim[0]
        y = (y+dy) % dim[1]
        p[i] = (x,y,dx,dy)
        m[x][y] = 1 

m = copy.deepcopy(mzero)
ii = 0
while(ii<10000):
    step()
    print("I:",ii)
    m = m.T
    for x in m:
        print("".join([str(y) for y in x]))
    m = copy.deepcopy(mzero)
    ii += 1


# 477 
# 201174624
# 212926352
print("------")
print("ans1:", ans1)
print("ans2:", ans2)


