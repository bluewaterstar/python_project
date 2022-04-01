# encoding: utf-8
"""
@file: ods_statistics_diff_v1.py
@version: 1.0
@author: Atlantis
@time: 2020/5/14 16:15
@DESC: 
"""
import os
import argparse
import subprocess
import random
import time
import json
import logging
import pymysql

import subprocess

from dayu.util.context import Context
from dayu.hooks.hive_server_hook import HiveServerHook
from dayu.exceptions import DayuException
from dayu.hooks.new_base_hook import NewBaseHook
from dayu.hooks.new_mysql_hook import NewMySQLHook
from dayu.util.enums import DATASOURCE_TYPE

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
curr = time.strftime('%Y%m%d', time.localtime(time.time()))
handler = logging.FileHandler("datalake_sqoop_table.log" + curr)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

console = logging.StreamHandler()
console.setLevel(logging.INFO)

logger.addHandler(handler)
logger.addHandler(console)
#mysql字段处理


###mysql表字段变化的表
def insert_diff(ds, hive_mysql_diff):
    print('--------------mmmmmmm---------')

    #table_diff = hive_table + ":" +  ",".join(hive_columns) +

    hql = '''
        INSERT into db_test.mysql_hive_table_diff
        select
          '%s' as id,
          '%s' as table_diff
        from db_test.oc_mysql_ins where id ='312'
    ''' % (ds, hive_mysql_diff)
    #随便一张表

    hive_conn_id="warehouse_hive"
    hiveserver = HiveServerHook(hive_conn_id)
    hql = Context().wrapper(hql)
    parms = hiveserver.get_records(hql)

###配置信息
def schema_info(ds):
    print('--------------nnnn---------')
    hql = '''
        select 
   `instance_code`, 
   `instance`,
    mysql_db,
    hive_db,
    username,
    passw
from db_test.db_info_belong
where mysql_db = 'starscream'
--where id in ('118','125','126')
    '''
    #随便一张表

    hive_conn_id="warehouse_hive"
    hiveserver = HiveServerHook(hive_conn_id)
    hql = Context().wrapper(hql)
    parms = hiveserver.get_records(hql)['data']

    return parms

#获取所有的表
def get_all_tables(mysql_db,instance_id,username,password):

    if username == None \
            or password == None \
            or instance_id == None \
            or mysql_db == None:
        logger.info("### get_all_tables 获取所有table时，缺少参数！")
        return []
    sqoop_cmd = "sqoop-list-tables --connect 'jdbc:mysql://%s:3306/%s?useUnicode=true&characterEncoding=utf-8&tinyInt1isBit=false&zeroDateTimeBehavior=convertToNull&serverTimezone=Asia/Shanghai' --username '%s' --password '%s'" % (
        instance_id, mysql_db, username, password)
    logger.info(">>>> get_all_tables sqoop_cmd {}".format(sqoop_cmd))
    p = os.popen(sqoop_cmd)
    result = p.read()
    return result.split("\n")[2:]

def get_all_hive_tables(hive_db,ods_hive):

    hql = "show tables in %s" % (hive_db)
    #hql = "show tables"
    #随便一张表
    print(hql)
    hive_conn_id="hive_%s" % (hive_db)
    #hive_conn_id.get_records(hql)
    print(hive_conn_id)
    hiveserver = HiveServerHook(hive_conn_id)
    hql2 = Context().wrapper(hql)
    parms = hiveserver.get_records(hql2)['data']
    hive_tables = []
    for parm in parms:
        if ods_hive in parm[0]:
            hive_tables.append(parm[0])
    print(hive_tables)
    return hive_tables

#mysql字段
def mysql_table_columns(instance_id, port, mysql_db, username, password, mysql_table):
    connect_param = {
        'host': instance_id,
        'port': port,
        'db': mysql_db,
        'user': username,
        'passwd': password,
        'charset': 'utf8',
        'use_unicode': True,
        'local_infile': True,
        'ssl': False
    }
    connector = pymysql.connect(**connect_param)
    mysql_columns = []
    cur = connector.cursor()

    print('-----aaaaaaaaa------------')

    try:
        cur.execute("SHOW FULL COLUMNS FROM `{}`".format(mysql_table))
        for row in cur.fetchall():
            col_name, data_type, collation, nullable, key, default, extra, privileges, comment = row
            mysql_columns.append(col_name)
    except Exception as e:
        logger.error(">>>>> get_source_table_column %s error" % (mysql_table))
        logger.error(e)
        raise RuntimeError(">>>>> get_source_table_column %s error" % (mysql_table))
    connector.commit()

    print('-----bbbbb------------')
    return mysql_columns

