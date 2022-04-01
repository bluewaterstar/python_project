# encoding: utf-8
"""
@file: copy
@version: 1.0
@author: Atlantis 不要将文件名与某个包名一样，不然引用的是文件而不是包
@time: 2020/4/20 16:56
"""
import copy

def testCopy():
    '''测试浅拷贝'''
    a = [10,20,[5,6]]
    b = copy.copy(a)

    print("a",a)
    print("b",b)
    b.append(30)
    b[2].append(7)
    print("浅拷贝。。。")
    print("a",a)
    print("b",b)


def testDeepCopy():
        '''测试深拷贝'''
        a=[10,20,[5,6]]
        b =copy.deepcopy(a)

        print("a",a)
        print('b',b)
        b.append(30)
        b[2].append(7)
        print("深拷贝，，，")
        print("a",a)
        print("b",b)

testCopy()
print("................")
testDeepCopy()















