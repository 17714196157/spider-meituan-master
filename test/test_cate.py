# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     test_cate
   Description :
   Author :       yu.zhang
   date：          18-7-13
-------------------------------------------------
"""
from pprint import pprint
from unittest import TestCase
from meituan.entities.cate import Cate


class Spider(object):
    config = {
        "RENDER_JS_URL": 'http://127.0.0.1:8000/render/js'
    }
    data_regex = r'^https{0,}:\/\/.*\.meituan.com\/(meishi|xiuxianyule|jiankangliren|jiehun|qinzi|yundongjianshen|jiazhuang|xuexipeixun|jiaoyupeixun|yiliao|aiche|chongwu|cate)\/[0-9].*\/{0,}$'


class TestCate(TestCase):
    def setUp(self):
        self.spider = Spider()

    def test_cate(self):
        """
        "http://www.meituan.com/cate/51238575/",
        "http://www.meituan.com/cate/5193986/",
        "http://www.meituan.com/cate/3250671/",
        "http://www.meituan.com/cate/4999548/",
        :return:
        """

        urls= [
            "http://www.meituan.com/cate/64974650/",
        ]
        for url in urls:
            task = {
                "url": url
            }
            cate = Cate(task, self.spider)
            pprint(cate.item())