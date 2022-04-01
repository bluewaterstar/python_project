# encoding: utf-8
"""
@file: 02_creat_zijincheng.py
@version: 1.0
@author: Atlantis
@time: 2020/12/12 15:34
@DESC: 使用Process创建子进程
"""
# 正在运行的程序：称为进程

# 1.导入多进程模块
# 2.创建子进程函数
# 3.测试代码作为主进程，去调用子进程

# 导入多进程包multiprocessing的Process模块
from multiprocessing import Process

# 定义子进程
def run_test():
    print('--test--我是子进程')

if __name__ == '__main__':
    print('我是主进程，我开始执行了')
    # 创建子进程对象Process()，参数target接收调用的对象,只需要写方法名就可以了
    p = Process(target=run_test)
    # 启动进程，这将运行子进程，并调用该子进程中的run()函数
    p.start()