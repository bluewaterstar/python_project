# encoding: utf-8
"""
@file: mpl_squares.py
@version: 1.0
@author: Atlantis
@time: 2020/12/7 10:43
@DESC: 使用pyplot包绘制折线图
"""
# pyplot 包含很多用于生成图表的函数
import matplotlib.pyplot as plt


# 建立绘制折线的列表
squares =[1,4,9,16,25]

# subplots() 可在一张图片中绘制一个或多个图表；变量fig表示整张图表，ax表示图片中的各个图片
fig,ax =plt.subplots()

# plot(数据) 的根据给定数据以有意义的方式绘制图表
ax.plot(squares)

# show()打开Matplotlib查看器并显示绘制的图表
plt.show()
