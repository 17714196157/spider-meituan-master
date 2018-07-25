# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     meishi
   Description :
   Author :       yu.zhang
   date：          18-6-29
-------------------------------------------------
"""
import requests
from client.log import logger

from meituan.entities.abc import Base


class MeiShi(Base):
    belong = "美食"

    def __init__(self, task, spider):
        super().__init__(task, spider)

    def item(self):
        url = self.task["url"]

        payload = requests.post(self.render_js_url, json={
            "url": url,
            "script": "() => {return {state:window._appState}}"
        }).json()

        if payload["code"] == 0:
            return
        var = payload["result"]

        try:
            # 北京美团,北京美食,北京自助餐

            category1, category2, category3 = var['state']['crumbNav']
            _detail_info = var['state']['detailInfo']
            name = _detail_info['name']
            avg_star = _detail_info['avgScore']
            avg_price = _detail_info['avgPrice']
            address = _detail_info['address']
            phone = _detail_info['phone']
            open_time = _detail_info['openTime']
            extra_info = _detail_info['extraInfos']
            lat, lng = _detail_info['latitude'], _detail_info['longitude']
            return {
                "url": url,
                "category1": category1.get('title', "")[:-2],
                "category2": category2.get('title', ""),
                "category3": category3.get('title', ""),
                "name": name,
                "avg_star": str(avg_star),
                "avg_price": str(avg_price),
                "address": address,
                "phone": phone,
                "open_time": open_time,
                "extra_info": [i['text'] for i in extra_info],
                "lat": str(lat),
                "lng": str(lng),
                "belong": self.belong
            }

        except Exception as e:
            logger.error("url:{}, result:{}".format(self.task['url'], payload))
            logger.exception(e)
            return
