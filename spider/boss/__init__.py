# -*- coding: utf-8 -*-

from spider.utils.http_tools import generate_http_headers
from spider.utils.cookies import Cookies as BaseCookies
from spider.consts import BOSS


def http_headers():
    headers = generate_http_headers()
    headers.update({
        'Host': 'www.zhipin.com',
        'Referer': 'http://www.zhipin.com',
        'Upgrade-Insecure-Requests': '1'
    })
    return headers


class Cookies(BaseCookies):
    url = BOSS.BASE_URL

