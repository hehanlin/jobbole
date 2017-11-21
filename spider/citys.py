# -*- coding: utf-8 -*-

import requests
from spider.consts import BOSS
from spider.utils.http_tools import generate_http_headers
from lxml import etree
from common.instances import logging_instance
from common.models.citys import Citys
# 全国 1
# 北京 1
# 上海 1
# 深圳 1
# 广州 1
# 杭州 1
# 成都 1
# 南京 1
# 武汉 1
# 西安 1
# 厦门 1
# 长沙 1
# 苏州 1
# 天津 1
# 西安 1
# 重庆 1
# 郑州 1
# 太原 1

logger = logging_instance(__name__)


def update_citys_data():
    Citys.insert_many(rows=crawl_citys_data_from_boss()).execute()


def crawl_citys_data_from_boss():
    try:
        resp = requests.get(BOSS.BASE_URL, headers=generate_http_headers())
        html = etree.HTML(resp.text)
        city_ele = html.xpath("//div[@class='city-box']//ul[@class='show']//li")
        city_datas = [{
            'name': each.xpath("text()")[0],
            'boss_code': each.xpath("@data-val")[0],
            'lagou_code': each.xpath("text()")[0],
            'zhilian_code': each.xpath("text()")[0]
        }  for each in city_ele ]
        return city_datas
    except Exception as e:
        logger.error(e)

if __name__ == "__main__":
    update_citys_data()
