# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     aiche
   Description :
   Author :       yu.zhang
   date：          18-6-29
-------------------------------------------------
"""
from meituan.entities.jiankangliren import JianKangLiRen


class AiChe(JianKangLiRen):
    belong = "爱车"

    def __init__(self, task, spider):
        super().__init__(task, spider)

    def item(self):
        return super(AiChe, self).item()
