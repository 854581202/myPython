# -*- coding:utf-8 -(-
import os
from multiprocessing import Process
def multiProcessingDemo():
    pid = os.fork()
    print(pid)
    if pid == 0:
        print("I(%s) am child process,my father process is %s"%(os.getpid(),os.getppid()))
    else:
        print("I(%s) am father process,my child process is %s"%(os.getpid(),pid))

def print_test(name):
    print("%s is run on child process %s"%(name,os.getpid()))

"""
if __name__ == '__main__':
    print("the parent process(%s) is run"%(os.getpid()))
    p = Process(target=print_test,args=('test',))
    p.start()
    p.join()
    print("the child Process end!")
    
"""

#----------------------------
#-------------POOL-----------
#----------------------------

from multiprocessing import Pool
import os,time,random

def run_proc(name):
    print("%s process(%s) working"%(name,os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print("Task %s run %0.2f seconds"%(name,(end-start)))

"""
if __name__ == '__main__':
    print("The process (%s) start running!"%os.getpid())
    p=Pool(10)    #不是说好的，cpu是几核的，就能最多调用几个进程么，我虚拟机环境分配了4核，怎么还能一次同时调用10个进程。
    for i in range(11):
        p.apply_async(run_proc,args=(i,))
    p.close()
    p.join()
    print("All done")
    
"""

#-----------------------------------------------------------
#-------------subprocess control input and output-----------
#-----------------------------------------------------------

import subprocess
"""
print("$nslookup www.baidu.com")
r=subprocess.call(["nslookup","www.baidu.com"])
print("the result:",r)
"""

"""
print("$nslookup www.baidu.com")
p=subprocess.Popen(["nslookup"],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
output,err = p.communicate(b'set q=mx\nwww.baidu.com\nexit\n')
print(output.decode("utf-8"))
print("exit with",p.returncode)
"""



#-----------------------------------------------------------
#-------------Queue control input and output----------------
#-----------------------------------------------------------
from multiprocessing import Process,Queue
import os,time,random

def write(q):
    print("the write process is %s"%(os.getpid()))
    for i in ["A","B","C"]:
        print("%s is put to queue"%(i))
        q.put(i)
        time.sleep(random.random()*3)

def read(q):
    print("the read process is %s" % (os.getpid()))
    while True:
        message = q.get(True)
        print("the writer says %s"%(message))

"""

if __name__ == "__main__":
    print("The parent process is %s"%(os.getpid()))
    q=Queue()
    qw = Process(target=write,args=(q,))
    qr = Process(target=read,args=(q,))
    qw.start()
    qr.start()
    qw.join()
    qr.terminate()
    
"""