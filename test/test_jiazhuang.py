# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     test_jiazhuang
   Description :
   Author :       yu.zhang
   date：          18-6-29
-------------------------------------------------
"""
from pprint import pprint
from unittest import TestCase

from meituan.entities.jiazhuang import JiaZhuang


class Spider(object):
    config = {
        "RENDER_JS_URL": 'http://127.0.0.1:8000/render/js'
    }


class TestJiazhuang(TestCase):

    def setUp(self):
        self.spider = Spider()

    def test_jiazhuang(self):
        task = {
            "url": "http://www.meituan.com/jiazhuang/81830954/",
        }

        jiazhuang = JiaZhuang(task, self.spider)
        pprint(jiazhuang.item())
