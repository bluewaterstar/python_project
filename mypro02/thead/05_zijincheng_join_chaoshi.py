# encoding: utf-8
"""
@file: 05_zijincheng_join_chaoshi.py
@version: 1.0
@author: Atlantis
@time: 2020/12/12 16:49
@DESC: join(超时时间) 也就是等待子进程多久
"""
from multiprocessing import Process
from time import sleep

def worker(interval):
    print("子进程开始啦！")
    sleep(interval)
    print('子进程结束喽！')

if __name__ == '__main__':
    print('主进程开始了')
    p = Process(target=worker,args=(5,))
    p.start()
    p.join(3) # 只等子进程3秒，若没有3的话要一直等子进程结束
    print('主进程结束了')
