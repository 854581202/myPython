# -*- coding:utf-8 -*-

import time,random,queue
from multiprocessing.managers import BaseManager

task_queue = queue.Queue()
result_queue = queue.Queue()

class QueueManager(BaseManager):
    pass

QueueManager.register("get_task_queue",callable=lambda:task_queue)
QueueManager.register("get_result_queue",callable=lambda:result_queue)
manager = QueueManager(address=('127.0.0.1',5000),authkey=b'123')
manager.start()

task = manager.get_task_queue()
result = manager.get_result_queue()

for i in range(10):
    n = random.randint(0,10000)
    print("Put %s to worker"%n)
    task.put(n)

for i in range(10):
    my_result = result.get(timeout=10)
    print("receive from worker %s"%my_result)


manager.shutdown()
print("master exit")