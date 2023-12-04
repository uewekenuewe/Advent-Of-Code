import re
file1 = open('day2-ex.in', 'r')
file1 = open('day2.in', 'r')
Lines = file1.readlines()
arr = []
x = []
ans1 = 0
ans2 = 0
# only 12 red cubes, 13 green cubes, and 14 bl
red = 12 
green = 13
blue = 14
for l in Lines:
    _id,sets = l.split(":")
    _id = re.findall("\d+",_id)[0]
    sets = sets.split(";")
    ans1_arr = []
    aok = True
    power = 0
    mr = 0
    mg = 0 
    mb = 0
    for s in sets:
        games = s.split(",")
        r = 0
        b = 0
        _g = 0            
        for g in games:
            if "red" in g:
                r += int(re.findall("\d+",g)[0])
            if "blue" in g:
                b += int(re.findall("\d+",g)[0])
            if "green" in g:
                _g += int(re.findall("\d+",g)[0])  
        if(r > red or b > blue or _g>green):
            aok = False
        mr = max(mr,r)
        mg = max(mg,_g)
        mb = max(mb,b)
    if(aok):
        ans1+=int(_id) 
    ans2 += (mr*mg*mb )    
 

# 3874
print(ans1)
print(ans2)