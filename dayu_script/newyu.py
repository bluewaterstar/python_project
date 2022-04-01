import sys
sys.stdout.reconfigure(encoding='utf-8')
import requests, json

import copy, os

import copy,os



def taskCode(task_code):
    #dev_url = 'https://dayuxdev-api.souche-inc.com/v1/jobs/4Jz0XSDniO1DMujT'
    #dev_url = 'https://dayuxdev-api.souche-inc.com/v1/jobs?nameKeyword={}&pageSize=999'.format(task_code)
    dev_url = 'https://dayux-server-api.souche-inc.com/v1/jobs?nameKeyword={}&pageSize=999'.format(task_code)
    headers = {
        "cookie": "isDingDing=true; tracknick=15711314694; _security_token_inc=91592206519586356; JSESSIONID=DC6BC4D97F229B6347648D75A8A64698",
        "origin": "https://dayux.souche-inc.com",
        "referer": "https://dayux.souche-inc.com/",
        "content-type": "application/json;charset=UTF-8",
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
    }

    s = requests.Session()

    r = s.get(url=dev_url, headers=headers)

    j = json.loads(r.text)

    aa1 = j['data']['items'][0]

    aa2 = aa1['instance']['code']

    print(aa2)
    return aa2


#获取新大禹sql
def tasksql(task_id):
    #task_code = 'ods_card_credit_ipkm_loan_credit_report_dd'
    dev_url = 'https://dayux-server-api.souche-inc.com/v1/jobs/{}'.format(task_id)
    headers = {
        "cookie": "isDingDing=true; tracknick=15711314694; _security_token_inc=91592206519586356; JSESSIONID=DC6BC4D97F229B6347648D75A8A64698",
        "origin": "https://dayux.souche-inc.com",
        "referer": "https://dayux.souche-inc.com/",
        "content-type": "application/json;charset=UTF-8",
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
    }

    s = requests.Session()

    r = s.get(url=dev_url, headers=headers)

    j = json.loads(r.text)
    print(j)

    j1 = j['data']['version']['content']['sql']

    #j2 = j1["data"]["config"]["sql"]

    print(j1)
    return j1





##新建任务
def task1(task_code, file_id, sql, hive_conn_id):
    parms, instance, version, content = {}, {}, {}, {}
    #task_code ="ods_finance_car_lease_v3_ipku_fcl_repay_info_mapper_dd"

    instance["name"] = task_code
    instance["jobType"] = "HIVE_SQL"
    instance["folderCode"] = file_id
    content["sql"] = sql
    content["datasourceKey"] = hive_conn_id
    #parms["retry_times"] = null
    version["content"] = copy.deepcopy(content)

    #parms["verify_sql"] = null
    parms["instance"] = copy.deepcopy(instance)
    parms["version"] = copy.deepcopy(version)
    parms["outputs"] = []
    #parms["expect_time"] = null
    parms["inputs"] = []

    dev_url = 'https://dayux-server-api.souche-inc.com/v1/jobs'


    headers = {
        "cookie": "isDingDing=true; tracknick=15711314694; _security_token_inc=91592206519586356; JSESSIONID=DC6BC4D97F229B6347648D75A8A64698",
        "origin": "https://dayux.souche-inc.com",
        "referer": "https://dayux.souche-inc.com/",
        "content-type": "application/json;charset=UTF-8",
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
    }

    dev_url2 = 'http://dayu.souche-inc.com/api/v2/tasks/22333/records'

    commit_post_req = requests.post(dev_url, json.dumps(parms), headers=headers)
    print(commit_post_req.text)

    return commit_post_req.text


