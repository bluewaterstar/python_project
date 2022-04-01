# encoding: utf-8
"""
@file: 3_walk.py
@version: 1.0
@author: Atlantis
@time: 2020/12/5 14:37
@DESC: 显示指定路径下的文件夹和文件路径
"""
import os

all_file =[]

# 获取项目当前路径
path =os.getcwd()
print("这是当前路径：",path)
# walk() 可以遍历指定路径的所有文件夹和文件，返回的是个迭代器对象
list_files= os.walk(path)
print("这是walk方法返回的生成器对象：",list_files)

for dirpath,dirnames,filenames in list_files:
    print("当前目录路径及子目录路径：",dirpath) # 当前文件夹路径及子文件夹路径
    # print("目录下包含的子目录：",dirnames) # 目录下的文件夹
    # print("目录下的所有文件，包含子目录下的：",filenames) # 目录下的文件及子目录下的文件
    # for dir in dirnames:
    #     # 让当前目录dirpath和子目录dirnames做拼接，拼接后追加到列表中
    #     all_file.append(os.path.join(dirpath,dir))
    #     #print(dir)
    for name in filenames:
        # 让当前目录dirpath和目录里的文件做拼接
        all_file.append(os.path.join(dirpath,name))
        #print(name)

# 遍历打印得到的列表
for file in all_file:
    print("这是列表all_file里的值：",file)
