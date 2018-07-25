# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     settings
   Description :
   Author :       yu.zhang
   date：          18-6-26
-------------------------------------------------
"""

DEBUG = True

# 用户信息
USERNAME = "zhangyu"
PASSWORD = "qwop!@()"

# policy
POLICY = "meituan-v2"

SITE_NAME = "meituan"

# 每个任务抓取的延时(秒)
SLEEP_TIME = 3

# 去重类型,有set和bloom两种

# 并发数
CONCURRENT = 4

# 深度遍历
DEPTH = 50
# 日志路径
LOG_PATH = "logs/meituan.log"

MONGODB_URL = 'mongodb://127.0.0.1:27017/meituan'

# 服务地址
RENDER_URL = 'http://127.0.0.1:8000'
RENDER_JS_URL = 'http://127.0.0.1:8000/render/js'
