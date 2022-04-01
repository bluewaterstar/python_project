# encoding: utf-8
"""
@file: 11_jincheng_no_share.py
@version: 1.0
@author: Atlantis
@time: 2020/12/19 10:02
@DESC:  多进程之间数据不共享
通过两个进程修改全局变量来测试
"""

# 导入模块
from multiprocessing import Process

num = 10
# 对全局变量加5的函数
def work1():
    global num
    num += 5
    print('子进程1运行后，num的值：',num)
# 对全局变量加10的函数
def work2():
    global num
    num += 10
    print('子进程2运行后，num的值：',num)

if __name__ == '__main__':

    print('主进程开始执行，num的值为：',num)
    p1=Process(target=work1)
    p2=Process(target=work2)
    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print('主进程执行完毕，num的值为：',num)

