# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     test_regex
   Description :
   Author :       yu.zhang
   date：          18-6-26
-------------------------------------------------
"""

from unittest import TestCase
import re


class TestUtil(TestCase):
    def test_regex(self):
        list_regex = r'^https{0,}:\/\/.*\.meituan.com\/(meishi|xiuxianyule|jiankangliren|jiehun|qinzi|yundongjianshen|jiazhuang|xuexipeixun|jiaoyupeixun|yiliao|aiche|chongwu)\/.*\/{0,}$'

        data_regex = r'^https{0,}:\/\/.*\.meituan.com\/(meishi|xiuxianyule|jiankangliren|jiehun|qinzi|yundongjianshen|jiazhuang|xuexipeixun|jiaoyupeixun|yiliao|aiche|chongwu)\/[0-9].*\/{0,}$'

        data_urls = [
            "http://www.meituan.com/meishi/5428418/",
            "http://www.meituan.com/xiuxianyule/91725271/",
            "http://bj.meituan.com/jiehun/20198/",
            "http://www.meituan.com/jiankangliren/317700/",
            "http://www.meituan.com/qinzi/317700/",
            "http://www.meituan.com/yundongjianshen/317700/",
            "http://www.meituan.com/jiazhuang/317700/",
            "http://www.meituan.com/xuexipeixun/317700/",
            "http://www.meituan.com/jiaoyupeixun/317700/",
            "http://www.meituan.com/yiliao/317700/",
            "http://www.meituan.com/aiche/317700/",
            "http://www.meituan.com/chongwu/317700/",

        ]

        list_urls = [
            "http://bj.meituan.com/",
            "http://bj.meituan.com/meishi/",
            "http://bj.meituan.com/meishi/c393/",
            "http://bj.meituan.com/meishi/c393/123",
            "http://bj.meituan.com/meishi/c393/123/",
            "http://bj.meituan.com/meishi/c393/123/c321",
            "http://bj.meituan.com/meishi/c393/123/c321/12321",
        ]
        # 1) 判断data_url是否合理
        for data_url in data_urls:
            resp = re.match(data_regex, data_url)
            self.assertIsNotNone(resp)

        for list_url in list_urls:
            resp = re.match(data_regex, list_url)
            self.assertIsNone(resp)

        # 2) 判断list_url是否合理
        for list_url in data_urls:
            resp = re.match(list_regex, list_url)
            self.assertIsNotNone(resp)

        list_urls.pop(0)
        for list_url in list_urls:
            resp = re.match(list_regex, list_url)
            self.assertIsNotNone(resp)