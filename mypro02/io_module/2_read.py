# encoding: utf-8
"""
@file: 2_read.py
@version: 1.0
@author: Atlantis
@time: 2020/12/4 17:41
@DESC: read()、readline()、readlines()
"""
# 读取4个字符
with open(r"d:/a1.txt","r",encoding="utf-8") as f:
    print(f.read(4))

# 读取全部
with open(r"d:/a1.txt","r",encoding="utf-8") as d:
    print(d.read())

# 按行读取一个文件
with open(r"d:/aa.txt","r",encoding="utf-8") as c:
    while True:
        a=c.readline()
        # 如果没有值就停止，有值就打印
        if not a:
            break
        else:
            print(a,end="")
print("...................")
# 使用迭代器读取每一行
with open(r"d:/aa.txt","r",encoding="utf-8") as e:
    for i in e:
        print(i,end="")

print("***************")
# 给读取到的每一行数据加上行号
with open(r"d:/aa.txt","r",encoding="utf-8") as f:
    for i in range(5):
        lines =f.readlines()
    # 读取完数据，使用枚举遍历
    # lines = [line.rstrip()+"#"+str(index +1) for index,line in enumerate(lines)] #使用列表推导式给lines从新赋值
    # lines = [line.rstrip()+"#"+str(index +1) for index,line in enumerate(lines)] #使用列表推导式给lines从新赋值
with open(r"d:/bb.txt","a",encoding="utf-8") as g:
        g.writelines(lines)

# 二进制文件的读取和写入
# with open(r'd:/490.jpg',"rb") as h:
#     with open(r"d:/480.jpg","wb") as j:
#         for k in h.readlines():
#             j.write(k)
# print("图片复制完成")
