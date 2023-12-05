import time
import sys
import os 
from termcolor import colored


file = open('day4-ex.in', 'r')
file = open('day4.in', 'r')
lines = file.readlines()
winMore ={}
ans1 = 0
ans2 = 0
ani = ["" for x in range(len(lines)+2)]
ani[-1] = "ans1: " + str(ans1)
ani[-2] = "ans2: " + str(ans2)

def animate(i):
    os.system("cls")
    ani[-1] = "ans1: " + str(ans1)
    ani[-2] = "ans2: " + str(ans2)
    if(i > 10):    
        for x in ani[i-10:i]:
            print(" ".join(x))
    else:
        for x in ani[:10]:
            print(" ".join(x))
    print("---------")
    print(ani[-1])
    print(ani[-2])
    print("---------")
    time.sleep(0.125) 

for i,l in enumerate(lines):
    l = l.strip()
    ani[i] = l
    animate(i)
    card,games = l.split(":")
    ani[i] = l.split(":")
    animate(i)
    elf,winning = games.split("|")
    elf = [int(x) for x in elf.split()]
    winning = [int(x) for x in winning.split()]
    ani[i] = [card] + [str(x) for x in elf] + ["/"] +  [str(x) for x in winning]
    animate(i)
    cnt = 0
    cnt2 = 0
    for x in elf:
        if x in winning:
            for t,txt in enumerate(ani[i]):
                if txt == str(x):
                    ani[i][t] = colored(str(x),"green",attrs=["bold","blink"])
                    animate(i)
            # ani[i][ani[i].index(str(x))] = 

            
            
            if cnt == 0:
                cnt +=1
            else:
                cnt*=2 
            cnt2+=1
        animate(i)
        
    toadd = []
    for x in range(i+2,i+2+cnt2):
        if(x <= len(lines)):
            toadd.append(x)
    winMore[i+1] = toadd
    ani[i] = ani[i] +[ "  \t\t  score: " + str(cnt)]
    ans1+=cnt

lookUp = {}
for x in (winMore):
    if len(winMore[x]) == 0:
        winMore[x] = 1

def getTotal(inp):
    r = 1 
    if( type(inp) == list ): 
        for x in inp:
            if(x in lookUp.keys()):
                r+=lookUp[x]
            else:
                lookUp[x] = getTotal(winMore[x])
                r += lookUp[x]
        return r
    else:
        return inp


ans2 = (getTotal([int(x)+1 for x in range(len(lines))]))
# print("ans1:",ans1)
# print("ans2:",ans2-1)
animate()