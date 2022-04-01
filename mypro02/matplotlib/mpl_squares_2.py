# encoding: utf-8
"""
@file: mpl_squares_2.py
@version: 1.0
@author: Atlantis
@time: 2020/12/17 22:47
@DESC:  校正图形(之前图形4的平方是25，不对！！！)
"""
from matplotlib import pyplot as plt



input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]

# 使用样式matplotlib内置样式  内置样式已经对背景，线条粗细，字体，字号做了设置
# pyplot.style.use('样式')
plt.style.use('seaborn')

# 设置中文字体为黑体
plt.rcParams['font.sans-serif']=['SimHei'] # 显示中文标签
# 解决保存图像是负号'-'显示为方块的问题,或者转换负号为字符串
plt.rcParams['axes.unicode_minus']=False   # 字符显示

# subplots() 可在一张图上，绘制一个或多个图表
fig,ax =plt.subplots()
# plot(输入数据，输出数据，线宽)
ax.plot(input_values,squares,linewidth=3)

# 添加图表标题及给x轴，y轴加上标签
ax.set_title("平方根",fontsize=24)
ax.set_xlabel("值",fontsize=14)
ax.set_ylabel("值的平方根",fontsize=14)

# 设置x轴、y轴刻度值的字体大小
ax.tick_params(axis='both',labelsize=14)

plt.show()