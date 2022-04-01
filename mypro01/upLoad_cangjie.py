# encoding: utf-8
"""
@file: upLoad_cangjie
@version: 1.0
@author: Atlantis
@time: 2019/12/20 10:48
"""
import paramiko

transport = paramiko.Transport(('172.17.40.241', 22))
transport.connect(username='hive', password='souchehive')

sftp = paramiko.SFTPClient.from_transport(transport)
# 将location.py 上传至服务器 /tmp/test.py
sftp.put('C:/Users/Blue water star/Downloads/zherang_yesterday_data.csv',#要上传的文件C:\Users\Blue water star\Downloads
         '/var/lib/hive/fengweixin/zherang_yesterday_data.csv')#表的路径
# 将remove_path 下载到本地 local_path
# sftp.get('remove_path', 'local_path')
transport.close()
