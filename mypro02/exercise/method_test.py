# encoding: utf-8
"""
@file: method_test
@version: 1.0
@author: Atlantis
@time: 2020/4/21 17:07
"""
# class Person:
#     def say_hi(self):
#         print("hello")
#
#     def say_hi(self,name):
#         print("{0},hello".format(name))
# p1 = Person()
#
# p1.say_hi("齐天大圣")

class Person:
    def work(self):
        print("努力上班！")

def play_game(self):
    print('{0}玩游戏'.format(self))

def work2(s):
    print("好好工作")
Person.play =play_game
Person.work = work2
p =Person()
p.play()
p.work()

