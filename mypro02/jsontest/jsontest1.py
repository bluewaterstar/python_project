# encoding: utf-8
"""
@file: jsontest1.py
@version: 1.0
@author: Atlantis
@time: 2021/8/18 9:24
@DESC: 
"""
import sys
import json
# f=open('G:/renew.json',encoding='utf-8')
# #1.将数据导入程序
# data=json.load(f)
# #2.遍历data，打印列表中的每一个字典
# for dict_data in data:
#     print(str(dict_data['tagName']))


sys.stdout = open('E:/renewable_prod_tag.txt', mode = 'w',encoding='utf-8')
f=open('E:/renewable_prod.log',encoding='gb2312')
for line in f:
    t=(json.loads(line))
    print(t['tagName'])




