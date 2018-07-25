# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     test_block
   Description :
   Author :       yu.zhang
   date：          18-7-3
-------------------------------------------------
"""
import re

from client.http.http_request import get_html
from lxml import etree

from meituan.utils import parse_url

url = "http://bj.meituan.com/meishi/c59/?attrs=65:154"

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

headers = {
    # "Referer": "http://nj.meituan.com/meishi/c62/"
}


def get_page():
    count = 0
    pre_url = "http://bj.meituan.com/xiuxianyule/c38b708/"
    html = get_html(pre_url, headers, proxies, cookies={"_lxsdk_s": "%7C%7C0"})
    root = etree.HTML(html)
    url_list = []
    try:
        url_list = root.xpath('//a/@href')
    except AttributeError:
        print(html)
    list_regex = r'^https{0,}:\/\/.*\.meituan.com\/(meishi|xiuxianyule|jiankangliren|jiehun|qinzi|yundongjianshen|jiazhuang|xuexipeixun|jiaoyupeixun|yiliao|aiche|chongwu)\/.*\/{0,}$'
    urls = []
    for url in url_list:
        url = parse_url(pre_url, url)
        match_list = re.match(list_regex, url)
        if match_list:
            count += 1
            urls.append(url)
            print(url)
    # 提交

    with open('test_block.html', 'w') as f:
        f.write(html)


if __name__ == '__main__':
    get_page()
