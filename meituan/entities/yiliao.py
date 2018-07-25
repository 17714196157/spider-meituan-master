# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     yiliao
   Description :
   Author :       yu.zhang
   date：          18-6-29
-------------------------------------------------
"""
from meituan.entities.jiankangliren import JianKangLiRen


class YiLiao(JianKangLiRen):
    belong = "医疗"

    def __init__(self, task, spider):
        super().__init__(task, spider)

    def item(self):
        return super(YiLiao, self).item()
