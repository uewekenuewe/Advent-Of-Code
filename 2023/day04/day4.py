file = open('day4-ex.in', 'r')
file = open('day4.in', 'r')
lines = file.readlines()
winMore ={}
ans1 = 0
ans2 = 0
for i,l in enumerate(lines):
    l = l.strip()
    card,games = l.split(":")
    elf,winning = games.split("|")
    elf = [int(x) for x in elf.split()]
    winning = [int(x) for x in winning.split()]
    cnt = 0
    cnt2 = 0
    for x in elf:
        if x in winning:
            if cnt == 0:
                cnt +=1
            else:
                cnt*=2 
            cnt2+=1
    toadd = []
    for x in range(i+2,i+2+cnt2):
        if(x <= len(lines)):
            toadd.append(x)
    winMore[i+1] = toadd

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
print("ans1:",ans1)
print("ans2:",ans2-1)
