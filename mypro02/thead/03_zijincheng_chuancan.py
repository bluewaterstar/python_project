# encoding: utf-8
"""
@file: 03_zijincheng_chuancan.py
@version: 1.0
@author: Atlantis
@time: 2020/12/12 15:49
@DESC: 子进程传参
"""
# 1.导多进程包multiprocessing的Process类
# 2.创建带参的任务
# 3.调用任务并传参

from multiprocessing import Process
from time import sleep

def run_test(name,age,**kwargs):
    print('子进程运行 name的值：%s,age的值：%d'%(name,age)) # 后面的这个%前面不能有逗号
    print('字典kwargs:',kwargs)
    sleep(0.5)

if __name__ == '__main__':
    print('主进程开始运行')
    # target接收调用对象，args接收元组，kwargs接收字典
    p1 = Process(target=run_test,args=('孙悟空',500),kwargs={'猪八戒':600})
    print('开始子进程')
    p1.start()
    print('结束主进程')
