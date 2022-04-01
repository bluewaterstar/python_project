# encoding: utf-8
"""
@file: lianxi.py
@version: 1.0
@author: Atlantis
@time: 2020/11/23 0:00
@DESC: 
"""
# def make_album(geshouname,zhuanjiname):
#     geshouxinxi ={'歌手':geshouname,'专辑名字':zhuanjiname}
#     return geshouxinxi
#
#
# while True :
#     geshou = input('歌手：')
#     if geshou == 'Q':
#         break
#     zhuanji = input('专辑：')
#     if zhuanji == 'Q' :
#         break
#
# geshoujieshao = make_album(geshou,zhuanji)
# print(geshoujieshao)


def make_album(geshouname,zhuanjiname,zhuanjishu=None):
    zhuanjixinxi = {'歌手':geshouname,'专辑':zhuanjiname}
    if zhuanjishu :
        zhuanjixinxi['专辑数'] = zhuanjishu
    return zhuanjixinxi

geshou = '请输入歌手名字：'
zhuanji = '请输入专辑名字：'

while True :
    print('输入q，退出')
    a = input(geshou)
    if a == 'q' :
        break
    b = input(zhuanji)
    if b == 'q' :
        break

    c = make_album(a,b)
    print(c)