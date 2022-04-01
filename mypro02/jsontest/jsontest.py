# encoding: utf-8
"""
@file: jsontest.py
@version: 1.0
@author: Atlantis
@time: 2021/8/9 10:02
@DESC: 截取json文件生成建表语句（未去重）
"""

import sys

# sys.stdout = open('G:/data/0915_json/huaguang.sql', mode = 'w',encoding='utf-8')
sys.stdout = open('G:/wind.sql', mode = 'w',encoding='utf-8')
# with open('e:/Python/renewable_prod_cedian.txt', 'r',encoding='utf-8') as f:
#
#     for line in f:
#         # res = 'create table if not exists '+ 'zn_dc_stable_'+ line.replace('\n','') + ' using zn_dc_stable tags('+ line.replace('\n','')[0:4] + '.' + line.replace('\n','')[5:] + ');'
#         res = 'CREATE TABLE IF NOT EXISTS '+ 'zn_dc_stable_'+ line.replace('\n','').replace('.','_') + \
#               ' USING zn_dc_stable TAGS("'+ line.replace('\n','') + '");'
#
#         print(res)


# G:/DC_PI_KZS_HUAGUANGTANSHUILI_PROD.json
#
# 解析规则json，按逗号分隔，取第4个元素，将元素的字符替换、拼接
with open('E:/renewable_prod.log', 'r',encoding='utf-8') as f:

    for line in f:
        res = 'create table if not exists '+ 'zn_dc_stable_'+ line.replace('"tagName":','').replace('.','_').replace('"','').split(',')[1] + ' using zn_dc_stable tags('+  \
                       line.replace('"tagName":','').replace('\n','').split(',')[1] + ');'

        print(res)

# 单json
# sys.stdout = open('d:/BEIHAISHUILI.txt', mode = 'w',encoding='utf-8')
# # G:/DC_PI_KZS_HUAGUANGTANSHUILI_PROD.json
# with open('C:/Users/Blue water star/Desktop/DC_PI_KZS_BEIHAISHUILI_PROD.json', 'r',encoding='utf-8') as f:
#
#     for line in f:
#         res = 'create table if not exists '+ 'zn_dc_stable_'+ line.replace('"tagName":','').replace('.','_').replace('"','').replace('{','').replace('}','').replace('\n','') + ' using zn_dc_stable tags('+ \
#               line.replace('"tagName":','').replace('\n','').replace('{','').replace('}','') + ');'
#
#         print(res)




