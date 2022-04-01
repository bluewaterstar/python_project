# encoding: utf-8
"""
@file: csvtest.py
@version: 1.0
@author: Atlantis
@time: 2021/8/9 15:17
@DESC:去除重复行后，写出到csv
"""

# 'sep' 是分隔符；
# 'header' 是否第一行作为DataFrame的column
# 'index_col' 是否把某一列作为DataFrame的Index
# import taos
import  pandas as pd
import gc
# 读取txt
train_data = pd.read_csv('E:/renewable_prod2.txt',
                         sep='\n ',
                         encoding='utf-8',
                         # index_col=0,
                         engine='python',
                         header=None)

# 删除特定行（包含‘打伞’的行）
#train_data[train_data[0].apply(lambda x: '打伞' not in x)]

# 去重
train_data.drop_duplicates(inplace=True)

train_data.set_index(0, inplace=True)

# 写入txt
train_data.to_csv('E:/renewable_prod.csv',
                  sep='\n',
                  encoding='utf-8',
                  header=None)
gc.collect()