##更新任务
def update_task1(task_id, parent_task_id, parent_task_code, task_code, file_id, sql, hive_conn):

    dev_url = 'https://dayux-server-api.souche-inc.com/v1/jobs'

    parms, instance, version, content, input1,outputs = {}, {}, {}, {}, {},{}
    # task_code ="ods_finance_car_lease_v3_ipku_fcl_repay_info_mapper_dd"

    instance["code"] = task_id

    instance["name"] = task_code
    instance["jobType"] = "HIVE_SQL"
    instance["folderCode"] = file_id
    instance["description"] = "HIVE_SQL"
    content["sql"] = sql
    content["datasourceKey"] = hive_conn
    # parms["retry_times"] = null
    version["config"] = {
        "jobParameters": "yesterday=${yyyy-MM-dd} yesterday_1=${yyyy-MM-dd-1} yesterday_30=${yyyy-MM-dd-30} week_in_year=${w} days_2_ago_ds=${yyyy-MM-dd-1} days_30_ago_ds=${yyyy-MM-dd-29} days_60_ago_ds=${yyyy-MM-dd-59} days_8_ago_ds=${yyyy-MM-dd-7} days_90_ago_ds=${yyyy-MM-dd-89} yesterday|delta(-1)=${yyyy-MM-dd-1}"
    }
    version["content"] = copy.deepcopy(content)
    version["scheduleType"] = "DAY"
    #version["startDate"] = "2020-05-23"
    #version["endDate"] = "2099-05-23"
    version["startTime"] = "01:00:00"
    version["endTime"] = "01:00:00"
    version["crontab"] = "0 0 1 * * ?"
    # parms["verify_sql"] = null
    parms["instance"] = copy.deepcopy(instance)
    parms["version"] = copy.deepcopy(version)
    parms["outputs"] = []
    # parms["expect_time"] = null
    input1["parentJobCode"] = parent_task_id
    input1["jobCode"] = task_id
    input1["inputName"] = parent_task_code
    outputs["outputName"] = task_code
    outputs["tableName"] = task_code
    outputs["jobCode"] = task_id
    parms["outputs"] = [outputs]
    parms["inputs"] = [input1]


    headers = {
        "cookie": "isDingDing=true; tracknick=15711314694; _security_token_inc=91592206519586356; JSESSIONID=DC6BC4D97F229B6347648D75A8A64698",
        "origin": "https://dayux.souche-inc.com",
        "referer": "https://dayux.souche-inc.com/",
        "content-type": "application/json;charset=UTF-8",
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
    }

    dev_url2 = 'http://dayu.souche-inc.com/api/v2/tasks/22333/records'

    commit_post_req = requests.post(dev_url, json.dumps(parms), headers=headers)
    print(commit_post_req.text)

    return commit_post_req.text


##提交任务
def commit_task(task_id):

    dev_url = 'https://dayux-server-api.souche-inc.com/v1/jobs/commit'

    parms, instance, version, content, input1 = {}, {}, {}, {}, {}


    parms["comment"] = ""

    parms["code"] = task_id



    headers = {
        "cookie": "isDingDing=true; tracknick=15711314694; _security_token_inc=91592206519586356; JSESSIONID=DC6BC4D97F229B6347648D75A8A64698",
        "origin": "https://dayux.souche-inc.com",
        "referer": "https://dayux.souche-inc.com/",
        "content-type": "application/json;charset=UTF-8",
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
    }

    dev_url2 = 'http://dayu.souche-inc.com/api/v2/tasks/22333/records'

    commit_post_req = requests.post(dev_url, json.dumps(parms), headers=headers)
    print(commit_post_req.text)

    return commit_post_req.text


#stg创建任务
def stg_task1(task_code):
    parms, instance, version, content = {}, {}, {}, {}
    #task_code ="ods_finance_car_lease_v3_ipku_fcl_repay_info_mapper_dd"

    instance["name"] = task_code
    instance["jobType"] = "VIRTUAL"
    instance["folderCode"] = 'vtc3CXhetE'
    content["code"] = "select 1"
    #parms["retry_times"] = null
    version["content"] = copy.deepcopy(content)

    #parms["verify_sql"] = null
    parms["instance"] = copy.deepcopy(instance)
    parms["version"] = copy.deepcopy(version)
    parms["outputs"] = []
    #parms["expect_time"] = null
    parms["inputs"] = []

    dev_url = 'https://dayux-server-api.souche-inc.com/v1/jobs'


    headers = {
        "cookie": "isDingDing=true; tracknick=15711314694; _security_token_inc=91592206519586356; JSESSIONID=DC6BC4D97F229B6347648D75A8A64698",
        "origin": "https://dayux.souche-inc.com",
        "referer": "https://dayux.souche-inc.com/",
        "content-type": "application/json;charset=UTF-8",
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
    }

    dev_url2 = 'http://dayu.souche-inc.com/api/v2/tasks/22333/records'

    commit_post_req = requests.post(dev_url, json.dumps(parms), headers=headers)
    print(commit_post_req.text)

    return commit_post_req.text

