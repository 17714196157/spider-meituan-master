# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     jiankangliren
   Description :
   Author :       yu.zhang
   date：          18-6-29
-------------------------------------------------
"""
import requests
from client.log import logger

from meituan.entities.abc import Base


class JianKangLiRen(Base):
    belong = "健康丽人"

    def __init__(self, task, spider):
        super().__init__(task, spider)

    def item(self):
        payload = requests.post(self.render_js_url, json={
            "url": self.task['url'],
            "script": "() => {return {state:window.AppData}}"
        }).json()

        if payload['code'] == 0:
            return

        try:
            result = payload['result']
            poi_info = result['state']['poiInfo']
            category1 = poi_info["cityName"]
            category2, category3 = [category1 + i["title"] for i in poi_info["crumbs"]]
            name = poi_info["name"]
            avg_score = poi_info["score"]
            avg_price = poi_info["avgPrice"]
            address = poi_info["address"]
            phone = poi_info["phone"]
            open_time = poi_info["openTime"]
            extra_info = [{"wifi": poi_info["wifi"], "park": poi_info["park"]}]
            lat, lng = poi_info['lat'], poi_info['lng']
            resp = {
                "url": self.task['url'],
                "category1": category1,
                "category2": category2,
                "category3": category3,
                "name": name,
                "avg_star": str(avg_score),
                "avg_price": str(avg_price),
                "address": address,
                "phone": phone,
                "open_time": open_time,
                "extra_info": extra_info,
                "lat": str(lat),
                "lng": str(lng),
                "belong": self.belong
            }
            return resp
        except Exception as e:
            logger.error("url:{}, result:{}".format(self.task['url'], payload))
            logger.exception(e)
            return
