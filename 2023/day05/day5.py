
import re 

file = open('day5.in', 'r')
file = open('day5-ex.in', 'r')
lines = file.readlines()
ans1 = 0
ans2 = 0

seeds = [int(x) for x in re.findall("\d+",lines[0])]
print(seeds)
mat = {}
mat2 = []
key = ""
section = []
for i,l in enumerate(lines[2:]):
    l = l.strip()
    if l != "\n":
        if "map" in l:
            key = l.replace(":","").replace("map","")
            mat[key] = []
            if len(section) != 0:
                mat2.append(section)
                section = []
            print(key)
        else:
            toAdd = [int(x) for x in l.split()]
            if len(toAdd) > 0:
                mat[key].append(toAdd)
                section.append(toAdd)

def overlap(start1, end1, start2, end2):
    """Does the range (start1, end1) overlap with (start2, end2)?"""
    return (
        start1 <= start2 <= end1 or
        start1 <= end2 <= end1 or
        start2 <= start1 <= end2 or
        start2 <= end1 <= end2
    )

print(mat)
ans1Arr = []
for s in seeds:
    for m in mat:
        for x in mat[m]:
            dest,sour,rang = x
            if(s in range(sour,sour+rang)):
                s_old= s
                s = dest + abs(s-sour)
                break
    ans1Arr.append(s)

ans1 = min(ans1Arr)

seeds2 = []
for i in range(0,len(seeds),2):
    seeds2.append(range(seeds[i],seeds[i]+seeds[i+1]))
seeds = seeds2 

ans2Arr = []
for s in seeds:
    for m in mat:
        for x in mat[m]:
            dest,sour,rang = x
            if(overlap(s.start,s.stop,sour,sour+rang)):
                s_old = s
                start = s.start
                stop = s.stop
                #clipping
                if(sour > s.start):
                    start = sour 
                if(sour+rang < s.stop):
                    stop = sour+rang
                #mapping
                if(sour < dest):
                    s = range(start+abs(sour-dest),stop+abs(sour-dest))
                else:
                    s = range(start-abs(sour-dest),stop-abs(sour-dest))

                print("match:",x,"-",s_old,"-->",s)
                ans2Arr.append(s.start)
                break
# 102509936
# 102509937
# 110321166
ans2 = min(ans2Arr)
print("----")
print("ans1:",ans1)
print("ans2:",ans2)
