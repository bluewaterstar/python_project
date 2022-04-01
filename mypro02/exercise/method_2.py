# encoding: utf-8
"""
@file: method_2.py
@version: 1.0
@author: Atlantis
@time: 2020/11/28 1:32
@DESC: 
"""
class Person :
    def work(self):
        print('好好工作！')

def play_game(a) :
    print("{0}在玩游戏".format(a))
Person.play = play_game
p = Person()
p.work()
p.play()
print(type(play_game),id(play_game))
print(type(Person.play),id(Person.play))
