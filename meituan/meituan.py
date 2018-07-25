# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     meituan
   Description :
   Author :       yu.zhang
   date：          18-6-26
-------------------------------------------------
"""
import re

from client.crawl import Crawl
from client.http.http_request import get_html
from client.invoke.proxy.proxy import get_proxy
from client.invoke.spider_server.core import spider_server
from client.log import logger
from lxml import etree

from meituan.entities.factory import CategoryFactory
from meituan.models import Meituan
from meituan.utils import parse_url, valid_url


class MeiTuanSpider(Crawl):
    start_url = "https://bj.meituan.com/"

    # list_regex = r'^https{0,}:\/\/.*\.meituan.com\/(meishi|xiuxianyule|jiankangliren|jiehun|qinzi|yundongjianshen|jiazhuang|xuexipeixun|jiaoyupeixun|yiliao|aiche|chongwu)\/.*\/{0,}$'
    data_regex = r'^https{0,}:\/\/.*\.meituan.com\/(meishi|xiuxianyule|jiankangliren|jiehun|qinzi|yundongjianshen|jiazhuang|xuexipeixun|jiaoyupeixun|yiliao|aiche|chongwu|cate)\/[0-9].*\/{0,}$'
    hotel_waimai_regex = r'https{0,}:\/\/(hotel|waimai|phoenix)\.meituan\.com\/{0,}'

    def __init__(self):
        super(MeiTuanSpider, self).__init__()
        self.count = 0

    def deal_forbidden(self, url, headers, proxies):
        count = 0
        try:
            while True:
                html = get_html(url, headers, proxies, cookies={"_lxsdk_s": "%7C%7C0"})
                count += 1
                if count > 3:
                    # 改成返回空字符串，然后以失败任务处理.
                    return ''
                if not html:
                    continue
                root = etree.HTML(html)
                exist = root.xpath('//p[@class="error-word"]')
                logger.info("deal_forbidden:is forbidden:{}".format(exist))
                if exist:
                    continue
                else:
                    return html
        except Exception as e:
            logger.error("deal_forbidden:{}".format(str(e)))

    def get_list(self, task):
        if task['depth'] <= 0:
            return
        pre_url = task["url"]
        # 1. 过滤掉hotel,waimai的
        if re.match(self.hotel_waimai_regex, pre_url):
            return
        logger.info("current url:{}".format(pre_url))
        proxies = get_proxy(self.config)
        headers = {
            "Referer": task['father']
        }
        # html = get_html(pre_url, headers=headers, proxies=proxies)
        html = self.deal_forbidden(pre_url, headers, proxies)
        if not html:
            logger.info("{}:获取失败".format(pre_url))
            spider_server.task.failure(task, [pre_url])
        root = etree.HTML(html)
        try:
            url_list = root.xpath('//a/@href')
        except AttributeError:
            spider_server.task.failure(task, [pre_url])
            return
        urls = set()
        for url in url_list:
            url = parse_url(pre_url, url)
            # 过滤掉hotel,waimai二级域名
            if valid_url(url) and not (re.match(self.hotel_waimai_regex, url)):
                self.count += 1
                urls.add(url)
        # 提交
        spider_server.task.finish(task, [pre_url])
        spider_server.task.new_task(task, urls)
        logger.info("current spider url count:{}".format(self.count))

    def get_data(self, task):
        logger.info('start get data task.')
        url = task['url']
        category = re.match(self.data_regex, url).group(1)
        obj = CategoryFactory.get(category)
        if not obj:
            return
        ins = obj(task, self)
        item = ins.item()
        # 目前返回3种情况, True表示来自cate的，None表示失败,字典表示成功
        if item is True:
            # 表示cate的
            return
        if not item:
            logger.error("获取详情失败")
            spider_server.task.failure(task, [url])
        else:
            Meituan.save_info(**item)
            spider_server.task.finish(task, [url])
