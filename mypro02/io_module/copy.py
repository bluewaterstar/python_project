# encoding: utf-8
"""
@version: 1.0
@author: Atlantis
@file: copy 将文件中的一行复制成多行的数据
@time: 2022/4/1 11:11
"""


f = open("d:/逆变器.txt","r",encoding='gb18030')
f1 = open("d:/逆变器b.txt", "w", encoding='gb18030')
str = f.readlines()
#初始化为零  复制行数
x = 0
for i  in str:
    # 每复制 50 行  就把初始值 设为 0
    x = 0
    # 以下是定义复制 50 行
    while x < 50:
        f1.write(i)
        x += 1
        continue
# 关闭文件
f.close()
f1.close()