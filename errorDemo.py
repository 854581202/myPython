# -*- coding:utf-8 -*-
from functools import reduce
import functools

#这是后加上去的，为了防止str2num处理“7.6”时报错。
def log(func):
    @functools.wraps(func)
    def wraper(*args,**kw):
        s = args[0]
        if "." in s:
            a,b=s.split(".")
            c=int(a)+int(b)/10**len(b)
            return func(c)
        else:
            return func(*args,**kw)
    return wraper

@log
def str2num(s):
    return int(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

now = log(str2num)
print(now("1"))
print(str(now.__name__))
main()