# -*- coding:utf-8 -*-
import queue,time
from multiprocessing.managers import BaseManager
class QueueManager(BaseManager):
    pass

QueueManager.register("get_task_queue")
QueueManager.register("get_result_queue")
m = QueueManager(address=("127.0.0.1",5000),authkey=b'123')
m.connect()

task = m.get_task_queue()
result = m.get_result_queue()

for i in range(10):
    try:
        myTask = task.get(timeout=1)
        print("recieve from server %s"%myTask)
        myTask_2 = myTask * myTask
        result.put(myTask_2)
        print("send %s to server"%myTask_2)
        time.sleep(1)
    except queue.Empty:
        print("queue is empty!")

print("worker exit")