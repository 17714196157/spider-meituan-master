# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     test_jiehun
   Description :
   Author :       yu.zhang
   date：          18-6-29
-------------------------------------------------
"""
from pprint import pprint
from unittest import TestCase

from meituan.entities.jiehun import JieHun


class Spider(object):
    config = {
        "RENDER_JS_URL": 'http://127.0.0.1:8000/render/js'
    }


class TestJieHun(TestCase):
    def setUp(self):
        self.spider = Spider()

    def test_jiehun(self):
        task = {
            "url": "http://www.meituan.com/jiehun/164236110/"
        }
        jiehun = JieHun(task, self.spider)
        pprint(jiehun.item())
