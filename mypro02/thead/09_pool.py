# encoding: utf-8
"""
@file: 09_pool.py
@version: 1.0
@author: Atlantis
@time: 2020/12/13 17:52
@DESC: 进程池非阻塞状态的使用:即使用apply_async(调用的对象,(传入对象的参数，是一个元组))
非阻塞：即保持进程池一直是满的，进程池里一个进程结束，等待的一个进程立马进入

0.导包，multiprocessing包下的Pool模块
1.定义一个执行任务的函数
2.使用Pool(进程数)创建进程池，可以定义进程池的大小，即有几个进程
3.进程池.apply_async()创建进程
4.进程池.close() 关闭进程池
5.进程池.join() 主进程等子进程结束再结束

"""
from multiprocessing import Pool
import time

# 创建任务执行的函数
def func(msg):
    print('start:',msg)
    time.sleep(2)
    print('end:',msg)

if __name__ == '__main__':
    #  创建进程数为3的进程池，也就是一次可以直接执行3个进程
    p=Pool(3)
    # 创建5个非阻塞进程
    for i in range(1,6):
        msg = '任务%d'%i
        # sopply_async(调用的方法,(传入前面调用方法的参数，是个元组))
        # 进程池满了之后，只有当一个进程执行完毕后会添加新的进程进去
        p.apply_async(func,(msg,))

    # 如果进程池不再接收新的请求，调用close
    p.close()
    p.join()
    print("主进程结束")
