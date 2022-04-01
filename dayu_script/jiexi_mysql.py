# encoding: utf-8
"""
@file: jiexi_mysql.py
@version: 1.0
@author: Atlantis
@time: 2020/6/19 9:35
@DESC: 解析mysql建表语句

"""
#!/use/bin/env python
# _*_ coding:utf-8 _*_
import copy, os
import re, csv


# 获取表的列
def tableCloumn():
    filename = r'D:\workspace\CProjects\dbsys.sql'
    # 加r代表不转义
    pos = []
    Efield = []
    i = 0
    table, columnlines2, columnlist, tables, cloumns, cloumn, cloumntype = '', '', [], {}, {}, '', ''
    with open(filename, 'r', encoding='utf-16') as file_to_read:
        while True:
            cloumns = {}
            i = 0
            lines = file_to_read.readline()
            # 整行读取数据
            if not lines:
                return tables
                break
                pass
            #if re.match(r'CREATE TABLE \[dbo\]\.\[T_CUS(.*)', lines, re.I):
            if re.match(r'CREATE TABLE \[dbo\]\.\[(.*)', lines, re.I):
                # if i > 184:
                # 打印字符串打印出来行
                #print(lines)
                # 表
                table1 = re.search(r'\[dbo\]\.\[(.*)', lines, re.I).group(0).replace(']', '').replace('(', '')
                table = table1.replace('[dbo.', '').replace('[', '')

                print("---ccc---")
                print(table)
                while True:
                    i += 1
                    columnlines = file_to_read.readline().lstrip()

                    # columnlist = columnlines.split(' ')
                    #if re.match(r'(.*)PRIMARY(.*)', columnlines, re.I) == None:
                    if re.search(r'PRIMARY', columnlines, re.I) == None:
                        columnlist = columnlines.split()
                        print(columnlist)

                        # columnlines2 = columnlines.replace("CREATE TABLE \\[dbo\\]\\.\\[", "").replace("\\]\\(", "")
                        # print(columnlines2)
                        cloumn = columnlist[0].replace('[', '').replace(']', '')

                        cloumntype = columnlist[1].replace('[', '').replace(']', '')
                        cloumns[cloumn] = cloumntype
                        # print(cloumns)

                    #if re.match(r'(.*)PRIMARY(.*)', columnlines, re.I):
                    if re.search(r'PRIMARY', columnlines, re.I):
                        print("-----PRIMARY-------")
                        print(columnlines)
                        print("______aaaaa_____")
                        print(cloumns)
                        tables[table] = copy.deepcopy(cloumns)
                        #print(tables)

                        break

            # print(lines)
            # p_tmp, E_tmp = [float(i) for i in lines.split()] # 将整行数据分割处理，如果分割符是空格，括号里就不用传入参数，如果是逗号， 则传入‘，'字符。
            # pos.append(p_tmp)  # 添加新读取的数据
            # Efield.append(E_tmp)
            pass
        # pos = np.array(pos) # 将数据从list类型转换为array类型。
        # Efield = np.array(Efield)
        # pass


def tableContent():
    filename = r'D:\workspace\CProjects\dbsys.sql'
    # 加r代表不转义
    table, cloumnConment, columnlist, cloumn = '', '', [], ''
    tables, cloumns, cloumn, key1 = {}, {}, '', ''
    with open(filename, 'r', encoding='utf-16') as file_to_read:
        while True:
            lines = file_to_read.readline()
            # 整行读取数据
            if not lines:
                return tables, cloumns
                break
                pass
            if re.match(r'EXEC sys.sp_addextendedproperty(.*)', lines, re.I):
                if re.match(r'(.*)@level2type=N(.*)', lines, re.I):
                    # print(re.match(r'(.*)@level2type=N(.*)', lines, re.I))
                    columnlist = lines.split(',')
                    cloumnConment = columnlist[1].lstrip().replace('@value=N', '').replace(';', '').replace("'", '').rstrip()

                    table = columnlist[5].replace('@level1name=N', '').replace("'", '')
                    cloumn = columnlist[7].replace('@level2name=N', '').replace("'", '').strip('\r\n')
                    # print(columnlist)
                    key1 = table + '&&' + cloumn
                    # print(key1)
                    cloumns[key1] = cloumnConment
                    # print(table + '&&' + cloumn + '&&' + cloumnConment)
                elif re.match(r'(.*)table(.*)', lines, re.I) and re.search(r'(.*)level2type=N(.*)', lines,re.I) == None:
                    # print(re.search(r'(.*)level2type=N(.*)', lines, re.I))
                    # print(lines)
                    tablelist = lines.split(',')
                    # print(tablelist)
                    cloumnConment = tablelist[1].lstrip().replace('@value=N', '').replace(';', '').replace("'", '').rstrip()
                    table = tablelist[5].replace('@level1name=N', '').replace("'", '').strip('\r\n')
                    tables[table] = cloumnConment
                    #print(table + '&&' + cloumnConment)
            pass

