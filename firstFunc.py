# -*- coding: utf-8 -*-
import math

def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

def quadratic(a,b,c):
    x1 = (-b-math.sqrt(b*2 - 4*a*c))/(2*a)
    x2 = (-b + math.sqrt(b * 2 - 4 * a * c)) / (2 * a)
    return x1,x2

x1,x2 = quadratic(1,4,1)
print("x1=",x1)