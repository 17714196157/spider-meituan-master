# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     test_xiuxianyule
   Description :
   Author :       yu.zhang
   date：          18-6-29
-------------------------------------------------
"""
from pprint import pprint
from unittest import TestCase

from meituan.entities.xiuxianyule import XiuXianYuLe


class Spider(object):
    config = {
        "RENDER_JS_URL": 'http://127.0.0.1:8000/render/js'
    }


class TestXXYL(TestCase):
    def setUp(self):
        self.spider = Spider()

    def test_xxyl(self):
        task = {
            "url": "http://www.meituan.com/xiuxianyule/165644519/"
        }

        xxyl = XiuXianYuLe(task, self.spider)
        pprint(xxyl.item())
