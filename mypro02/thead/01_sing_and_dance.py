# encoding: utf-8
"""
@file: 01_sing_and_dance.py
@version: 1.0
@author: Atlantis
@time: 2020/12/12 15:13
@DESC: 模拟唱歌和跳舞
"""
from time import sleep

# 1.定义唱歌函数
# 2.定义跳舞函数
# 3.测试执行

# 唱歌
def sing():
    for i in range(3):
        print("我在唱歌...%d"%i)# %d是格式控制字符，代表十进制数；后面的%i，代表变量i要遵循前面的格式
        sleep(1)

# 跳舞
def dance():
    for i in range(3):
        print("我在跳舞...%d"%i)
        sleep(1)

# 测试 __name__和'__main__'相等，说明上面的代码运行没有问题
if __name__ == '__main__':
    sing()
    dance()
# 还唱歌还跳舞怎么办呢？