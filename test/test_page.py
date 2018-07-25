# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     test_page
   Description :
   Author :       yu.zhang
   date：          18-7-10
-------------------------------------------------
"""

from client.http.http_request import get_html
from lxml import etree

from meituan.utils import parse_url

pre_url = "http://www.meituan.com/s/%E5%A6%88%E5%92%AA%E5%AE%9D%E8%B4%9D%E4%B8%93%E4%B8%9A%E5%84%BF%E7%AB%A5%E6%91%84%E5%BD%B1"
hotel_waimai_regex = r'https{0,}:\/\/(hotel|waimai)\.meituan\.com\/{0,}'


def deal_forbidden(url, headers, proxies):
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
            if exist:
                continue
            else:
                return html
    except:
        return


headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36,'
}
html = deal_forbidden(pre_url, headers, None)

root = etree.HTML(html)
url_list = root.xpath('//a/@href')
for url in url_list:
    url = parse_url(pre_url, url)
    print(url)
