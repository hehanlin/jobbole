# -*- coding: utf-8 -*-

from spider.utils import generate_http_headers

BASE_URL = "http://www.zhipin.com"


def http_headers():
    headers = generate_http_headers().update({
        'Host': 'www.zhipin.com',
        'Referer': 'http://www.zhipin.com/',
        'Upgrade-Insecure-Requests': '1'
    })
    return headers
