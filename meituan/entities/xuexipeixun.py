# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     xuexipeixun
   Description :
   Author :       yu.zhang
   date：          18-6-29
-------------------------------------------------
"""
import requests
from client.log import logger

from meituan.entities.abc import Base


class XueXiPeiXun(Base):
    belong = "学习培训"

    def __init__(self, task, spider):
        super().__init__(task, spider)

    def item(self):
        url = self.task['url']
        payload = requests.post(self.render_js_url, json={
            "url": url,
            "script": "() => {return {state:window.__LEGO_WIDGETS_FALLBACK__}}"
        }).json()

        if payload['code'] == 0:
            return

        result = payload['result']
        try:
            for s in result["state"]:
                if s['name'] == 'lego-widget-mtpc-shop-sidebar-widgets':
                    map_info = s['params']['mapInfo']
                    shop_info = s['params']['shopInfo']

                    category1, category2, category3 = map_info["cityName"] + "美团", map_info["cityName"] + "学习培训", ""
                    name = map_info["shopName"]
                    avg_score = shop_info['star']
                    avg_price = ""
                    address = shop_info['address']
                    phone = shop_info['phoneNo']
                    open_time = ""
                    extra_info = []
                    lat, lng = map_info["glat"], map_info["glng"]
                    resp = {
                        "url": url,
                        "category1": category1[:-2],
                        "category2": category2,
                        "category3": category3,
                        "name": name,
                        "avg_star": str(avg_score),
                        "avg_price": avg_price,
                        "address": address,
                        "phone": phone,
                        "open_time": open_time,
                        "extra_info": extra_info,
                        "belong": self.belong,
                        "lat": str(lat),
                        "lng": str(lng)
                    }

                    return resp
        except Exception as e:
            logger.error("url:{}, result:{}".format(self.task['url'], payload))
            logger.exception(e)
            return
