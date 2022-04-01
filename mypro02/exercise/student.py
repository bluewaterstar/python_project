# encoding: utf-8
"""
@file: student.py
@version: 1.0
@author: Atlantis
@time: 2020/6/2 9:17
@DESC: 
"""
class Student:
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def say_score(self):
        print(self.name,'的分数是:',self.score)
s1 = Student('张三',80)
s1.say_score()
