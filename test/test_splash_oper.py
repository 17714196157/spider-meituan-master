# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     test_splash_oper
   Description :
   Author :       yu.zhang
   date：          18-6-27
-------------------------------------------------
"""
import json
from unittest import TestCase

import requests

session = requests.session()

headers = [(key, value) for key, value in {"User-Agent": "aa", "c": "DD"}.items()]


class TestSimpleOperator(TestCase):
    def test_meishi(self):
        'http://httpbin.org/user-agent'
        resp = session.post('http://192.168.1.161:8050/render.html',
                           params={
                               'url': 'http://httpbin.org/user-agent',
                               'http_method': 'GET',
                               'wait': 2,
                               # 'proxy': 'abuyun',
                               'timeout': 20,
                               'cookies': {"_lxsdk_s": "%7C%7C0"},
                                'headers': {"A": "AAA"}
                           })
        print(resp.text)
