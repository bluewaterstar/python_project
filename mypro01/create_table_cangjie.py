# encoding: utf-8
"""
@file: create_table_cangjie
@version: 1.0
@author: Atlantis
@time: 2019/12/20 9:34
"""
# -*- coding: utf-8 -*-
import paramiko
# import email6
import smtplib
import poplib
from email.parser import Parser
import pandas as pd
import time

table = 'zherang_yesterday_data'#改表名zherang_yesterday_data、zherang_new_data
excel_path = 'C:/Users/Blue water star/Downloads/'+table+'.xlsx'#改路径C:\Users\Blue water star\Downloads
df = pd.read_excel(excel_path)#这个会直接默认读取到这个Excel的第一个表单
# data=df.head()#默认读取前5行的数据
row = len(df.index.values)
# data=df.ix[0].values
labels = list(df.columns.values)
# print (labels)
table_name = table
# print (table_name)
column = ''
column_select = ''
values = ''
for i in range(len(labels)):
    # print (len(labels))
    try:
        column_1 = labels[i].split('.')[1]
    except:
        column_1 = labels[i]
    column_select = column_select + column_1 + ','
    # data = df.loc[0, labels[i]]
    # print (data,type(data))
    if i == len(labels) - 1:
        # value = value + "'" + str(data) + "'"
        column = column + str(column_1) + " string\n"
    else:
        # value = value + "'" + str(data) + "'" + ','
        column = column + str(column_1) + " string,\n"
print(column_select)
#
# for j in range(row):
#     # print (j)
#     value = ''
#     for i in range(len(labels)):
#         # print (i)
#         data = df.loc[j,labels[i]]
#         if isinstance(data,str) is True :
#             data=data.replace(',','.')
#         if i == len(labels) - 1:
#             value = value + "'" + str(data) + "'"
#
#         else:
#             value = value + "'" + str(data) + "'" + ','
#     if j == row-1:
#         values = values + '(' + value + ')'
#     else:
#         values = values + '(' + value + '),'
#     values=values.replace('nan', '')

# print(value)
# print (column)
# insert_sql="insert into   db_test.data_tmp values %s" % values
# command_3='''hive -e "desc %s"''' % table

# 服务器相关信息,下面输入你个人的用户名、密码、ip等信息
ip = "172.17.40.241"
port = 22
user = "hive"
password = "souchehive"
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 建立连接
ssh.connect(ip, port, user, password, timeout=10)
#输入linux命令
command = '''hive -e "drop table if  exists db_test.zherang_yesterday_data "''' #表名
command_1 = '''hive -e "create table  db_test.zherang_yesterday_data (%s) ROW format delimited
fields terminated by ','
STORED AS TEXTFILE; "''' % column


# path='/Users/fengweixin/Downloads/%s.sql' % table
# f = open(path, 'w')  # 若是'wb'就表示写二进制文件
# f.write(insert_sql)
# f.close()

# print (command_1)
stdin, stdout, stderr = ssh.exec_command(command+';'+command_1, get_pty=True)


# 输出命令执行结果
result = stdout.read().decode(encoding='utf-8')
print(result)

# stdin_1,stdout_1,stderr_1 = ssh.exec_command(command_2,get_pty=True)
# time.sleep(5)

# 输出命令执行结果
# result = stdout_1.read().decode(encoding='utf-8')
# print((result))
# if 'Partition' in result:
#     print (1)
#     # Partition=result.split('\n')[-1].split(' ')[0]
#     Partition=result.split('\n')[-3].split(' ')[0]
#     print (Partition)
print(2)


#关闭连接
ssh.close()


#
# transport = paramiko.Transport(('172.17.40.241', 22))
# transport.connect(username='hive', password='souchehive')
#
# sftp = paramiko.SFTPClient.from_transport(transport)
# # 将location.py 上传至服务器 /tmp/test.py
# sftp.put('/Users/fengweixin/Downloads/%s.sql',
#          '/var/lib/hive/fengweixin/%s.sql') % (table,table)
# # 将remove_path 下载到本地 local_path
# # sftp.get('remove_path', 'local_path')
# transport.close()
