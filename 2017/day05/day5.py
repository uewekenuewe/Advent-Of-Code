
import re 

file = open('5ex.in', 'r')
file = open('5.in', 'r')
lines = file.readlines()
ans1 = 0
ans2 = 0

def evalStr(strin):
    result = [[],[],""] 
    for c in strin:
        if c in ["a","e" ,"i","o","u"]:
            result[0].append(c)

    for i in range(0,len(strin)-1):
        if strin[i] == strin[i+1]:
            result[1].append(strin[i]+strin[i+1])

    for x in ["ab", "cd", "pq", "xy"]:
        if x in strin:
            result[2] = x 
    print(result)
    if(len(result[2]) > 0):
        return False
    else:
        return (len(result[0]) >= 3 and len(result[1]) > 0)

for l in lines:
    l = l.strip()
    if(evalStr(l)):
        ans1+=1
    print(l,evalStr(l))

print("----------")
print("ans1:",ans1)
print("ans2:",ans2)
