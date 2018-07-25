# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     test_meishi
   Description :
   Author :       yu.zhang
   date：          18-6-27
-------------------------------------------------
"""
from pprint import pprint
from unittest import TestCase

from meituan.entities.meishi import MeiShi


class Spider(object):
    config = {
        "RENDER_JS_URL": 'http://127.0.0.1:8000/render/js'
    }


class TestMeiShi(TestCase):
    def setUp(self):
        self.spider = Spider()

    def test_meishi(self):
        task = {
            "url": "http://www.meituan.com/cate/127095128/"

        }
        meishi = MeiShi(task, self.spider)
        pprint(meishi.item())
