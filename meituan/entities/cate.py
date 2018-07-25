# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     cate
   Description :
   Author :       yu.zhang
   date：          18-7-13
-------------------------------------------------
"""
import re

from client.http.http_request import basic_request
from client.log import logger

from meituan.entities.abc import Base
from meituan.utils import parse_url


class Cate(Base):
    belong = ""

    def __init__(self, task, spider):
        super(Cate, self).__init__(task, spider)

    def item(self):
        from meituan.entities.factory import CategoryFactory
        # 此处处理跳转情况
        try:
            response = basic_request(self.task['url'])
            if not response.history:
                # todo: 表示没有跳转,那么这个就不处理了
                return True
            location = response.history[0].headers.get("Location")
            if location:
                url = parse_url(self.task['url'], location)
                category = re.match(self.spider.data_regex, url).group(1)
                obj = CategoryFactory.get(category)
                # 替换成新的
                self.task['url'] = url
                ins = obj(self.task, self.spider)
                item = ins.item()
                return item

        except Exception as e:
            logger.error("url:{}".format(self.task['url']))
            logger.exception(e)
            return