def createFile(sql):
    #path = os.path.abspath(os.path.dirname(os.path.dirname(filepath))) + '\\Task'
    #if not os.path.exists(path):
    #    os.makedirs(path)
    #print(path)
    path = r'D:\workspace\CProjects\ '
    num2 =  '\n'
    with open(path + 'create.sql', 'a', encoding='utf-8') as odsfile:
        odsfile.write(num2)
        odsfile.write(sql)

    #with open(path + '\\' + mysqlschema + '_dl.sql', 'a', encoding='utf-8') as dlfile:
    #    dlfile.write(num2)
    #   dlfile.write(sql2)


def csvFile(column2):
    #path = os.path.abspath(os.path.dirname(os.path.dirname(filepath))) + '\\Task'
    #if not os.path.exists(path):
    #    os.makedirs(path)
    #print(path)
    path = r'D:\workspace\CProjects\ '
    num2 =  '\n'
    with open(path + '1.csv', 'a', encoding='utf-8') as f:
        f_csv = csv.writer(f)
        f_csv.writerows(column2)

if __name__ == '__main__':
    tables = tableCloumn()
    # print(tables)
    tablecoment = tableContent()
    tablecomment = tablecoment[0]
    # print(tablecomment)
    columncomment = tablecoment[1]
    # print(columncomment)
    columncomment1 = ''
    columns, columns2= [], []
    for key, value in tables.items():
        columns = []
        tablecoment1 = tablecomment.get(key, '')
        task_code = 'ods_dbsys_ipls_' + key.lower().replace('-', '_') + '_dd'
        dl_task_code = 'dl_dbsys_ipls_' + key.lower().replace('-', '_') + '_dd'
        createsql = 'CREATE TABLE dl_cyp.' + task_code + '\n(\n'
        createview1 = 'CREATE OR REPLACE VIEW ' + dl_task_code + '\n(\n'
        createview2 = 'SELECT'
        createview = ''
        i = 0
        # columnkeys = [i[0] for i in valuecolumn['columns']]
        for column, cloumntype in value.items():
            i += 1

            cloumntype1 = ''
            if cloumntype.split('(')[0] in ('varchar', 'nvarchar', 'char', 'nchar', 'bit'):
                cloumntype1 = 'STRING'
            elif cloumntype.split('(')[0] in ('int', 'tinyint', 'smallint'):
                cloumntype1 = 'INT'
            elif cloumntype.split('(')[0] == 'datetime':
                cloumntype1 = 'TIMESTAMP'
            else:
                cloumntype1 = cloumntype.upper()

            columns.append(column)
            column1 = key + '&&' + column

            # print(column1)
            columncomment1 = columncomment.get(column1,'')

            columns2.append([key, tablecoment1, column, cloumntype, cloumntype1, columncomment1])


            # print(columncomment1)
            if i == 1:
                createsql += "\t`" + column.lower() + "`   " + cloumntype1 + "    " + "COMMENT '" + columncomment1 + "'"
                createview1 += '\t`' + column.lower() + "`   " + "COMMENT '" + columncomment1 + "'"

                createview2 += '\n\t`' + column.lower() + '`'

            else:
                createsql += ",\n" + "\t`" + column.lower() + "`   " + cloumntype1 + "    " + "COMMENT '" + columncomment1 + "'"
                createview1 += ",\n" + "\t`" + column.lower() + "`   " + "COMMENT '" + columncomment1 + "'"

                createview2 += ',\n\t`' + column.lower() + '`'

        createsql += "\n" + ")" + "\n" + "COMMENT '" + tablecoment1 + "'" \
                     + "\n" + "PARTITIONED BY (ds STRING COMMENT '分区')"

        createsql += '''\nROW FORMAT DELIMITED\nNULL DEFINED AS ""\nSTORED AS orc \nTBLPROPERTIES ("orc.compress"="SNAPPY")'''


        createview = createview1 + ",\n\t ds                COMMENT '分区'\n)\nCOMMENT '" + tablecoment1 \
                     + "'\n\tAS\n" + createview2 + ",\n\tds\n" + "FROM" + "\n\t" + "dl_cyp." + task_code

        createFile(createsql + '\n\n' + createview + '\n')
        print(createsql)
        print(createview)

        # task_code = 'tmp_aa6'
        j = 0
        # if j == 0:
        #    j += 1
        # request_parms(createsql, columns, task_code, key)
        conn_id = '1103'
        source_key = 'hive_dl_cyp'
        dl_folder_id = ''
    csvFile(columns2)
    # commit_post_dl = url.request_parms(createview, conn_id, source_key, task_code, dl_task_code, dl_folder_id)
    # dl_commit = update_url2.request_parms(dl_task_code)
    # dl_task_id = getTaskcode.taskCode(dl_task_code)
    # dl_task_dep = getTaskcode.dep_tasks(dl_task_id, createview, conn_id, source_key, task_code, dl_task_code,
    #                                    dl_folder_id)
    #    break

