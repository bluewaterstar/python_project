# encoding: utf-8
"""
@file: task_inita.py
@version: 1.0
@author: Atlantis
@time: 2020/6/4 18:08
@DESC: 新大禹建任务依赖的包
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import copy, os
import requests, json

def task_inita_ods(mysqlschema, instance, task_code):
    inita = """ 
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


#sqoop 到分区表
def load_by_sqoop(instance_id, mysql_db, username, password, tmp_hive_table, mysql_table, hive_db, map_columns , ds):
    
    #实例
    instance_id = instance_id
    #mysql库
    db = mysql_db
    #用户
    username = username
    #密码
    password = password
    #hive表
    hive_table = tmp_hive_table
    timestamp = int(time.time() * 1000)
    table = mysql_table
    #hive库
    hive_db = hive_db
    #字段
    map_cloumns = map_columns
    diff_table = ''
    print(map_cloumns)
    
    ds = ds
    print(ds)
    
    connection_url = "jdbc:mysql://{}:3306/{}?useUnicode=true&characterEncoding=utf-8&tinyInt1isBit=false&zeroDateTimeBehavior=convertToNull&serverTimezone=Asia/Shanghai".format(
        instance_id,
        db)

    sqoop_import_cmdb = '''
                        sqoop import -Dmapred.job.queue.name=etl --verbose  \\\\
                            --connect '%s' \\\\
                            --username '%s' \\\\
                            --password '%s' \\\\
                            --num-mappers 1 \\\\
                            --as-textfile \\\\
                            --hive-overwrite \\\\
                            --create-hive-table \\\\
                            --hive-drop-import-delims \\\\
                            --hive-import \\\\
                            --null-string '\\\\\\\\N' \\\\
                            --null-non-string '\\\\\\\\N' \\\\
                            --hive-table '%s' \\\\
                            --target-dir 'hdfs://NameNodeHACluster/user/souche/tbls/%s_%d_%d' --delete-target-dir   \\\\
                            --table %s \\\\
                            --mapreduce-job-name '%s_%d' \\\\
                            --hive-database %s \\\\
                            --map-column-java '%s' \\\\
                            --map-column-hive '%s'
                    ''' % (
            connection_url, username, password, hive_table, hive_table, timestamp, random.randint(0, 100000),
            table,
            hive_table,
            timestamp, hive_db, ",".join(map_cloumns), ",".join(map_cloumns))
    
    print(sqoop_import_cmdb)

    tmp_hive_table = 'tmp0_' + hive_table

    drop_table_ddl = "DROP TABLE IF EXISTS %s.%s" % (hive_db, hive_table)
    
    hive_conn_id="warehouse_hive"
    hiveserver = HiveServerHook(hive_conn_id)
    hql = Context().wrapper(drop_table_ddl)
    parms2 = hiveserver.get_records(drop_table_ddl)
    print(parms2)
    print('-----------------ffffffffffff------')
    
    try:
        p = subprocess.Popen(sqoop_import_cmdb, shell=True, close_fds=True, stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, stderr = p.communicate()

        if p.returncode != 0:
            raise DayuException("Cannot execute {} on {}. Error code is: "
                            "{}. Output: {}, Stderr: {}"
                            .format(sqoop_import_cmdb, 'db_pay',
                                    p.returncode, output, stderr))
    except Exception as err:
        diff_table = table
        logger.info(">>>>>[error] import table instance_id=[%s] db=[%s] table=[%s]" % (instance_id, db, table))
    finally:
        pass
    return diff_table

#mysql字段处理

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

def exc_insert_sql(hive_db, hive_table, hive_columns, tmp_hive_table, ds):
    print('--------------cccccc---------')
    hql = '''
        INSERT OVERWRITE TABLE %s.%s PARTITION(ds='%s')
        select
          %s
        from %s.%s
    ''' % (hive_db, hive_table, ds, ",".join(hive_columns), hive_db, tmp_hive_table)

    hive_conn_id="warehouse_hive"
    hiveserver = HiveServerHook(hive_conn_id)
    hql = Context().wrapper(hql)
    parms = hiveserver.get_records(hql)

    print('hql=',hql)

    drop_table_ddl = "DROP TABLE IF EXISTS %s.%s" % (hive_db, tmp_hive_table)
    drop_table_ddl = Context().wrapper(drop_table_ddl)
    parms2 = hiveserver.get_records(drop_table_ddl)

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
def schema_info(instance_id, mysql_db):
    print('--------------nnnn---------')
    
    #table_diff = hive_table + ":" +  ",".join(hive_columns) +  
    
    hql = '''
        select
   `instance_code`,
   `instance`,
    mysql_db,
    hive_db,
    username,
    passw
from db_test.db_info_belong
where instance ='%s' and mysql_db = '%s'
    ''' % (instance_id, mysql_db)
    #随便一张表

    hive_conn_id="warehouse_hive"
    hiveserver = HiveServerHook(hive_conn_id)
    hql = Context().wrapper(hql)
    parms = hiveserver.get_records(hql)['data']

    return parms

#获取所有的表
def get_all_tables(mysql_db,instance_id,username,password):
    
    if username == None \\
            or password == None \\
            or instance_id == None \\
            or mysql_db == None:
        logger.info("### get_all_tables 获取所有table时，缺少参数！")
        return []
    sqoop_cmd = "sqoop-list-tables --connect 'jdbc:mysql://%s:3306/%s?useUnicode=true&characterEncoding=utf-8&tinyInt1isBit=false&zeroDateTimeBehavior=convertToNull&serverTimezone=Asia/Shanghai' --username '%s' --password '%s'" % (
        instance_id, mysql_db, username, password)
    logger.info(">>>> get_all_tables sqoop_cmd {}".format(sqoop_cmd))
    p = os.popen(sqoop_cmd)
    result = p.read()
    result1 = result.split("\\n")[2:]

    return result1

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
        """

    aaa = """
if __name__ == '__main__':
    
    #库 'ft_city_bank_account_config'
    mysql_db = '{mysql_db}'
    #实例
    instance_id = '{instance_id}'
    
    parm = schema_info(instance_id, mysql_db)[0]
    print(parm)
    #实例编码
    instance_code = parm[0]
    #用户名
    username = parm[4]
    #用户名密码
    password = parm[5]
    #hive库
    hive_db = parm[3]
    port = 3306
    ds = '{{{{yesterday}}}}'
    ods_hive = 'ods_' + mysql_db.replace('-','_') + '_' + instance_code

    mysql_tables = get_all_tables(mysql_db,instance_id,username,password)
    hive_tables =  get_all_hive_tables(hive_db,ods_hive)

    mysql_table, hive_table, mysql_columns, hive_columns, mysql_columns_sort, hive_columns_sort, hive_mysql_diff, map_columns, table_diff, mysql_columns_lower, hive_columns_string = '', '', [], [], [], [], '', [], '', [], []
    column_diff, table_diff, diff_table, import_table_diff = '', '', '', ''
    db = mysql_db.replace('-','_')
    
    for table in mysql_tables: 
        hive_table = "ods_" + db.lower() + "_" + instance_code + "_" + table.lower() + "_dd"
        tmp_hive_table = "tmp0_" + hive_table
        mysql_table = table
        map_columns = []
        mysql_columns_lower = []
        hive_columns_string = []
        if hive_table in hive_tables :
            mysql_columns = mysql_table_columns(instance_id, port, mysql_db, username, password, mysql_table)
            hive_columns = hive_table_columns(hive_db,hive_table)
            for column in mysql_columns:
                map_columns.append("%s=String" % (column))
                mysql_columns_lower.append(column.lower())
            for hive_column in hive_columns:
                hive_columns_string.append('`' + hive_column + '`')
            mysql_columns_sort = sorted(mysql_columns_lower)
            #print(mysql_columns_sort)
            hive_columns_sort = sorted(hive_columns)
            #print(hive_columns_sort)
            if mysql_columns_sort == hive_columns_sort:
                diff_table = load_by_sqoop(instance_id, mysql_db, username, password, tmp_hive_table, mysql_table, hive_db, map_columns , ds)
                if diff_table == '':
                    exc_insert_sql(hive_db, hive_table, hive_columns_string, tmp_hive_table, ds)
                else:
                    import_table_diff += "," + diff_table
            else:
                column_diff = '|' + hive_table + ":" +  ",".join(hive_columns) + ',' + mysql_table + ":" +  ",".join(mysql_columns)
        else:
            table_diff += ',' + mysql_db + ':' + mysql_table
        
    hive_mysql_diff = column_diff + ',' + 'import_table_diff:' + import_table_diff + ',' + 'table_diff:' + table_diff
    insert_diff(ds, hive_mysql_diff)
        """.format(mysql_db=mysqlschema, instance_id=instance)

    pyt = inita + aaa

    parms, config, basic = {}, {}, {}

    #parms["task_id"] = task_id

    # config["sql"] = "select 1"
    config["source_code"] = pyt
    # config["conn_id"] = "1090"
    config["python_bin"] = "python3"
    # config["source_key"] = "hive_dl_ycgj"

    parms["config"] = copy.deepcopy(config)

    basic["app_id"] = "33"
    basic["app_name"] = "数据湖"

    #依赖
    basic["dep_tasks"] = ["ods_initalization_sqoop_v2"]
    basic["comment"] = ""
    # 任务名
    basic["task_code"] = task_code
    basic["task_type"] = "PythonJob"

    # 文件夹
    # basic['folder_id'] = 951
    basic['folder_id'] = "1107"

    parms['basic'] = copy.deepcopy(basic)

    dev_url = 'http://dayu.souche-inc.com/api/v2/tasks'

    headers = {
        'Cookie': '_security_token_inc=91584515638708100',
        'Host': 'dayu.souche-inc.com',
        'Content-Type': 'application/json;charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
    }
    # task_id = 'ods_transfercar_iplk_log_interface_app_v2_dd'
    # post_commit_url = dev_url + 'jobs/{}/commit'
    # parm = request_parms()
    print(parms)

    commit_post_req = requests.post(dev_url, json.dumps(parms), headers=headers)

    print(commit_post_req.text)
    return commit_post_req.text



if __name__ == '__main__':

    aa = task_inita_ods('sfs_server', 'rm-bp12v172dyfq03vy0.mysql.rds.aliyuncs.com', 'tmp_aa5')

    print(aa)

