import re
import copy 
file1 = open('day4.in', 'r')
file1 = open('day4-ex.in', 'r')
Lines = file1.readlines()
arr = []
x = []
ans1 = 0
ans2 = 0
winMore = [_+1 for _ in range(len(Lines))]
lookUp = {}
lookUp2 = {}
for i,l in enumerate(Lines):
    l = l.strip()
    a,b = l.split(":")
    win,num = b.split("|")
    xo = 0
    num = re.findall("\d+",num)
    win = re.findall("\d+",win)
    num = [int(x) for x in num]
    win = [int(x) for x in win]
    first = False
    for n in num:
        if n in win:
            if not first:
                xo+=1
                first = True
            else:
                xo*=2
    ans1+= xo
    print(i+1,win,num,xo)
    toAdd = []
    for x in range(i+2,i+2+xo):
        if x < len(Lines):
            toAdd.append(x)

    lookUp[i+1] = xo
    lookUp2[i+1] = toAdd 
    # print(winMore)

print(winMore)

lookUp = lookUp2
print(lookUp)
def findSum(n):
    if(len(lookUp[n]) == 0):
        return 1
    else:
        sum = 1
        for x in lookUp[n]:
            sum += findSum(x)
        return sum
asdf = []
for x in winMore:
    asdf += lookUp[x]
for x in asdf:
    ans2+=findSum(x)
sum += len(Lines)
print(findSum(3))

# for _ in range(50000):
#     ans2 += len(winMore)
#     winMore2 = []
#     for x in winMore:
#         winMore2 += lookUp2[x]

#     winMore = copy.deepcopy(winMore2)
#     if(len(winMore2) == 0):
#         break

print("----------")
print("ans1:",ans1)
print("ans2:",ans2)