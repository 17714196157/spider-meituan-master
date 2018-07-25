# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     xiuxianyule
   Description :
   Author :       yu.zhang
   date：          18-6-29
-------------------------------------------------
"""
import requests
from client.log import logger

from meituan.entities.abc import Base


class XiuXianYuLe(Base):
    belong = "休闲娱乐"

    def __init__(self, task, spider):
        super().__init__(task, spider)

    def item(self):
        url = self.task["url"]
        payload = requests.post(self.render_js_url, json={
            "url": url,
            "script": "() => {return {state:window.__LEGO_WIDGETS_FALLBACK__}}"
        }).json()

        if payload['code'] == 0:
            return
        result = payload['result']

        try:
            for s in result["state"]:
                if s['name'] == 'lego-widget-play-mt-map':
                    poi_info = s['params']['poiInfo']
                    category1, category2, category3 = [i['title'] for i in poi_info['breadCrumbNavDTOList']]
                    name = poi_info["shopName"]
                    avg_score = poi_info['score']
                    avg_price = poi_info['avgPrice']
                    address = poi_info['address']
                    phone = poi_info['phone']
                    open_time = poi_info['openTime']
                    extra_info = [{"wifi": poi_info['wifi']}]
                    lat, lng = poi_info['lat'], poi_info['lng']

                    resp = {
                        "url": url,
                        "category1": category1[:-2],
                        "category2": category2,
                        "category3": category3,
                        "name": name,
                        "avg_star": str(avg_score / 10),
                        "avg_price": str(avg_price),
                        "address": address,
                        "phone": phone,
                        "open_time": open_time,
                        "extra_info": extra_info,
                        "belong": self.belong,
                        'lat': str(lat),
                        'lng': str(lng)
                    }
                    return resp
        except Exception as e:
            logger.error("url:{}, result:{}".format(self.task['url'], payload))
            logger.exception(e)
            return
