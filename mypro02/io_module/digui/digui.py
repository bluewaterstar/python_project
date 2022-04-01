# encoding: utf-8
"""
@file: digui.py
@version: 1.0
@author: Atlantis
@time: 2020/12/5 21:25
@DESC: 递归：函数直接或间接调用自身。
    递归头：什么时候不调用自己
    递归体：什么时候调用自己

    使用递归算法遍历目录下所有文件
"""
import os
# allfile = []
# def getFiles(path,level):
#     # 获取路径path下的文件和文件夹，返回的是一个列表
#     childFiles = os.listdir(path)
#     # 遍历列表
#     for file in childFiles:
#       # 把路径和文件做一个拼接
#         filepath = os.path.join(path,file)
#       # 如果拼接后还是一个文件夹路径，就再调用自己，直到是一个文件，level是一个变量，调一次方法+1，用于加制表符，显示层级
#         if os.path.isdir(filepath):
#             getFiles(filepath,level+1)
#         allfile.append("\t"*level+filepath)
# 传入当前路径，level为0
# getFiles(os.getcwd(),0)
#
# for f in reversed(allfile):
#     print(f)

file=[]
def digui(path):
    # listdir(路径) 返回路径下的文件和文件夹，是一个列表
    c=os.listdir(path)
    # print("这是当前路径下的问件及文件夹：",c)
    for a in c:
        b=os.path.join(path,a) # 父目录路径和里面的文件做一个连接
        if os.path.isdir(b): # 如果连接后还是一个文件夹，就还调用自己
            digui(b)
        # 如果不是文件夹了，就将对象追加到列表
        file.append(b)
        # print(b)

digui(os.getcwd())
for d in reversed(file):
    print(d)

