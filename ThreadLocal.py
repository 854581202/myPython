# -*- coding:utf-8 -*-

import threading

thread_local = threading.local()
def process_student():
    student = thread_local.student
    print("the %s is running with student %s"%(threading.current_thread().name,student))

def process_thread(name):
    thread_local.student = name
    process_student()

t1=threading.Thread(target=process_thread,args=("Alice",),name="ThreadStudentAlice")
t2=threading.Thread(target=process_thread,args=("Bob",),name="ThreadStudentBob")
t1.start()
t2.start()
t1.join()
t2.join()
print("End!")