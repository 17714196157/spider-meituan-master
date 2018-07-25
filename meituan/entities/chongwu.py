# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     chongwu
   Description :
   Author :       yu.zhang
   date：          18-6-29
-------------------------------------------------
"""
from meituan.entities.jiankangliren import JianKangLiRen


class ChongWu(JianKangLiRen):
    belong = "宠物"

    def __init__(self, task, spider):
        super().__init__(task, spider)

    def item(self):
        return super(ChongWu, self).item()
