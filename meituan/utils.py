# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     utils
   Description :
   Author :       yu.zhang
   date：          18-6-25
-------------------------------------------------
"""
import re
from urllib.parse import urlparse, urlunparse


def parse_url(parent_url, url):
    parse = urlparse(url)
    # 表示带上了http以及域名
    if parse.scheme and parse.netloc:
        return url
    par_parse = urlparse(parent_url)
    parse_to_dict = parse._asdict()
    if not parse.scheme:
        # 如果没带http, 则使用parent的,例如//bj.meituan.com/meishi/123321
        parse_to_dict["scheme"] = par_parse.scheme
    if not parse.netloc:
        # 如果没带域名的,则使用parent的,例如/meishi/123321
        parse_to_dict["netloc"] = par_parse.netloc
    return urlunparse([value for _, value in parse_to_dict.items()])


def valid_url(url):
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url) is not None
