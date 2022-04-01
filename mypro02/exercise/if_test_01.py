# encoding: utf-8
"""
@file: if_test_01
@version: 1.0
@author: Atlantis
@time: 2020/4/17 17:56
"""

# num=input('请输一个小于10的整数：')
# if int(num)<10:
#     print(num)

# num =input("请输入一个整数：")
# if int(num)<10:
#     print(num)
# else:
#     print("数字太大，请输入一个小于10的整数")

# num =input("请输入一个数字：")
# print(num if int(num)<10 else "数字太大！")

# score = int(input('请输入分数：'))
# grade=''
# if score<60:
# #     grade="不及格"
# # if 60<=score<80:
# #     grade="及格"
# # if(80<=score<90):
# #     grade='良好'
# # if(90<=score<=100):
# #     grade="优秀"
# # print("分数是{0}，等级是{1}".format(score,grade))

# if score <60:
#     grade ='不及格'
# elif score<80:
#     grade="及格"
# elif score<90:
#     grade='良好'
# elif score<100:
#     grade='优秀'
# print('分数是{0}，等级是{1}'.format(score,grade))

# x = int(input('请输入x坐标：'))
# y = int(input('请输入y坐标：'))
#
# if(x==0 and y==0):print("原点")
# elif(x==0):print("y轴")
# elif(y==0):print("x轴")
# elif(x>0 and y>0):print("第一象限")
# elif(x<0 and y>0):print("第二象限")
# elif(x<0 and y<0):print("第三象限")
# else:
#     print("第四象限")

# score =int(input("请输入一个在0-100之间的数字："))
# grade =""
# if score >100 or score<0:
#     score = int(input('输入错误！请输入一个在0-100之间的数字：'))
# else:
#     if score >=90:
#         grade ="A"
#     elif score >=80:
#         grade='B'
#     elif score >=70:
#         grade='C'
#     elif score >=60:
#         grade='D'
#     else:
#         grade='E'
# print("分数为{0}，等级为{1}".format(score,grade))

score =int(input('请输入一个在0-100之间的数字：'))
degree ='ABCDE'
num =0
if score >100 or score<0:
    score =input("输入错误！请重新输入一个在0-100之间的数字：")
else:
    num=score//10
    if num<6:num=5
    print('分数是{0},等级是{1}'.format(score,degree[9-num]))







