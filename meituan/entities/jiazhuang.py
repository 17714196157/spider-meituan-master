# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     jiazhuang
   Description :
   Author :       yu.zhang
   date：          18-6-29
-------------------------------------------------
"""
from client.http.http_request import get_html
from client.log import logger
from lxml import etree

from meituan.entities.abc import Base


class JiaZhuang(Base):
    belong = "家装"

    def __init__(self, task, spider):
        super().__init__(task, spider)

    def item(self):
        url = self.task['url']
        html = get_html(url, cookies={"_lxsdk_s": "%7C%7C0"})
        if not html:
            return
        root = etree.HTML(html)
        try:
            category1, category2, *category3 = root.xpath('//div[@class="breadcrumb-wrapper"]/ul/li/a/text()')
            name = "".join(root.xpath('//div[@class="shop-name"]/h1/text()'))
            avg_score = "".join(root.xpath('//a[@href="#t-comment"]/text()'))
            avg_price = ""
            address = "".join(root.xpath('//p[@class="shop-contact address"]/text()'))
            phone = "".join(root.xpath('//div[@class="shop-contact telAndQQ"]/span/strong/text()'))
            open_time = "".join(root.xpath('//p[@class="shop-contact"]/text()'))
            extra_info = root.xpath('//div[@class="material-shop__special-services js_dialog-services"]/ul/li/text()')

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
