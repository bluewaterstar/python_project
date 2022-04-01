# encoding: utf-8
"""
@file: 1_write_a.py
@version: 1.0
@author: Atlantis
@time: 2020/12/4 15:40
@DESC: write()、writelines()练习
"""
f1 = open(r"d:/a1.txt","a",encoding="utf-8")
s1 ="越过长城，走向世界！"
f1.write(s1)
f1.close()

f = open(r"d:/aa.txt","w",encoding="utf-8")
s = ['孙悟空\n','猪八戒\n','沙悟净\n']
f.writelines(s)
f.close()
# PermissionError: [Errno 13] Permission denied: 'd:/aa.txt' 文件打开时，执行程序报的错

