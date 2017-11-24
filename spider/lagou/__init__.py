# -*- coding: utf-8 -*-

from spider.utils.http_tools import generate_http_headers
from spider.utils.cookies import Cookies as BaseCookies
from spider.consts import LAGOU


def http_headers():
    headers = generate_http_headers()
    headers.update({
        'Host': LAGOU.HOST,
        'Referer': LAGOU.BASE_URL,
        'Upgrade-Insecure-Requests': '1'
    })
    return headers


class Cookies(BaseCookies):
    url = LAGOU.BASE_URL