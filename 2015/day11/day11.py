import re
import sys
import numpy as np
import copy 

ans1 = 0
ans2 = 0

l = "vzbxkghb"

def password_valid(pw:str):
    if "i" in pw or "o" in pw or "l" in pw:
        return -1
    stright_increasing = False
    for i in range(len(pw)-2):
        if ord(pw[i])+1 == ord(pw[i+1]) and ord(pw[i])+2 == ord(pw[i+2]):
            stright_increasing = True
    if not stright_increasing:
        return -2 

    diff_segments = False
    seg1 = ""
    for v,c in seg(pw):
        if c >= 2 and seg1 == "": 
            seg1 = v 
        if c >= 2 and seg1 != "":
            if seg1 != v:
                diff_segments = True
                break


    if not diff_segments:
        return -3
    

    return 1

def seg(line:str):
    result = [[line[0],1]]
    for i in range(1,len(line)):
        if result[-1][0] == line[i]:
            result[-1][1]+=1
        else:
            result.append([line[i],1])
    return result

def increment_password(pw:str):
    pw_num = [ord(x)-ord('a') for x in pw]
    pw_num[-1] += 1 
    for i in range(len(pw_num)-1,-1,-1):
       if  pw_num[i]>= 26:
            pw_num[i] = pw_num[i] % 26
            pw_num[i-1] += 1
       else:
            break
    result = ""
    for i in range(len(pw_num)):
        result += chr(pw_num[i]+ord('a'))
    return result



current_pw = "vzbxkghb"
while(password_valid(current_pw) < 0):
    current_pw = increment_password(current_pw)

ans1 = current_pw
current_pw = increment_password(current_pw)
while(password_valid(current_pw) < 0):
    current_pw = increment_password(current_pw)

ans2 = current_pw
print("------")
print("ans1:", ans1)
print("ans2:", ans2)