##更新任务
def stg_update_task1(task_id, task_code):

    dev_url = 'https://dayux-server-api.souche-inc.com/v1/jobs'

    parms, instance, version, content, input1, outputs = {}, {}, {}, {}, {},{}
    # task_code ="ods_finance_car_lease_v3_ipku_fcl_repay_info_mapper_dd"

    instance["code"] = task_id

    instance["name"] = task_code
    instance["jobType"] = "VIRTUAL"
    instance["folderCode"] = "vtc3CXhetE"
    instance["description"] = "HIVE_SQL"
    content["sql"] = "select 1"
    # parms["retry_times"] = null
    version["config"] = {
        "jobParameters": "yesterday=${yyyy-MM-dd} yesterday_1=${yyyy-MM-dd-1} yesterday_30=${yyyy-MM-dd-30} week_in_year=${w} days_2_ago_ds=${yyyy-MM-dd-1} days_30_ago_ds=${yyyy-MM-dd-29} days_60_ago_ds=${yyyy-MM-dd-59} days_8_ago_ds=${yyyy-MM-dd-7} days_90_ago_ds=${yyyy-MM-dd-89} yesterday|delta(-1)=${yyyy-MM-dd-1}"
    }
    version["content"] = copy.deepcopy(content)
    version["scheduleType"] = "DAY"
    #version["startDate"] = "2020-05-23"
    #version["endDate"] = "2099-05-23"
    version["startTime"] = "00:00:00"
    version["endTime"] = "00:00:00"
    version["crontab"] = ""
    # parms["verify_sql"] = null
    parms["instance"] = copy.deepcopy(instance)
    parms["version"] = copy.deepcopy(version)
    parms["outputs"] = []
    input1["parentJobCode"] = "3xsmi88TQtZJEdkV"
    input1["jobCode"] = task_id
    input1["inputName"] = "replace_stg_binlog_view"
    outputs["outputName"] = task_code
    outputs["tableName"] = task_code
    outputs["jobCode"] = task_id
    parms["outputs"] = [outputs]
    parms["inputs"] = [input1]


    headers = {
        "cookie": "isDingDing=true; tracknick=15711314694; _security_token_inc=91592206519586356; JSESSIONID=DC6BC4D97F229B6347648D75A8A64698",
        "origin": "https://dayux.souche-inc.com",
        "referer": "https://dayux.souche-inc.com/",
        "content-type": "application/json;charset=UTF-8",
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
    }

    dev_url2 = 'http://dayu.souche-inc.com/api/v2/tasks/22333/records'

    commit_post_req = requests.post(dev_url, json.dumps(parms), headers=headers)
    print(commit_post_req.text)

    return commit_post_req.text


def flush_task1(task_code):
    parms, instance, version, content = {}, {}, {}, {}

    task_id = taskCode(task_code)
    #parms["verify_sql"] = null
    parms["startDate"] = "2020-06-29"
    parms["endDate"] = "2020-06-29"
    parms["codes"] = [task_id]
    #parms["expect_time"] = null
    parms["sync"] = "false"
    parms["includeChildren"] = "false"
    parms["stage"] = "PUBLISHED"


    dev_url = 'https://dayux-server-api.souche-inc.com/v1/jobs/flush'


    headers = {
        "cookie": "isDingDing=true; tracknick=15711314694; _security_token_inc=91592206519586356; JSESSIONID=DC6BC4D97F229B6347648D75A8A64698",
        "origin": "https://dayux.souche-inc.com",
        "referer": "https://dayux.souche-inc.com/",
        "content-type": "application/json;charset=UTF-8",
        "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
    }

    dev_url2 = 'http://dayu.souche-inc.com/api/v2/tasks/22333/records'

    commit_post_req = requests.post(dev_url, json.dumps(parms), headers=headers)
    print(commit_post_req.text)

    return commit_post_req.text

