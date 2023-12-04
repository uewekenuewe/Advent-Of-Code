import re
file1 = open('day3-ex.in', 'r')
file1 = open('day3.in', 'r')
Lines = file1.readlines()
arr = []
x = []
ans1 = 0
ans2 = 0
M = []
M_ = []
for l in Lines:
    l = l.strip()
    l2 = []
    nums = re.findall("\d+",l)
    nums2 = []
    for n in nums:
        if(len(str(n)) == 3):
            nums2.append(n)
            nums2.append(n)
            nums2.append(n)
        if(len(str(n)) == 2):
            nums2.append(n)
            nums2.append(n)
        if(len(str(n)) == 1):
            nums2.append(n)
    nums = nums2 
    k = 0
    for x in l:
        if x.isdigit():
            l2.append(int(nums[k]))
            k+=1
        else:
            if x == ".":
                l2.append(0)
            else:
                l2.append(x)
    

    M.append(l2)
print(M[-2])
print("----------")




for x in range(len(M)):
    for y in range(len(M[0])):
        if type(M[x][y]) == str:
            s = []
            if 0<= y+1 < len(M[0]):
                s.append(M[x][y+1])
            if 0<= y-1 < len(M[0]):
                s.append(M[x][y-1])

            top = []
            for dy in [1,0,-1]:
                if(0<=x-1 <len(M) and 0<=y+dy<len(M[0])):
                    if(M[x-1][y+dy] not in top):
                        top.append(M[x-1][y+dy])

            bottom = []
            for dy in [1,0,-1]:
                if(0<=x+1 <len(M) and 0<=y+dy<len(M[0])):
                    if(M[x+1][y+dy] not in bottom):
                        bottom.append(M[x+1][y+dy])                        
            s += top + bottom
            ans1 += sum(s)
            s2 = []
            for i in range(len(s)):
                if s[i] == 0:
                    continue
                else:
                    s2.append(s[i])
            s = s2
            if(M[x][y] == "*" and len(s) == 2):
                print(x,y,M[x][y],s)         
                ans2 += s[0]*s[1]       


# 596425
# 590764
print(ans1, ans1 == 532445)
print(ans2, ans2 == 79842967)