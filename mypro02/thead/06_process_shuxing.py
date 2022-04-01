# encoding: utf-8
"""
@file: 06_process_shuxing.py
@version: 1.0
@author: Atlantis
@time: 2020/12/12 17:01
@DESC: Pocess常用属性
# pid 获取进程的ID
# name 获取进程的名称
# is_alive()判断进程是否运行，True表示运行，False表示结束
"""
import multiprocessing
import time

def clock(interval):
    # 循环获取3次当前时间，间隔2秒
    for i in range(3):
        print("当前时间：{}".format(time.ctime())) # ctime() 获取时间戳字符串
        time.sleep(interval)


if __name__ == '__main__':
    print('主进程开始了')
    p = multiprocessing.Process(target=clock,args=(2,))
    p.start()
    # 子进程状态 True表示运行，False表示结束
    print('p.is_alive',p.is_alive())
    p.join()
    print('p.pid',p.pid)
    print('p.name',p.name)
    print('p.is_alive',p.is_alive())
