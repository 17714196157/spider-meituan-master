# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     spider_meituan
   Description :
   Author :       yu.zhang
   date：          18-6-26
-------------------------------------------------
"""

from meituan.meituan import MeiTuanSpider
from meituan import settings

if __name__ == '__main__':
    meituan = MeiTuanSpider()
    meituan.config.from_object(settings)
    meituan.run()
