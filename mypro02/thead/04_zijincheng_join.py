# encoding: utf-8
"""
@file: 04_zijincheng_join.py
@version: 1.0
@author: Atlantis
@time: 2020/12/12 16:11
@DESC: join()等子进程结束在结束主进程
"""
from multiprocessing import Process
from time import sleep

def worker(interval):
    print('子进程开始')
    sleep(interval)
    print('子进程结束')

if __name__ == '__main__':
    print('主进程开始运行了')
    p = Process(target=worker,args=(3,))
    p.start()
    # sleep(4)
    # 等子进程结束再结束子进程
    p.join()
    print('主进程结束了')








