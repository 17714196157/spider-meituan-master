# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     test_xuexipeixun
   Description :
   Author :       yu.zhang
   date：          18-6-29
-------------------------------------------------
"""
from pprint import pprint
from unittest import TestCase

from meituan.entities.xuexipeixun import XueXiPeiXun


class Spider(object):
    config = {
        "RENDER_JS_URL": 'http://127.0.0.1:8000/render/js'
    }


class TestXXPX(TestCase):
    def setUp(self):
        self.spider = Spider()

    def test_xxpx(self):
        task = {
            "url": "http://www.meituan.com/xuexipeixun/52508190/"
        }
        x = XueXiPeiXun(task, self.spider)
        pprint(x.item())
