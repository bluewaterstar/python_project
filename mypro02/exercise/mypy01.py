# encoding: utf-8
"""
@file: mypy01
@version: 1.0
@author: Atlantis
@time: 2020/4/17 17:53
"""
from datetime import datetime,timedelta
print('Hello World!')
current_month = datetime.today()
# 昨天时间
yesterday_ds = (current_month - timedelta(days=1)).strftime("%Y-%m-%d")
print(current_month)
print(yesterday_ds)


