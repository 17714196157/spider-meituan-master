# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     jiehun
   Description :
   Author :       yu.zhang
   date：          18-6-29
-------------------------------------------------
"""
from client.http.http_request import get_html
from client.log import logger
from lxml import etree

from meituan.entities.abc import Base


class JieHun(Base):
    belong = "结婚"

    def __init__(self, task, spider):
        super().__init__(task, spider)

    def item(self):
        url = self.task['url']
        html = get_html(url, cookies={"_lxsdk_s": "%7C%7C0"})
        if not html:
            return
        try:
            root = etree.HTML(html)
            category1, category2, *category3 = root.xpath('//span[@class="bread-name"]/text()')
            name = "".join(root.xpath('//div[@class="shop-name"]/h1/text()'))
            avg_score = "".join(root.xpath('//a[@href="#t-comment"]/span[@itemprop="count"]/text()')) + "封点评"
            avg_price = "".join(root.xpath('//em[@class="average"]/text()'))
            address = "".join(root.xpath('//div[@class="fl"]/span[@class="fl"]/text()'))
            phone = "".join(root.xpath('//span[@class="icon-phone"]/text()'))
            open_time = ""
            extra_info = root.xpath('//div[@class="recommend"]/span/text()')

            resp = {
                "url": url,
                "category1": category1[:-2],
                "category2": category2,
                "category3": "" if not category3 else "".join(category3),
                "name": name,
                "avg_star": avg_score,
                "avg_price": avg_price,
                "address": address,
                "phone": phone,
                "open_time": open_time,
                "extra_info": extra_info,
                "belong": self.belong
            }
            return resp
        except Exception as e:
            logger.error("url:{}".format(url))
            logger.exception(e)
            return
