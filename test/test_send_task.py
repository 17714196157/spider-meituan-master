# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     test_send_task
   Description :
   Author :       yu.zhang
   date：          18-7-3
-------------------------------------------------
"""
import requests

payload = {
    "policy": "meituan-v2",
    "site_name": "meituan",
    "depth": 50,
    "father": "https://nj.meituan.com/",
    "type": "list",
    "stat": 0,
    "url": "https://nj.meituan.com/",
    "start_url": 1
}
headers = {
    "access-token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1NjIwNTgxNjYsImlhdCI6MTUzMDUyMDM2NiwiaXNzIjoiY2hlbmd3ZWkiLCJwdWJsaWNfaWQiOiJmZjk5NjgwNC1jYzliLTRjMTUtOTllZS01OGFmNzI3YzVmNjEifQ.bWiciN8MVTELJGBTXA6nHcqPu_W4dNhiFiGbpk_Ug6E"
}
resp = requests.post("http://47.98.36.72:12345/spider/task", json=payload, headers=headers).json()
print(resp)
