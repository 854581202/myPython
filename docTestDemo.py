# -*- coding:utf-8 -*-
def fn(n):
    '''
    caculate 1*2*...*n
    >>> fn(1)
    1
    >>> fn(2)
    2
    >>> fn("s")
    Traceback (most recent call last):
    ...
    ValueError: expect arg be integer
    >>> fn(0)
    Traceback (most recent call last):
    ...
    ValueError: expect arg >= 1
    '''
    if not isinstance(n,int):
        raise ValueError("expect arg be integer")
    if n < 1:
        raise ValueError("expect arg >= 1")
    elif n==1:
        return 1
    elif n > 1:
        return n*(fn(n-1))

if __name__=="__main__":
    import doctest
    doctest.testmod()