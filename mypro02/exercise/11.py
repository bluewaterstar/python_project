# encoding: utf-8
"""
@file: 11.py
@version: 1.0
@author: Atlantis
@time: 2021/7/14 14:02
@DESC: 腾讯文档获取
"""
from urllib.request import urlopen
import requests
import re


url = 'https://docs.qq.com/dop-api/get/sheet'

params={
    "tab": "BB08J2",
    "padId": "300000000$EhOkQZvJjsDG",
    "subId": "BB08J2",
    "startrow": "1",
    "endrow": "3908",
    "xsrf": "8e89e8b50c062e6d",
    "_r": "0.16214436609786187",
    "outformat": "1",
    "normal": "1",
    "preview_token": "",
    "nowb": "1"
}

res=requests.get(url, params=params).text
names=re.findall('《(.*?)》',res)
print(names)
for name in names:
    print(name)