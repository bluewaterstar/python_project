# encoding: utf-8
"""
@file: getTaskcode
@version: 1.0
@author: Atlantis
@time: 2020/5/14 14:55
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')
import requests, json
import copy, os


def taskCode(task_code):
    dev_url = 'http://dayu.souche-inc.com/api/v2/tasks/{}/search'.format(task_code)


    headers = {
        'Cookie': '_security_token_inc=91584515638708100',
        'Host': 'dayu.souche-inc.com',
        'Content-Type': 'application/json;charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
    }

    data = {
        '_security_token_inc': '91584515638708100',
        'isDingDing': 'false',
        'tracknick': '15711314694'
    }

    s = requests.Session()

    r = s.get(url=dev_url, params=data, headers=headers)

    j = json.loads(r.text)

    print(j)

    a = j["data"][0]
    task_id = a["task_id"]

    return task_id


def dep_tasks(task_id, sql, conn_id, source_key, dep_tasks, task_code, folder_id):
    parms, config, basic = {}, {}, {}

    parms["task_id"] = task_id

    #config["sql"] = "select 1"
    config["sql"] = sql
    #config["conn_id"] = "1090"
    config["conn_id"] = conn_id
    #config["source_key"] = "hive_dl_ycgj"
    config["source_key"] = source_key

    parms["config"] = copy.deepcopy(config)

    basic["app_id"] = "33"
    basic["app_name"] = "数据湖"
    dep_tasks1 = dep_tasks
    #依赖
    basic["dep_tasks"] = [dep_tasks1]
    basic["comment"] = ""
    #任务名
    basic["task_code"] = task_code
    basic["task_type"] = "HiveJob"

    #文件夹
    #basic['folder_id'] = 951
    basic['folder_id'] = folder_id

    parms['basic'] = copy.deepcopy(basic)


    #dev_url = 'http://dayu.souche-inc.com/api/v2/tasks'

    headers = {
        'Cookie': '_security_token_inc=91584515638708100',
        'Host': 'dayu.souche-inc.com',
        'Content-Type': 'application/json;charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
    }
    #task_id = 'ods_transfercar_iplk_log_interface_app_v2_dd'
    #post_commit_url = dev_url + 'jobs/{}/commit'
    #parm = request_parms()
    print(parms)

    dev_url2 = 'http://dayu.souche-inc.com/api/v2/tasks/{}'.format(task_id)

    commit_post_req = requests.post(dev_url2, json.dumps(parms), headers=headers)
    print(commit_post_req.text)

    return commit_post_req


if __name__ == '__main__':
    task_code = 'ods_4sagent_iplm_broker_account_dd'
    a = taskCode(task_code)

