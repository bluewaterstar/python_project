# encoding: utf-8
"""
@file: test_requests.py
@version: 1.0
@author: Atlantis
@time: 2021/8/20 21:05
@DESC: 
"""
# 相当于打开浏览器，可以访问网址
import requests

# 输入网址，回车，因为地址是字符串，所以引号引起来，太长，起个名字为url
url ='https://www.baidu.com/'

resp = requests.get(url)
# 规定编码，gbk或utf-8，非必须，乱码时指定
resp.encoding='utf-8'
# 输出返回信息，输出格式要规定
print(resp.text)
# .text 以文本形式输出，用于阅读，看效果
# .content 以二进制的形式输出，用于保存数据

# with 确保异常打开关闭不损坏文件
# open 打开
# as 给前面代码起小名
# wb以二进制方式写入

with open('第一个爬虫.html','wb')  as f:
    f.write(resp.content)
