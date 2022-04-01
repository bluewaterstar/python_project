# encoding: utf-8
"""
@file: 10_pool_apply.py
@version: 1.0
@author: Atlantis
@time: 2020/12/14 10:40
@DESC: 线程池的阻塞状态：每次只能执行一个进程，不管进程池有多大
apply(函数,(传参,))
"""
# 导包
from multiprocessing import Pool
import time

def func(msg):
    print('进程开始:%d'%msg)
    time.sleep(2)
    print('结束进程:%d'%msg)

if __name__=='__main__':
    p = Pool(3)
    # 使用apply() 创建非阻塞进程
    for i in range(1,6):
        msg='任务%d'%i
        p.apply(func,(msg,))

    p.close()
    p.join()


