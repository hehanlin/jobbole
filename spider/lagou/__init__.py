# -*- coding: utf-8 -*-

from spider.utils.http_tools import generate_http_headers


def http_headers():
    headers = generate_http_headers()
    headers.update({
        'Host': 'www.lagou.com',
        'Referer': 'https://www.lagou.com',
        'Upgrade-Insecure-Requests': '1'
    })
    return headers