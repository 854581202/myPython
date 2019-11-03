# -*- coding:utf-8 -*-
import threading,time

def loop():
    print("The %s start working"%{threading.current_thread().name})
    for i in range(5):
        print("The %s >>> %s"%(threading.current_thread().name,i))
        time.sleep(1)
    print("The %s done these works"%{threading.current_thread().name})

"""

if __name__=="__main__":
    print("The %s begin."%(threading.current_thread().name))
    t=threading.Thread(target=loop,name="loopThread")
    t.start()
    t.join()
    print("The %s done"%{threading.current_thread().name})
"""

#-----------------------------------------------
#--------------no lock error--------------------
#-----------------------------------------------

balance = 0
def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n

def change(n):
    for i in range(1000000):
        change_it(n)

"""

if __name__ == "__main__":
    t1=threading.Thread(target=change,args=(5,))
    t2 = threading.Thread(target=change,args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("work done,we expect the variable balance's value is 0,but the variable balance's value is %s"%(balance))
"""

#---------------------------------------------------------------
#--------------but this no lock example can work right,why------
#---------------------------------------------------------------

balance1 = 0
def change_it1(n):
    global balance1
    balance1 = balance1 + n
    balance1 = balance1 - n

def change1():
    for i in range(1000000):
        change_it1(i)

"""
if __name__ == "__main__":
    t1 = threading.Thread(target=change1)
    t2 = threading.Thread(target=change1)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("work done,we expect the variable balance's value is 0,but the variable balance's value is %s"%(balance))    
"""

#-----------------------------------------------
#--------------lock ----------------------------
#-----------------------------------------------

balance = 0
lock = threading.Lock()
def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n

def change(n):
    for i in range(1000000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()

"""

if __name__ == "__main__":                                                                                          
    t1=threading.Thread(target=change,args=(5,))                                                                    
    t2 = threading.Thread(target=change,args=(8,))                                                                  
    t1.start()                                                                                                      
    t2.start()                                                                                                      
    t1.join()                                                                                                       
    t2.join()                                                                                                       
    print("work done,we expect the variable balance's value is 0,but the variable balance's value is %s"%(balance)) 
    
"""

#---------------------------------------------------------
#--------------one tread dead loop------------------------
#---------------------------------------------------------

def dead_loop():
    x=0
    while True:
        x = x + 1
        x = x - 1
"""

if __name__ == "__main__":
    print("the dead loop is running")
    t=threading.Thread(target=dead_loop)
    t.start()
    t.join()
    print("end")
"""

#---------------------------------------------------------
#--------------multi tread dead loop------------------------
#---------------------------------------------------------
import multiprocessing
def dead_loop():
    x=0
    while True:
        x = x + 1
        x = x - 1
"""
if __name__ == "__main__":
    print("the dead loop is running")
    for i in range(multiprocessing.cpu_count()):
        t=threading.Thread(target=dead_loop)
        t.start()
    print("end")
"""











