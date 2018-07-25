# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     test_qinzi
   Description :
   Author :       yu.zhang
   date：          18-6-29
-------------------------------------------------
"""
from pprint import pprint
from unittest import TestCase

from meituan.entities.qinzi import QinZi


class Spider(object):
    config = {
        "RENDER_JS_URL": 'http://127.0.0.1:8000/render/js'
    }


class TestQinZi(TestCase):
    def setUp(self):
        self.spider = Spider()

    def test_jklr(self):
        task = {
            "url": "http://www.meituan.com/qinzi/41330858/",
        }

        jklr = QinZi(task, self.spider)
        pprint(jklr.item())