#hive字段处理
def hive_table_columns(hive_db,hive_table):

    hql = '''
        desc %s.%s
    ''' % (hive_db,hive_table)

    hive_conn_id="warehouse_hive"
    hiveserver = HiveServerHook(hive_conn_id)
    hql = Context().wrapper(hql)
    print('hql=',hql)
    parms = hiveserver.get_records(hql)['data']
    hive_columns = []
    for column in parms:
        hive_columns.append(column[0] )

    hive_columns.remove('ds')
    hive_columns.remove('ds')
    hive_columns.remove('')
    hive_columns.remove('')
    hive_columns.remove('# col_name            ')
    hive_columns.remove('# Partition Information')
    print(hive_columns)

    return hive_columns


def mysql_num(instance_id, port, mysql_db, username, password, mysql_table, ds_1):
    connect_param = {
        'host': instance_id,
        'port': port,
        'db': mysql_db,
        'user': username,
        'passwd': password,
        'charset': 'utf8',
        'use_unicode': True,
        'local_infile': True,
        'ssl': False
    }
    connector = pymysql.connect(**connect_param)
    cur = connector.cursor()
    print('-----aaaaaaaaa------------')

    cur.execute("select count(*) FROM `{0}` where date_create <= '{1}' or date_create is null ".format(mysql_table, ds_1))
    mysql_num = cur.fetchall()[0][0]
    print('mysql：')
    print(mysql_num)
    print(type(mysql_num))
    return mysql_num

#hivenum
def hive_num(hive_db,hive_table,ds):

    hql = '''
        select count(*) from %s.%s where ds ='%s'
    ''' % (hive_db,hive_table,ds)

    hive_conn_id="warehouse_hive"
    hiveserver = HiveServerHook(hive_conn_id)
    hql = Context().wrapper(hql)
    print('hql=',hql)
    parms = hiveserver.get_records(hql)['data'][0]
    hive_num = parms[0]
    print('hive')
    print(type(hive_num))
    return hive_num

if __name__ == '__main__':

    ds = '{{yesterday}}'
    ds_1 = '{{yesterday|delta(1)}}'
    mysql_tables, hive_table, ods_hive, mysql_columns, hive_columns, mysql_columns_lower = [], '', '', [], [], []
    mysql_num1, hive_num1, num_diff, date_diff, column_diff, table_diff = 0, 0, '', '', '', ''
    parms = schema_info(ds)
    port = 3306
    for parm in parms:
        instance_code = parm[0]
        instance_id = parm[1]
        #mysql库
        mysql_db = parm[2]
        #用户名
        username = parm[4]
        #用户名密码
        password = parm[5]
        #hive库
        hive_db = parm[3]
        #所有的表mysql
        ods_hive = 'ods_' + mysql_db.replace('-','_') + '_' + instance_code
        mysql_tables = get_all_tables(mysql_db,instance_id,username,password)
        hive_tables =  get_all_hive_tables(hive_db,ods_hive)
        for mysql_table in mysql_tables:
            hive_table = "ods_" + mysql_db.lower().replace('-','_') + "_" + instance_code + "_" + mysql_table.lower() + "_dd"
            if hive_table in hive_tables:
                mysql_columns = mysql_table_columns(instance_id, port, mysql_db, username, password, mysql_table)
                hive_columns = hive_table_columns(hive_db,hive_table)
                mysql_columns_lower = []
                for mysql_column in mysql_columns:
                    mysql_columns_lower.append(mysql_column.lower())
                #hive_columns_sort = sorted(hive_columns)
                #mysql_columns_sort = sorted(mysql_columns_lower)
                #print(hive_columns_sort)
                #print(mysql_columns_sort)
                #print(hive_columns_sort == mysql_columns_sort)
                #a = (hive_columns_sort == mysql_columns_sort)
                if hive_columns == mysql_columns_lower:
                    pass
                else:
                    column_diff += '|' + hive_table + ":" +  ",".join(hive_columns) + ',' + mysql_table + ":" +  ",".join(mysql_columns)
            else:
                table_diff += ',' +  mysql_db + ':' + mysql_table


    all_diff = 'num_diff:' + num_diff + ',date_diff:' + date_diff + ',column_diff:' + column_diff + ',table_diff:' + table_diff
    insert_diff(ds, all_diff)
