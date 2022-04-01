# encoding: utf-8
"""
@file: todotext.py
@version: 1.0
@author: Atlantis
@time: 2021/5/20 16:42
@DESC: 
"""
# 给读取到的每一行数据加上行号
with open(r"d:/1.txt","r",encoding="utf-8") as f:
    lines =f.readlines()
    # 读取完数据，使用枚举遍历
    lines = ['(' + line.replace('+08:00','').replace('}','').replace('("isGood":','').replace('"sendTS":','').replace('"tagName":','').replace('"piTS":','').replace('"tagValue":','').replace('\n','').split(',')[4] + "," \
             + line.replace('+08:00','').replace('}','').replace('("isGood":','').replace('"sendTS":','').replace('"tagName":','').replace('"piTS":','').replace('"tagValue":','').replace('\n','').split(',')[2] + "," \
             + line.replace('+08:00','').replace('}','').replace('("isGood":','').replace('"sendTS":','').replace('"tagName":','').replace('"piTS":','').replace('"tagValue":','').replace('\n','').split(',')[0] + "," \
             + line.replace('+08:00','').replace('}','').replace('("isGood":','').replace('"sendTS":','').replace('"tagName":','').replace('"piTS":','').replace('"tagValue":','').replace('\n','').split(',')[1] + '),'+'\n'  for index,line in enumerate(lines)] #使用列表推导式给lines从新赋值
    # lines = [line.replace('+08:00','').replace('}','').replace('("isGood":','').replace('"sendTS":','').replace('"tagName":','').replace('"piTS":','').replace('"tagValue":','')   for index,line in enumerate(lines)] #使用列表推导式给lines从新赋值

f = open(r"d:/3.txt","w",encoding="utf-8")
f.writelines(lines)
f.close()

# line= "abc,def,ggg"
# # print(line.split(',')[2])
# print(line)