# -*- coding:utf-8 -*-
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

def count1():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
"""
f1, f2, f3 = count1()
print(f1())
print(f2())
print(f3())
"""

#-------------------------------------------------------
#每次调用打印一个不同的数
#-------------------------------------------------------

def createCount():
    def counter(i):
        def g():
            return i
        return g
    fs=[]
    for i in range(1,4):
        fs.append(counter(i))
    return fs

"""
f1,f2,f3 = createCount()
print(str(f1) + "value is " + str(f1()))
print(str(f2) + "value is " + str(f2()))
print(str(f3) + "value is " + str(f3()))
"""

#-------------------------------------------------------
#利用闭包返回一个计数器函数，每次调用它返回递增整数
#-------------------------------------------------------
def createIter():
    def int_iter():
        i = 0
        while True:
            yield i
            i = i + 1


    f = int_iter()
    def print_iter():
        return next(f)
    return print_iter


f = createIter()
print(f())
print(f())
print(f())
print(f())















