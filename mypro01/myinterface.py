# encoding: utf-8
"""
@file: myinterface
@version: 1.0
@author: Atlantis
@time: 2019/12/30 17:43
"""
import json
import requests
import os
import time

# 业财接口判断是否可以推送
def yecai(itemPurpose,dataTypeCode,accountingPeriod,productCode):
    url_yecai = "http://hyper-ledger.prepub.souche-inc.com/query/Ledger?itemPurpose=%s&dataTypeCode=%s&accountingPeriod=%s&productCode=%s" % (itemPurpose,dataTypeCode,accountingPeriod,productCode)
    print(url_yecai)
    ret = requests.get(url_yecai)
    text = json.loads(ret.text)
    return (text["success"])
    # print (text["data"]["status"])


# 传参数
itemPurpose='00101010'  #款项
dataTypeCode='ys_receivable'    #数据类型
accountingPeriod='2019-02'   #入账期间
productCode='0010101'
# 任务名
tsak_code="store_month_rent_allowance_ledger_tmp_to_mysql"

# 获取是否可以推送状态
result=yecai(itemPurpose,dataTypeCode,accountingPeriod,productCode)

if result=='true':
    # 调大禹任务接口
    url_dayu_s = "http://dayu.souche-inc.com/api/v2/executions"
    headers = {'content-type': 'application/json'}
    requestData = {"task_code": tsak_code}
    ret = requests.post(url_dayu_s, json=requestData, headers=headers)
    # 调用接口成功
    if ret.status_code == 200:
        text = json.loads(ret.text)
        # print (text)
        # 获取任务id
        id = text["data"]["id"]
    else:
        txt = '启动任务失败......'
        os._exit(0)
    # 调大禹任务状态接口
    url_dayu_r = "http://dayu.souche-inc.com/api/v2/executions/%s" % id
    time_s = 0
    status=""
    # 每5s查询一次执行状态，成功则任务结束
    while status != 'true':
        ret = requests.get(url_dayu_r)
        time.sleep(5)
        if ret.status_code == 200:
            text = json.loads(ret.text)
            # print(text)
            status = (text["data"]["status"])
            time_s += 5
            # 任务超过30分钟还未成功，终止任务
            if time_s >= 1800:
                txt = '任务执行超时，已停止任务......'
                os._exit(0)
                break

        else:
            txt = '获取任务执行状态失败......'
            os._exit(0)
else :
    pass