if __name__ == '__main__':

    new_ods_file = {'dl_retail': '1OwXzLKata', 'dl_tgc': 'loAHbk9n45', 'dl_cyp': 'eaO4nDRAb2',
                    'dl_czy': 'APaueQNMdD', 'dl_finsv': 'oA4CmngA71', 'dl_ins': 'XJsD6ODKOi',
                    'dl_fin': '6rcDeTRJgb', 'dl_pub': '7NsJbTDbvw', 'dl_cheniu': 'xIKOCzdO0u',
                    'dl_risk': '2eOI6lTkja', 'dl_ycgj': '3pMzaO2OS3', 'dl_scm': 'AZcJP2e8Jh',
                    'dl_dfc': '9nM1Va9p4S', 'dl_inrs': 'GZQH3pYjTz', 'dl_jiaxuan': 'oeK0AeSQBF',
                    'dl_outrs': 'YncJBxZ150'}
    new_dl_file = {'dl_retail': 'wtK2ZFPzu0', 'dl_tgc': 'sSKAV77uFA', 'dl_cyp': 'ULALvKzyWI',
                   'dl_czy': 'DOOIoZUpZJ', 'dl_finsv': 'drQjxqD6aa', 'dl_ins': 'kSOsykzb27',
                   'dl_fin': 'Q3wnDdd8fU', 'dl_pub': 'XKM3pTs5GB', 'dl_cheniu': '1B82qb8Zd1',
                   'dl_risk': 'EXQN6SJCyv', 'dl_ycgj': '5lqEN4k77q', 'dl_scm': '8wuqvi2XuK',
                   'dl_dfc': 'qAucM2a0XI', 'dl_inrs': 'azaWUPUiXf', 'dl_jiaxuan': 'M6gpu5ucOo',
                   'dl_outrs': '3qA1WIvOWr'}

    task_code = 'ods_platform_user_center_iplm_base_opr_logs_dd'
    ods_file_id = 'eaO4nDRAb2'

    aa = ['dl_toolize_finance_product_ipeg_tfp_used_car_info_dd',
          'dl_toolize_finance_product_ipeg_tfp_used_car_pic_audit_dd',
          'dl_toolize_finance_product_ipeg_tfp_used_car_pic_dd',
          'dl_toolize_finance_product_ipeg_tfp_used_complete_dd',
          'dl_toolize_finance_product_ipeg_tfp_used_complete_trace_dd',
          'dl_toolize_finance_product_ipeg_tfp_used_product_apply_dd',
          'dl_toolize_finance_product_ipeg_tfp_used_product_dd',
          'dl_toolize_finance_product_ipeg_tfp_used_product_layered_detail_dd',
          'dl_toolize_finance_product_ipeg_tfp_used_product_trace_dd',
          'dl_toolize_finance_product_ipeg_tfp_used_repurchase_layered_detail_dd',
          'dl_toolize_finance_product_ipeg_tfp_new_car_four_plus_zero_product_param_dd',
          'dl_toolize_finance_product_ipeg_tfp_new_complete_param_dd',
          'dl_toolize_finance_product_ipeg_tfp_new_product_apply_dd',
          'dl_toolize_finance_product_ipeg_tfp_new_product_dd',
          'dl_toolize_finance_product_ipeg_tfp_new_product_layered_detail_dd',
          'dl_toolize_finance_product_ipeg_tfp_new_product_trace_dd'
          ]
    for i in aa:
        task_id = flush_task1(i)