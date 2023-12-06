
import re 

file = open('day6-ex.in', 'r')
file = open('day6.in', 'r')
lines = file.readlines()
ans1 = 0
ans2 = 0
time = [int(x) for x in lines[0].split(":")[1].split()]
dist = [int(x) for x in lines[1].split(":")[1].split()]

races = []
for i in range(len(time)):
    races.append((time[i],dist[i]))
ans1arr = []
for r in races:
    t,d = r 
    a = 0
    for i in range(1,t):
        s = i*(t-i) 
        if s > d:
            a += 1
    ans1arr.append(a)

ans1 = 1 
for x in ans1arr:
    ans1 *= x

print("----")
print("ans1:",ans1)

time = int((lines[0].split(":")[1]).replace(" ",""))
dist = int((lines[1].split(":")[1]).replace(" ",""))

left = -1
for i in range(1,time):
    s = i*(time-i) 
    if s > dist:
        if left == -1:
            left = i
            break

right = -1
for i in range(time,0,-1):
    s = i*(time-i) 
    if s > dist:
        if right == -1:
            right = i+1
            break
ans2 = abs(left-right)

# print(time,dist)
print("ans2:",ans2)
