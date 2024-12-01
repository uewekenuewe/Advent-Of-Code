# Using readlines()
import re
#file1 = open('day1-ex.in', 'r')
file1 = open('day1.in', 'r')
Lines = file1.readlines()
arr = []
x = []
sum = 0
values = ["1","2","3","4","5","6","7","8","9","one", "two", "three", "four", "five", "six", "seven", "eight",  "nine"]
written = ["one", "two", "three", "four", "five", "six", "seven", "eight",  "nine"]
## part 1
# for l in Lines:
#     numbers = re.findall("\d",l)
#     x = numbers[0] + numbers[-1]
#     sum += int(x)
#     numbers = [int(x) for x in numbers]

print(sum)
sum = 0
for l in Lines:
    ind = {}
    a = ("",9999)
    b = ("",-1)
    for v in values:
        ind = l.find(v)
        if(ind < a[1] and ind != -1):
            a = (v,ind)
        ind = l.rfind(v)
        if(ind > b[1] and ind != -1):
            b = (v,ind)

    if b[0] in written:
        b = str(written.index(b[0])+1)
    else: 
        b = b[0]
    if a[0] in written:
        a = str(written.index(a[0])+1)      
    else:
        a = a[0]
    n = a+b   
    sum += int(n)

sum = 0
for l in Lines:
    nums = []
    for i in range(len(l)):
        if l[i].isdigit():
            nums.append(int(l[i]))
        else:
            for v in values:
                if l[i:i+len(v)] in written:
                    nums.append(written.index(l[i:i+len(v)])+1)
                    break
    sum += int(str(nums[0]) + str(nums[-1]))
# 54643
# 51288
# 51562
# 54719 !!
print(sum) 
