# encoding: utf-8
"""
@file: while_test
@version: 1.0
@author: Atlantis
@time: 2020/4/20 12:30
"""
# num =0
# # sum_all=0
# # sum_even=0
# # sum_odd=0
# # while num<=100:
# #     sum_all +=num
# #     if num%2==0:sum_even +=num
# #     else:sum_odd +=num
# #     num +=1
# # print("1-100 所有数的累加和",sum_all)
# # print("1-100 偶数的累加和",sum_even)
# # print("1-100奇数的累加和",sum_odd)

# empNum=0
# salarySum=0
# salarys=[]
# while True:
#     s=input("请输入员工的薪资（按Q或q结束）：")
#     if s.upper()=='Q':
#         print("录入完成,退出")
#         break
#     if float(s)<0:
#         print('注意薪资是大于0的数字！！！')
#         continue
#     empNum += 1
#     salarys.append(float(s))
#     salarySum += float(s)
#
#     print("员工数{0}".format(empNum))
#     print("录入薪资",salarys)
#     print("平均薪资{0}".format(salarySum/empNum))

salarySum=0
salarys =[]
for i in range(4):
    s = input("请输入一共4名员工的薪资（按Q或q中途结束）:")

    if s.upper()=='Q':
        print("录入完成，退出")
        break
    if float(s)<0:
        continue
    salarys.append(float(s))
    salarySum += float(s)
else:
    print("您已经全部录入4名员工的薪资")
print("录入薪资：",salarys)
print("平均薪资{0}".format(salarySum/4))









