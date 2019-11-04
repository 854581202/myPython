# -×- coding:utf-8 -*-
#fact(n) = n! = 1 x 2 x 3 x ... x (n-1) x n = (n-1)! x n = fact(n-1) x n

def fact(n):
    if n == 1:
        return 1
    return n*fact(n-1)


print(fact(10))