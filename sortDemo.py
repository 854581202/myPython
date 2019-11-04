# -*- coding:utf-8 -*-
def dependOnName(s):
    return s[0]

def dependOnGrade(s):
    return s[1]

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L_New = sorted(L,key=dependOnGrade)
print(L_New)

