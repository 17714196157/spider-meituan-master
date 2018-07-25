# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     qinzi
   Description :
   Author :       yu.zhang
   date：          18-6-29
-------------------------------------------------
"""
from meituan.entities.jiankangliren import JianKangLiRen


class QinZi(JianKangLiRen):
    belong = "亲子"

    def __init__(self, task, spider):
        super().__init__(task, spider)

    def item(self):
        return super(QinZi, self).item()
