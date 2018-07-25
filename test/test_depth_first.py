# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     test_depth_first
   Description :
   Author :       yu.zhang
   date：          18-6-28
-------------------------------------------------
"""
import re
from collections import deque
from hashlib import md5

import redis
import requests
from lxml import etree
from urllib.parse import urlparse, urljoin, urlunparse

q = deque()

proxy_meta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
    "host": '115.28.253.245',
    "port": 9020,
    "user": 'H5H22B1742467O8D',
    "pass": '8A992F54C2E993F3',
}

proxies = {
    "http": proxy_meta,
    "https": proxy_meta,
}

r = redis.StrictRedis()


def md5_obj(bs):
    m = md5()
    m.update(bs)
    return m.hexdigest()


KEY = "meituan-depth"


def dupefilter(url):
    md5_result = md5_obj(url.encode())
    return r.sadd(KEY, md5_result)


def parse_url(parent_url, url):
    parse = urlparse(url)
    if parse.scheme and parse.netloc:
        return url
    par_parse = urlparse(parent_url)
    parse_to_dict = parse._asdict()
    if not parse.scheme:
        parse_to_dict["scheme"] = par_parse.scheme
    if not parse.netloc:
        parse_to_dict["netloc"] = par_parse.netloc
    return urlunparse([value for _, value in parse_to_dict.items()])


class DepthFirstSpider(object):
    list_regex = r'^https{0,}:\/\/.*\.meituan.com\/(meishi|xiuxianyule|jiankangliren|jiehun|qinzi|yundongjianshen|jiazhuang|xuexipeixun|jiaoyupeixun|yiliao|aiche|chongwu)\/.*\/{0,}$'
    data_regex = r'^https{0,}:\/\/.*\.meituan.com\/(meishi|xiuxianyule|jiankangliren|jiehun|qinzi|yundongjianshen|jiazhuang|xuexipeixun|jiaoyupeixun|yiliao|aiche|chongwu)\/[0-9].*\/{0,}$'

    def __init__(self, start_url):
        self.count = 0
        self.data_count = 0
        self.start_url = start_url
        r.delete(KEY)
        dupefilter(self.start_url)

    def start_index(self):
        headers = {
            "User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/66.0.3359.139 Safari/537.36',
            'Referer': self.start_url
        }
        response = requests.get(self.start_url, headers=headers, proxies=proxies)
        html = response.text

        if not html:
            raise NotImplementedError

        root = etree.HTML(html)
        url_list = root.xpath('//a/@href')
        for url in url_list:
            # 先过滤
            ok = dupefilter(url)
            if not ok:
                continue
            match = re.match(self.list_regex, url)
            if match:
                self.count += 1
                print("当前爬取count:", self.count)
                print(url)
                payload = {
                    "depth": 1,
                    "father": self.start_url,
                    "url": url
                }
                q.append(payload)

    def crawl(self):
        while True:
            # 获取一个url
            payload = q.popleft()
            depth = payload['depth']
            father = payload['father']
            pre_url = payload['url']
            if depth > 50:
                return
            headers = {
                "User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
                'Referer': father
            }
            try:
                response = requests.get(pre_url, headers=headers, proxies=proxies, timeout=5)
            except Exception:
                continue
            html = response.text
            if not html:
                # 表示获取失败
                print("获取失败了")
                continue
            root = etree.HTML(html)
            url_list = root.xpath('//a/@href')
            for url in url_list:
                # 有可能相对路径，开始补齐
                url = parse_url(pre_url, url)
                # 先过滤
                ok = dupefilter(url)
                if not ok:
                    # print("过滤掉了:", pre_url, url, type(ok))
                    continue
                # 如果是list url
                match_list = re.match(self.list_regex, url)
                if match_list:
                    payload = {
                        "depth": depth + 1,
                        "father": pre_url,
                        "url": url
                    }
                    q.append(payload)

            print("当前队列的总数", len(q))


if __name__ == '__main__':
    s = DepthFirstSpider("http://bj.meituan.com")
    s.start_index()
    s.crawl()
