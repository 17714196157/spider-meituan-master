# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     test_yundongjianshen
   Description :
   Author :       yu.zhang
   date：          18-6-29
-------------------------------------------------
"""
from pprint import pprint
from unittest import TestCase

from meituan.entities.yundongjianshen import YunDongJianShen


class Spider(object):
    config = {
        "RENDER_JS_URL": 'http://127.0.0.1:8000/render/js'
    }


class TestYunDongJianShen(TestCase):
    def setUp(self):
        self.spider = Spider()

    def test_jklr(self):
        task = {
            "url": "http://www.meituan.com/yundongjianshen/1757888/",
        }

        jklr = YunDongJianShen(task, self.spider)
        pprint(jklr.item())