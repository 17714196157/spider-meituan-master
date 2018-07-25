# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     test_util
   Description :
   Author :       yu.zhang
   date：          18-6-28
-------------------------------------------------
"""
from unittest import TestCase
from urllib.parse import urlparse, urlunparse


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


class TestUtil(TestCase):
    def test_parse_url(self):
        """
         测试两种情况

         /meishi
         //www.baidu.com/meishi

         :return:
         """
        a = "/meishi"
        b = "//www.baidu.com/meishi"
        c = "http://www.baidu.com/meishi"
        a = parse_url("http://www.baidu.com", a)
        b = parse_url("http://www.baidu.com", b)
        c = parse_url("http://www.baidu.com", c)
        self.assertEqual(a, "http://www.baidu.com/meishi")
        self.assertEqual(b, "http://www.baidu.com/meishi")
        self.assertEqual(c, "http://www.baidu.com/meishi")
        e = "/meishi/77375132/"
        e = parse_url("http://bj.meituan.com/meishi/c54/", e)
        print(e)