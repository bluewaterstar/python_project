# encoding: utf-8
"""
@file: 08_extends_process.py
@version: 1.0
@author: Atlantis
@time: 2020/12/13 1:22
@DESC: 使用继承的方式创建进程
1.继承Process类
2.如果有实例属性要初始化，需要重写init方法
3.重写run方法，方法体是进程要执行的任务
注：调用子进程时，用的是start()方法，但底层实际调的是run()方法，所以要重写run()方法，
    子进程的任务是什么，run()的方法体里写的就是什么。
4.创建子进程:类名()
"""
from multiprocessing import Process
import time

class ClockProcess(Process):
    # 如果有实例属性要初始化，要重写__init__()；interval属性要初始化
    def __init__(self,interval):
        # 调用父类初始化方法，初始化父类属性
        Process.__init__(self)
        # 初始化自己新增的实例属性
        self.interval = interval

    # 重写run方法，方法体是进程要执行的任务
    def run(self):
        print('子进程开始执行的时间：{}'.format(time.ctime()))
        # 传入了自身属性
        time.sleep(self.interval)
        print('子进程结束的时间:{}'.format(time.ctime()))

if __name__=='__main__':
    # 创建子进程
    p =ClockProcess(3)
    # 调用子进程
    p.start()
    p.join()
    print('主进程执行完')

