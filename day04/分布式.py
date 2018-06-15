import time
from multiprocessing.managers import BaseManager
from queue import Queue


# 创建QueueManager:
class QueueManager(BaseManager):
   pass


# QueueManager从网络上获取Queue
QueueManager.register('my_task_queue')
QueueManager.register('my_result_queue')

# 连接到服务器
server_address = '10.35.163.57'
print('Connect to server %s...' % server_address)

manager = QueueManager(address = (server_address, 5000), authkey = 'Hydra'.encode())
# 从网络连接:
manager.connect()
# 获取Queue的对象:
task = manager.my_task_queue()
result = manager.my_result_queue()
# 从task队列取任务,并把结果写入result队列:
for i in range(10):
   try:
      n = task.get(timeout = 1)
      print('run task{}:{}'.format(i, n))
      time.sleep(1)
      result.put('yeah!' + str(i))
   except Queue.empty:
      print('task queue is empty.')
# 处理结束:
print('worker exit.')
