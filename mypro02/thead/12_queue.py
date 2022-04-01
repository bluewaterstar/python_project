# encoding: utf-8
"""
@file: 12_queue.py
@version: 1.0
@author: Atlantis
@time: 2020/12/19 10:56
@DESC: 多线程中的队列 from multiprocessing import Queue
1.定义一个队列 Queue(队列长度) # 可以指定队列的大小，如果不写默认的队列是无限
2.往队列中添加元素 队列名.put('消息')
    # q.put('消息4',block=True,timeout=1)
    # put方法中可选参数 block=True,timeout=1 队列已经满了，等待1s，如果还是没有空余的空间，则跑队列已满的异常
3.队列是否已经满了 队列.full()
4.从队列中读取并一个个移除元素 队列名.get()
    #     print(q.get(block=True,timeout=1))
5.队列的大小 队列名.qsize()

"""
from multiprocessing import Queue
# 创建队列
q = Queue(3)
# 往队列中插入消息
q.put('消息1')
q.put('消息2')
q.put('消息3')

# q.put('消息4',block=True,timeout=1)
print('判断当前队列是否已满：',q.full())
if not q.full():
    q.put('消息4',block=True,timeout=1)

# 直接打印，得到的是队列对象的地址
print(q)
# get() 读取并删除元素
# print(q.get())

# 如果队列不为空，则获取里面的一个元素
# if not q.empty():
#     print(q.get(block=True,timeout=1))

# 获取队列大小(长度)
print('队列的大小：',q.qsize())

print(range(3)) # 得到 range(0, 3) 即range传入一个数，默认是会从0开始

# 遍历获取队列每一个元素
for i in range(q.qsize()):
    print(q.get())