# -*- coding:utf-8 -*-
import time,functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('call %s, at time : %s ms,the machine said %s' % (func.__name__,time.time(),text))
            return func(*args,**kw)
        return wrapper
    return decorator

@log("jsut a test")    #this is the decorator修饰器 相当于执行了 now = log('execute')(now)
def now():
    print("2019-10-24")

print(now())