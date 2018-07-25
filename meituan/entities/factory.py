# -*- coding: utf-8 -*-

"""
-------------------------------------------------
   File Name：     factory
   Description :
   Author :       yu.zhang
   date：          18-6-26
-------------------------------------------------
"""
from meituan.entities.aiche import AiChe
from meituan.entities.chongwu import ChongWu
from meituan.entities.jiankangliren import JianKangLiRen
from meituan.entities.jiazhuang import JiaZhuang
from meituan.entities.jiehun import JieHun
from meituan.entities.meishi import MeiShi
from meituan.entities.qinzi import QinZi
from meituan.entities.xiuxianyule import XiuXianYuLe
from meituan.entities.xuexipeixun import XueXiPeiXun
from meituan.entities.yiliao import YiLiao
from meituan.entities.yundongjianshen import YunDongJianShen
from meituan.entities.cate import Cate

category_map = {
    "meishi": MeiShi,
    "xiuxianyule": XiuXianYuLe,
    "jiankangliren": JianKangLiRen,
    "jiehun": JieHun,
    "qinzi": QinZi,
    "yundongjianshen": YunDongJianShen,
    "jiazhuang": JiaZhuang,
    "xuexipeixun": XueXiPeiXun,

    "yiliao": YiLiao,
    "aiche": AiChe,
    "chongwu": ChongWu,
    "cate": Cate
}


class CategoryFactory(object):
    @classmethod
    def get(cls, name):
        return category_map.get(name)
