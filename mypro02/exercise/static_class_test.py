# encoding: utf-8
"""
@file: static_class_test
@version: 1.0
@author: Atlantis
@time: 2020/4/21 15:18
"""
# class Student:
#     company='SXT'
#
#     @staticmethod
#     def add(a,b):
#         print("{0}+{1}={2}".format(a,b,(a+b)))
#         return a+b
# Student.add(20,30)

#析构对象
# class Person:
#     def __del__(self):
#         print("销毁对象:{}".format(self))
#
# p1=Person()
# p2=Person()
# del p2
# print("程序结束")


# 测试_call_,可调用对象
class SalaryAccount:
    def __call__(self,salary):
        yearSalary = salary*12
        daySalary = salary//30
        hourSalary =daySalary//8

        return
    dict(monthSalary=salary,yearSalary=yearSalary,daySalary=daySalary,hourSalary=hourSalary)
    s = SalaryAccount()
    print(s(5000))









