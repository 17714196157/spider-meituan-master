# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     abc
   Description :
   Author :       yu.zhang
   date：          18-6-29
-------------------------------------------------
"""


class Base(object):
    belong = ""

    def __init__(self, task, spider):
        self.task = task
        self.spider = spider

    @property
    def render_js_url(self):
        return self.spider.config["RENDER_JS_URL"]

    def item(self):
        """
        返回抓取的数据
        :return:
        """
        raise NotImplementedError
