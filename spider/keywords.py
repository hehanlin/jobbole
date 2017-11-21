# -*- coding: utf-8 -*-

import requests
from lxml import etree
from spider.utils.http_tools import generate_http_headers
from common.instances import logging_instance
from spider.consts import BOSS, LAGOU
from common.sqlalchemy.keywords import Keywords as KeywordsModel

logger = logging_instance(__name__)


def update_keywords_data():
    keywords = set(
        crawl_boss_keywords() + crawl_lagou_keywords()
    )
    keywords = [
        {'keyword': each} for each in keywords
    ]
    KeywordsModel.add_many(keywords)


def crawl_lagou_keywords()->list:
    try:
        resp = requests.get(LAGOU.BASE_URL, headers=generate_http_headers())
        html = etree.HTML(resp.text)
        keywords = html.xpath("//div[@class='mainNavs']//a/text()")
        return keywords
    except Exception as e:
        logger.error(e)


def crawl_boss_keywords()->list:
    try:
        resp = requests.get(BOSS.BASE_URL, headers=generate_http_headers())
        html = etree.HTML(resp.text)
        keywords = html.xpath("//div[@class='menu-sub']//a/text()")
        return keywords
    except Exception as e:
        logger.error(e)

if __name__ == "__main__":
    print(crawl_boss_keywords()+crawl_lagou_keywords())
    update_keywords_data()
