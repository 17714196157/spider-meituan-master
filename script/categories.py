# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     categories
   Description :
   Author :       yu.zhang
   date：          18-6-26
-------------------------------------------------
"""

from client.http.http_request import http_request

from lxml import etree

from urllib.parse import urlparse


def get_categories():
    resp = http_request("http://bj.meituan.com/", None, {}, {})
    text = resp.text

    root = etree.HTML(text)
    a = root.xpath('//div[@class="category-nav-container"]//a[@href]')

    # 获取所有的分类
    return [_a.attrib.get("href") for _a in a]


def deal_categories():
    results = ['http://bj.meituan.com/meishi/',
               'http://waimai.meituan.com',
               'http://hotel.meituan.com',
               'http://phoenix.meituan.com/?phx_wake_up_type=mtpc_category&phx_wake_up_source=nav',
               'http://maoyan.com/films?utm_source=meituanweb',
               'http://www.meituan.com/flight/',
               'http://www.meituan.com/train/',
               'http://bj.meituan.com/xiuxianyule/',
               'http://bj.meituan.com/xiuxianyule/c10/',
               'http://bj.meituan.com/shenghuo/',
               'http://bj.meituan.com/jiankangliren/',
               'http://bj.meituan.com/jiankangliren/c74/',
               'http://bj.meituan.com/jiankangliren/c20423/',
               'http://bj.meituan.com/jiehun/', 'http://bj.meituan.com/jiehun/c20198/',
               'http://bj.meituan.com/jiehun/c20210/', 'http://bj.meituan.com/qinzi/',
               'http://bj.meituan.com/qinzi/c20108/', 'http://bj.meituan.com/qinzi/c20045/',
               'http://bj.meituan.com/yundongjianshen/', 'http://bj.meituan.com/yundongjianshen/c20253/',
               'http://bj.meituan.com/jiazhuang/', 'http://bj.meituan.com/jiazhuang/c20182/',
               'http://bj.meituan.com/jiazhuang/c20771/', 'http://bj.meituan.com/jiaoyupeixun/',
               'http://bj.meituan.com/xuexipeixun/c20287/', 'http://bj.meituan.com/yiliao/',
               'http://bj.meituan.com/chongwu/c20691/', 'http://bj.meituan.com/aiche/',
               'http://bj.meituan.com/xiuxianyule/c234/', 'http://bj.meituan.com/xiuxianyule/c230/',
               'http://bj.meituan.com/meishi/', 'http://bj.meituan.com/meishi/', 'http://bj.meituan.com/meishi/c393/',
               'http://bj.meituan.com/meishi/c11/', 'http://bj.meituan.com/meishi/c17/',
               'http://bj.meituan.com/meishi/c40/', 'http://bj.meituan.com/meishi/c36/',
               'http://bj.meituan.com/meishi/c28/', 'http://bj.meituan.com/meishi/c35/',
               'http://bj.meituan.com/meishi/c395/', 'http://bj.meituan.com/meishi/c54/',
               'http://bj.meituan.com/meishi/c20003/', 'http://bj.meituan.com/meishi/c55/',
               'http://bj.meituan.com/meishi/c56/', 'http://bj.meituan.com/meishi/c20004/',
               'http://bj.meituan.com/meishi/c57/', 'http://bj.meituan.com/meishi/c400/',
               'http://bj.meituan.com/meishi/c58/', 'http://bj.meituan.com/meishi/c41/',
               'http://bj.meituan.com/meishi/c60/', 'http://bj.meituan.com/meishi/c62/',
               'http://bj.meituan.com/meishi/c63/', 'http://bj.meituan.com/meishi/c217/',
               'http://bj.meituan.com/meishi/c227/', 'http://bj.meituan.com/meishi/c228/',
               'http://bj.meituan.com/meishi/c229/', 'http://bj.meituan.com/meishi/c232/',
               'http://bj.meituan.com/meishi/c233/', 'http://bj.meituan.com/meishi/c24/',
               'http://bj.meituan.com/meishi/c59/', 'http://waimai.meituan.com', 'http://waimai.meituan.com',
               'http://waimai.meituan.com', 'http://hotel.meituan.com', 'http://hotel.meituan.com',
               'http://hotel.meituan.com/beijing/xj6', 'http://hotel.meituan.com/beijing/xj45',
               'http://hotel.meituan.com/beijing/xj23', 'http://hotel.meituan.com/beijing/xj01',
               'http://phoenix.meituan.com/?phx_wake_up_type=mtpc_category&phx_wake_up_source=hot',
               'http://phoenix.meituan.com/?phx_wake_up_type=mtpc_category&phx_wake_up_source=hot',
               'http://phoenix.meituan.com/shanghai/?phx_wake_up_type=mtpc_category&phx_wake_up_source=shanghai',
               'http://phoenix.meituan.com/chengdu/?phx_wake_up_type=mtpc_category&phx_wake_up_source=chengdu',
               'http://phoenix.meituan.com/beijing/?phx_wake_up_type=mtpc_category&phx_wake_up_source=beijing',
               'http://phoenix.meituan.com/chongqing/?phx_wake_up_type=mtpc_category&phx_wake_up_source=chongqing',
               'http://phoenix.meituan.com/nanjing/?phx_wake_up_type=mtpc_category&phx_wake_up_source=nanjing',
               'http://phoenix.meituan.com/hangzhou/?phx_wake_up_type=mtpc_category&phx_wake_up_source=hangzhou',
               'http://phoenix.meituan.com/guangzhou/?phx_wake_up_type=mtpc_category&phx_wake_up_source=guangzhou',
               'http://phoenix.meituan.com/xian/?phx_wake_up_type=mtpc_category&phx_wake_up_source=xian',
               'http://phoenix.meituan.com/dalian/?phx_wake_up_type=mtpc_category&phx_wake_up_source=dalian',
               'http://www.meituan.com/flight/', 'http://www.meituan.com/flight/', 'http://www.meituan.com/flight/',
               'http://www.meituan.com/iflight/', 'http://www.meituan.com/train/', 'http://www.meituan.com/train/',
               'http://www.meituan.com/train/', 'http://bj.meituan.com/xiuxianyule/',
               'http://bj.meituan.com/xiuxianyule/', 'http://bj.meituan.com/xiuxianyule/c52/',
               'http://bj.meituan.com/xiuxianyule/c112/', 'http://bj.meituan.com/xiuxianyule/c234/',
               'http://bj.meituan.com/xiuxianyule/c230/', 'http://bj.meituan.com/xiuxianyule/c20773/',
               'http://bj.meituan.com/xiuxianyule/c20772/', 'http://bj.meituan.com/xiuxianyule/c20104/',
               'http://bj.meituan.com/xiuxianyule/c218/', 'http://bj.meituan.com/xiuxianyule/c516/',
               'http://bj.meituan.com/xiuxianyule/c20770/', 'http://bj.meituan.com/xiuxianyule/c38/',
               'http://bj.meituan.com/xiuxianyule/c20779/', 'http://bj.meituan.com/xiuxianyule/c20777/',
               'http://bj.meituan.com/xiuxianyule/c219/', 'http://bj.meituan.com/xiuxianyule/c20776/',
               'http://bj.meituan.com/xiuxianyule/c26/', 'http://bj.meituan.com/xiuxianyule/c10/',
               'http://bj.meituan.com/xiuxianyule/c10/', 'http://bj.meituan.com/xiuxianyule/c10/',
               'http://bj.meituan.com/shenghuo/', 'http://bj.meituan.com/shenghuo/',
               'http://bj.meituan.com/shenghuo/c20112/', 'http://bj.meituan.com/shenghuo/c20113/',
               'http://bj.meituan.com/shenghuo/c20454/', 'http://bj.meituan.com/shenghuo/c20453/',
               'http://bj.meituan.com/shenghuo/c20111/', 'http://bj.meituan.com/shenghuo/c20057/',
               'http://bj.meituan.com/shenghuo/c20457/', 'http://bj.meituan.com/shenghuo/c20474/',
               'http://bj.meituan.com/shenghuo/c20456/', 'http://bj.meituan.com/shenghuo/c20459/',
               'http://bj.meituan.com/shenghuo/c20458/', 'http://bj.meituan.com/shenghuo/c20460/',
               'http://bj.meituan.com/shenghuo/c20196/', 'http://bj.meituan.com/shenghuo/c221/',
               'http://bj.meituan.com/shenghuo/c21006/', 'http://bj.meituan.com/shenghuo/c21007/',
               'http://bj.meituan.com/shenghuo/c21113/', 'http://bj.meituan.com/jiankangliren/',
               'http://bj.meituan.com/jiankangliren/', 'http://bj.meituan.com/jiankangliren/c74/',
               'http://bj.meituan.com/jiankangliren/c75/', 'http://bj.meituan.com/jiankangliren/c76/',
               'http://bj.meituan.com/jiankangliren/c20423/', 'http://bj.meituan.com/jiankangliren/c220/',
               'http://bj.meituan.com/jiankangliren/c20422/', 'http://bj.meituan.com/jiankangliren/c20419/',
               'http://bj.meituan.com/jiankangliren/c20421/', 'http://bj.meituan.com/jiankangliren/c20420/',
               'http://bj.meituan.com/jiankangliren/c20418/', 'http://bj.meituan.com/jiehun/',
               'http://bj.meituan.com/jiehun/', 'http://bj.meituan.com/jiehun/c20198/',
               'http://bj.meituan.com/jiehun/c20303/', 'http://bj.meituan.com/jiehun/c20641/',
               'http://bj.meituan.com/jiehun/c20210/', 'http://bj.meituan.com/jiehun/c20201/',
               'http://bj.meituan.com/jiehun/c20199/', 'http://bj.meituan.com/jiehun/c20200/',
               'http://bj.meituan.com/jiehun/c20202/', 'http://bj.meituan.com/jiehun/c20204/',
               'http://bj.meituan.com/jiehun/c20206/', 'http://bj.meituan.com/jiehun/c20205/',
               'http://bj.meituan.com/jiehun/c20207/', 'http://bj.meituan.com/jiehun/c20203/',
               'http://bj.meituan.com/jiehun/c20208/', 'http://bj.meituan.com/qinzi/c20108/',
               'http://bj.meituan.com/qinzi/c20108/', 'http://bj.meituan.com/qinzi/c20514/',
               'http://bj.meituan.com/qinzi/c20782/', 'http://bj.meituan.com/qinzi/c20045/',
               'http://bj.meituan.com/qinzi/c20045/', 'http://bj.meituan.com/qinzi/c20865/',
               'http://bj.meituan.com/qinzi/c20787/', 'http://bj.meituan.com/qinzi/c20789/',
               'http://bj.meituan.com/qinzi/c20790/', 'http://bj.meituan.com/qinzi/c20864/',
               'http://bj.meituan.com/qinzi/c20791/', 'http://bj.meituan.com/qinzi/c398/',
               'http://bj.meituan.com/qinzi/c398/', 'http://bj.meituan.com/qinzi/c20048/',
               'http://bj.meituan.com/qinzi/c20515/', 'http://bj.meituan.com/qinzi/c20783/',
               'http://bj.meituan.com/qinzi/c20784/', 'http://bj.meituan.com/qinzi/c20042/',
               'http://bj.meituan.com/qinzi/c20042/', 'http://bj.meituan.com/qinzi/c20516/',
               'http://bj.meituan.com/qinzi/c20792/', 'http://bj.meituan.com/qinzi/c20793/',
               'http://bj.meituan.com/qinzi/c20794/', 'http://bj.meituan.com/qinzi/c20795/',
               'http://bj.meituan.com/qinzi/c20796/', 'http://bj.meituan.com/qinzi/c20170/',
               'http://bj.meituan.com/qinzi/c20785/', 'http://bj.meituan.com/qinzi/c20171/',
               'http://bj.meituan.com/yundongjianshen/', 'http://bj.meituan.com/yundongjianshen/',
               'http://bj.meituan.com/yundongjianshen/c20253/', 'http://bj.meituan.com/yundongjianshen/c20266/',
               'http://bj.meituan.com/yundongjianshen/c20256/', 'http://bj.meituan.com/yundongjianshen/c20257/',
               'http://bj.meituan.com/yundongjianshen/c20268/', 'http://bj.meituan.com/yundongjianshen/c20270/',
               'http://bj.meituan.com/yundongjianshen/c20258/', 'http://bj.meituan.com/yundongjianshen/c20259/',
               'http://bj.meituan.com/yundongjianshen/c20262/', 'http://bj.meituan.com/yundongjianshen/c20265/',
               'http://bj.meituan.com/yundongjianshen/c20264/', 'http://bj.meituan.com/yundongjianshen/c20260/',
               'http://bj.meituan.com/yundongjianshen/c20261/', 'http://bj.meituan.com/yundongjianshen/c20263/',
               'http://bj.meituan.com/yundongjianshen/c20267/', 'http://bj.meituan.com/yundongjianshen/c20269/',
               'http://bj.meituan.com/yundongjianshen/c20271/', 'http://bj.meituan.com/jiazhuang/c20180/',
               'http://bj.meituan.com/jiazhuang/c20180/', 'http://bj.meituan.com/jiazhuang/c20878/',
               'http://bj.meituan.com/jiazhuang/c20879/', 'http://bj.meituan.com/jiazhuang/c20880/',
               'http://bj.meituan.com/jiazhuang/c20182/', 'http://bj.meituan.com/jiazhuang/c20182/',
               'http://bj.meituan.com/jiazhuang/c20829/', 'http://bj.meituan.com/jiazhuang/c20823/',
               'http://bj.meituan.com/jiazhuang/c20825/', 'http://bj.meituan.com/jiazhuang/c20835/',
               'http://bj.meituan.com/jiazhuang/c20826/', 'http://bj.meituan.com/jiazhuang/c20822/',
               'http://bj.meituan.com/jiazhuang/c20827/', 'http://bj.meituan.com/jiazhuang/c20824/',
               'http://bj.meituan.com/jiazhuang/c20832/', 'http://bj.meituan.com/jiazhuang/c20831/',
               'http://bj.meituan.com/jiazhuang/c20828/', 'http://bj.meituan.com/jiazhuang/c20834/',
               'http://bj.meituan.com/jiazhuang/c20830/', 'http://bj.meituan.com/jiazhuang/c20833/',
               'http://bj.meituan.com/jiazhuang/c20771/', 'http://bj.meituan.com/jiazhuang/c20771/',
               'http://bj.meituan.com/jiazhuang/c20838/', 'http://bj.meituan.com/jiazhuang/c20840/',
               'http://bj.meituan.com/jiazhuang/c20841/', 'http://bj.meituan.com/jiazhuang/c20839/',
               'http://bj.meituan.com/jiazhuang/c20843/', 'http://bj.meituan.com/jiazhuang/c20184/',
               'http://bj.meituan.com/jiazhuang/c20184/', 'http://bj.meituan.com/jiazhuang/c20847/',
               'http://bj.meituan.com/jiazhuang/c20846/', 'http://bj.meituan.com/jiazhuang/c20845/',
               'http://bj.meituan.com/xuexipeixun/c20287/', 'http://bj.meituan.com/xuexipeixun/c20287/',
               'http://bj.meituan.com/xuexipeixun/c20313/', 'http://bj.meituan.com/xuexipeixun/c20314/',
               'http://bj.meituan.com/xuexipeixun/c20315/', 'http://bj.meituan.com/xuexipeixun/c20316/',
               'http://bj.meituan.com/xuexipeixun/c20317/', 'http://bj.meituan.com/xuexipeixun/c20318/',
               'http://bj.meituan.com/xuexipeixun/c20319/', 'http://bj.meituan.com/xuexipeixun/c20291/',
               'http://bj.meituan.com/xuexipeixun/c20291/', 'http://bj.meituan.com/xuexipeixun/c20323/',
               'http://bj.meituan.com/xuexipeixun/c20324/', 'http://bj.meituan.com/xuexipeixun/c20325/',
               'http://bj.meituan.com/xuexipeixun/c20326/', 'http://bj.meituan.com/xuexipeixun/c20622/',
               'http://bj.meituan.com/xuexipeixun/c20623/', 'http://bj.meituan.com/xuexipeixun/c20624/',
               'http://bj.meituan.com/xuexipeixun/c20637/', 'http://bj.meituan.com/xuexipeixun/c20327/',
               'http://bj.meituan.com/xuexipeixun/c20286/', 'http://bj.meituan.com/xuexipeixun/c20286/',
               'http://bj.meituan.com/xuexipeixun/c20306/', 'http://bj.meituan.com/xuexipeixun/c20307/',
               'http://bj.meituan.com/xuexipeixun/c20308/', 'http://bj.meituan.com/xuexipeixun/c20309/',
               'http://bj.meituan.com/xuexipeixun/c20310/', 'http://bj.meituan.com/xuexipeixun/c20311/',
               'http://bj.meituan.com/xuexipeixun/c20620/', 'http://bj.meituan.com/xuexipeixun/c20621/',
               'http://bj.meituan.com/xuexipeixun/c20312/', 'http://bj.meituan.com/xuexipeixun/c20288/',
               'http://bj.meituan.com/xuexipeixun/c20288/', 'http://bj.meituan.com/xuexipeixun/c20320/',
               'http://bj.meituan.com/xuexipeixun/c20321/', 'http://bj.meituan.com/xuexipeixun/c20322/',
               'http://bj.meituan.com/yiliao/', 'http://bj.meituan.com/yiliao/', 'http://bj.meituan.com/yiliao/c20275/',
               'http://bj.meituan.com/yiliao/c20276/', 'http://bj.meituan.com/yiliao/c20277/',
               'http://bj.meituan.com/yiliao/c20278/', 'http://bj.meituan.com/yiliao/c20279/',
               'http://bj.meituan.com/yiliao/c20280/', 'http://bj.meituan.com/aiche/', 'http://bj.meituan.com/aiche/',
               'http://bj.meituan.com/aiche/c20115/', 'http://bj.meituan.com/aiche/c20116/',
               'http://bj.meituan.com/aiche/c20117/', 'http://bj.meituan.com/aiche/c20118/',
               'http://bj.meituan.com/aiche/c20119/', 'http://bj.meituan.com/aiche/c20120/',
               'http://bj.meituan.com/aiche/c20121/', 'http://bj.meituan.com/aiche/c20135/',
               'http://bj.meituan.com/aiche/c20161/', 'http://bj.meituan.com/aiche/c20162/',
               'http://bj.meituan.com/aiche/c20163/', 'http://bj.meituan.com/aiche/c20164/',
               'http://bj.meituan.com/aiche/c20174/', 'http://bj.meituan.com/aiche/c20212/',
               'http://bj.meituan.com/aiche/c20215/', 'http://bj.meituan.com/aiche/c20237/',
               'http://bj.meituan.com/aiche/c20381/', 'http://bj.meituan.com/aiche/c20767/',
               'http://bj.meituan.com/aiche/c20768/', 'http://bj.meituan.com/chongwu/c20691/',
               'http://bj.meituan.com/chongwu/c20691/', 'http://bj.meituan.com/chongwu/c25147/',
               'http://bj.meituan.com/chongwu/c25148/', 'http://bj.meituan.com/xiuxianyule/',
               'http://bj.meituan.com/xiuxianyule/', 'http://bj.meituan.com/xiuxianyule/c10/',
               'http://bj.meituan.com/xiuxianyule/c234/', 'http://bj.meituan.com/xiuxianyule/c230/',
               'http://bj.meituan.com/xiuxianyule/c38/', 'http://bj.meituan.com/xiuxianyule/c20770/',
               'http://bj.meituan.com/xiuxianyule/c20104/', 'http://bj.meituan.com/xiuxianyule/c218/',
               'http://bj.meituan.com/xiuxianyule/c20777/', 'http://bj.meituan.com/xiuxianyule/c516/',
               'http://bj.meituan.com/xiuxianyule/c20776/', 'http://bj.meituan.com/xiuxianyule/c20773/',
               'http://bj.meituan.com/xiuxianyule/c219/', 'http://bj.meituan.com/xiuxianyule/c20779/',
               'http://bj.meituan.com/xiuxianyule/c26/']

    categories = set()
    for result in results:
        parse = urlparse(result)
        path = parse.path
        if not path:
            pass
        try:
            categories.add(path.split('/')[1])
        except IndexError:
            pass
    return categories



if __name__ == '__main__':
    resp = deal_categories()
    print(resp)
