# encoding: utf-8
"""
@file: re.py
@version: 1.0
@author: Atlantis
@time: 2021/8/11 16:26
@DESC: 查询出文本重复数据，输出到文件
"""
d = {}
for line in open('C:/Users/Blue water star/Desktop/1628774624981-1'):
    d[line] = d.get(line, 0) + 1
fd = open('d:/1628774624981.txt', 'w')
for k, v in d.items():
    if v > 1:
        fd.write(k)
fd.close()
