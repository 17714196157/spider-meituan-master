# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     yundongjianshen
   Description :
   Author :       yu.zhang
   date：          18-6-29
-------------------------------------------------
"""
from meituan.entities.xiuxianyule import XiuXianYuLe


class YunDongJianShen(XiuXianYuLe):
    belong = "运动健身"

    def __init__(self, task, spider):
        super().__init__(task, spider)

    def item(self):
        return super(YunDongJianShen, self).item()
