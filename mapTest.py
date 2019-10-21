# -*- coding:utf-8 -*-

def f(x):
    return x*x

#r = map(f,[1,2,3,4,5])
#print(list(r))

#------------------------------------
def normalize(strs):
    isHead = True
    newStr=""
    for c in strs:
        if isHead:
            newStr= newStr + c.upper()
            isHead = False
        else:
            newStr= newStr + c.lower()
    return newStr

#strs = ['adam', 'LISA', 'barT']
#print(list(map(normalize,strs)))

#----------------------------------------
#Python提供的sum()函数可以接受一个list并求和，
#请编写一个prod()函数，可以接受一个list并利用reduce()求积：
#----------------------------------------
from functools import reduce
def prod(num1,num2):
    return num1 + num2

#myList = [1,2,3,4]
#print(reduce(prod,myList))

#---------------------------------------------
#    利用map和reduce编写一个str2float函数，
#    把字符串'123.456'转换成浮点数123.456：
#--------------------------------------------

def transfer(c):
    int_str_table = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,".":"."}
    return int_str_table[c]

def splitStr(mystr):
    i = -1
    for str in mystr:
        i = i + 1
        if(str == "."):
            return mystr[:i],mystr[(i+1):]


def strToFloat(num1,num2):
     return num1*10 + num2


#strs="1314.520"
#strsUpper ,strsLower= splitStr(strs)
#varIntUpper = reduce(strToFloat,map(transfer,strsUpper))
#varIntLower = reduce(strToFloat,map(transfer,strsLower)) /10**len(strsLower)   #这里/10**len(strsLower)完全没想到
#print(varIntLower + varIntUpper)

#---------------------------------------------
#    优化后
#    利用map和reduce编写一个str2float函数，
#    把字符串'123.456'转换成浮点数123.456：
#--------------------------------------------
def strToFloat2(num1, num2):
    return num1 * 10 + num2

def transfer2(strs):
    n=strs.index(".")
    strUpper=list(map(int,strs[:n]))
    strLower=list(map(int,strs[n+1:]))
    intUpper=reduce(strToFloat2,strUpper)
    intLower=reduce(strToFloat2,strLower)/(10**len(strLower))
    print(intUpper + intLower)

strs="1314.520"
transfer2(strs)