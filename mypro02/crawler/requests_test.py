# encoding: utf-8
"""
@file: requests_test.py
@version: 1.0
@author: Atlantis
@time: 2020/12/9 21:29
@DESC: 
"""
import requests
# 如何使用：（requests模块的编码流程）
# - 指定url
# - 发起请求
# - 获取响应数据
# - 持久化存储

if __name__ == "__main__":
    #1.指定url
    url = 'https://www.sogou.com/'

    # 2.发起请求
    #get方法会返回一个响应对象
    response = requests.get(url=url)

    # 3.获取响应数据.text返回的是字符串形式的响应数据
    page_text = response.text
    print(page_text)

    # 4.持久化存储
    with open('./sogou.html','w',encoding='utf-8') as fp:
        fp.write(page_text)
    print('爬取数据结束！！！')


