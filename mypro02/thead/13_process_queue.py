# encoding: utf-8
"""
@file: 13_process_queue.py
@version: 1.0
@author: Atlantis
@time: 2020/12/19 11:47
@DESC: 通过队列进行队列之间的通信
"""
# 1.导包
from multiprocessing import Process,Queue
from time import sleep

# 2.定义写入队列数据的方法
def writer(q):
    a=['a','b','c','d']
    for i in a:
        print('开始写入的值：%s'%i)
        q.put(i)
        sleep(1)
# 3.定义读取队列数据的方法
def reader(q):
    for i in range(q.qsize()):
        print('读取到的队列的值:%s'%q.get())
        sleep(1)

# 创建进程测试
if __name__=='__main__':
    # 创建队列
    q =Queue()
    p=Process(target=writer,args=(q,)) # 注意创建进程时传入的参数
    p2=Process(target=reader,args=(q,))

    p.start()
    p.join()

    p2.start()
    p2.join()




