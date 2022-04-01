# encoding: utf-8
"""
@file: crawler.py
@version: 1.0
@author: Atlantis
@time: 2020/12/1 10:56
@DESC: 最简单的爬虫
"""
from urllib.request import urlopen

url = "http://www.baidu.com"
# 发送请求
response = urlopen(url)
# 读取内容
info = response.read()
# 打印内容
print(info.decode())

# 打印状态码
# print(response.getcode())
# # 打印真实url
# print(response.geturl())
# # 打印响应头
# print(response.info())
