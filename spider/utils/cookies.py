# -*- coding: utf-8 -*-

import logging
import random
import time

import requests

from spider import consts
from spider.utils.http_tools import get_proxys


class Cookies(object):
    _cookies = []
    _last_update_time = None
    url = None # 子类重写

    @classmethod
    def refresh_cookies(cls):
        """刷新 cookie """
        proxys = get_proxys()
        cls._cookies = cls._get_cookies_from_proxys(proxys)
        cls._last_update_time = time.time()

    @classmethod
    def get_random_cookies(cls):
        now = time.time()
        # cookie 超时时间
        if len(cls._cookies) == 0 or (now - cls._last_update_time) >= consts.SECONDS_OF_DAY:
            cls.refresh_cookies()
        return random.choice(cls._cookies)

    @classmethod
    def remove_cookies(cls, cookies):
        cls._cookies.remove(cookies)

    @classmethod
    def _get_cookies_from_proxys(cls, proxys, proxy_type='https'):
        logging.info('重新获取 --{}-- cookies !'.format(cls.url))
        logging.info('代理 IP 的数量:{}'.format(len(proxys)))
        cookies = []
        for proxy in proxys:
            try:
                response = requests.get(cls.url, # cls.url 子类重写
                                        proxies={proxy_type: proxy},
                                        allow_redirects=False,
                                        timeout=2)
                if len(response.cookies):
                    cookies.append(response.cookies)
            except:
                pass
        logging.info('--{}--可用 cookies 数量: {}'.format(cls.url, len(cookies)))
        return cookies
