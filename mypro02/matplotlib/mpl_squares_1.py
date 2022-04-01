# encoding: utf-8
"""
@file: mpl_squares_1.py
@version: 1.0
@author: Atlantis
@time: 2020/12/17 21:35
@DESC: 修改标签文字及线条粗细
"""
#  pyplot包 包含很多生成图表的函数
from matplotlib import pyplot as plt
from matplotlib import font_manager as fm, rcParams


# 设置中文字体为黑体
plt.rcParams['font.sans-serif']=['SimHei'] # 显示中文标签
# 解决保存图像是负号'-'显示为方块的问题,或者转换负号为字符串
plt.rcParams['axes.unicode_minus']=False   # 字符显示



squares =[1,4,9,16,25]
# subplot() 可在一张图片上绘制一个或多张图表
fig,ax= plt.subplots()
# plot(数据) 根据数据绘制图表 ,linewidth可用以设置线宽
ax.plot(squares,linewidth=3)

# 设置图表标题、坐标轴标签
ax.set_title("平方数",fontsize=24)
ax.set_xlabel("值",fontsize=14)
ax.set_ylabel('值的平方',fontsize=14)

# 设置刻度标记的大小
ax.tick_params(axis='both',labelsize=14)


plt.show()

