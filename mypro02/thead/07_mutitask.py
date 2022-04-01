# encoding: utf-8
"""
@file: 07_mutitask.py
@version: 1.0
@author: Atlantis
@time: 2020/12/12 17:25
@DESC: 创建多个进程
"""
from multiprocessing import Process
from time import sleep


def work1(intervel):
    print('执行woke1')
    sleep(intervel)
    print('结束work1')


def work2(intervel):
    print('执行woke2')
    sleep(intervel)
    print('结束work2')


def work3(intervel):
    print('执行woke3')
    sleep(intervel)
    print('结束work3')


if __name__ == '__main__':
    print('执行主进程')
    p1 = Process(target=work1, args=(4,))
    p2 = Process(target=work2, args=(2,))
    p3 = Process(target=work3, args=(3,))

    # 调用子进程
    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    print('p1.name:',p1.name)
    print('p2.name:',p2.name)
    print('p3.name:',p3.name)
    print('主进程执行完了')


