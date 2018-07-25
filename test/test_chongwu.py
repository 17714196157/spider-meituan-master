# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     test_chongwu
   Description :
   Author :       yu.zhang
   date：          18-7-4
-------------------------------------------------
"""
from pprint import pprint
from unittest import TestCase

from meituan.entities.chongwu import ChongWu


class Spider(object):
    config = {
        "RENDER_JS_URL": 'http://127.0.0.1:8000/render/js'
    }


class TestAiChe(TestCase):
    def setUp(self):
        self.spider = Spider()

    def test_aiche(self):
        task = {
            "url": "http://www.meituan.com/chongwu/2846856/",
        }

        aiche = ChongWu(task, self.spider)
        pprint(aiche.item())
