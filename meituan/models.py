# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     models
   Description :
   Author :       yu.zhang
   date：          18-6-29
-------------------------------------------------
"""
from client.log import logger
from mongoengine import DynamicDocument
from mongoengine import StringField, ListField, DateTimeField
from datetime import datetime


class Meituan(DynamicDocument):
    url = StringField(default="", required=False)
    category1 = StringField(default="", required=False)
    category2 = StringField(default="", required=False)
    category3 = StringField(default="", required=False)
    name = StringField(default="", required=False)
    avg_star = StringField(default="", required=False)
    avg_price = StringField(default="", required=False)
    address = StringField(default="", required=False)
    phone = StringField(default="", required=False)
    open_time = StringField(default="", required=False)
    extra_info = ListField(default=[], required=False)
    spider_time = DateTimeField(default=datetime.now)
    belong = StringField(default="", required=False)
    lat = StringField(default="", required=False)
    lng = StringField(default="", required=False)

    @classmethod
    def save_info(cls, **payload):
        ins = cls()
        for key, value in payload.items():
            setattr(ins, key, value)
        try:
            ins.save()
        except Exception as e:
            logger.error("insert db error:{}".format(str(e)))
            return
