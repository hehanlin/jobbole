# -*- coding: utf-8 -*-

from spider.utils.http_tools import generate_http_headers
from spider.utils.cookies import Cookies as BaseCookies
from spider.consts import BOSS
from spider.boss.jobs import crawl_search_keyword
from common.sqlalchemy.keywords import Keywords as KeywordsModel
from common.sqlalchemy.citys import Citys as CitysModel
from common.instances import logging_instance

logger = logging_instance(__name__)


def http_headers():
    headers = generate_http_headers()
    headers.update({
        'Host': BOSS.HOST,
        'Referer':BOSS.BASE_URL,
        'Upgrade-Insecure-Requests': '1'
    })
    return headers


class Cookies(BaseCookies):
    url = BOSS.BASE_URL


def crawl_start():
    logger.info("boss crawler start ...")
    keywords = KeywordsModel.list()
    citys = CitysModel.list()
    for each in keywords:
        for city in citys:
            crawl_search_keyword(each.id, each.keyword, city.boss_code)
