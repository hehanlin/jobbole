# -*- coding: utf-8 -*-

import logging
import random
import time
import requests
from common.instances import logging_instance
from spider import consts
from spider.utils.proxy import Proxies

logger = logging_instance(__name__)


class Cookies(object):
    _cookies = []
    _last_update_time = None
    url = None # 子类重写

    @classmethod
    def refresh_cookies(cls):
        """刷新 cookie """
        proxys = Proxies.get_proxies(number=40)
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
    def _get_cookies_from_proxys(cls, proxys):
        logger.info('重新获取 --{}-- cookies !'.format(cls.url))
        logger.info('代理 IP 的数量:{}'.format(len(proxys)))
        cookies = []
        for proxy in proxys:
            try:
                logger.info("--%s--尝试用%s获取cookie" % (cls.url, proxy))
                proxies = {
                    'http': 'http://{}'.format(proxy),
                    'https': 'http://{}'.format(proxy)
                }
                response = requests.get(cls.url, # cls.url 子类重写
                                        proxies=proxies,
                                        timeout=5)
                if len(response.cookies):
                    cookies.append(response.cookies)
            except Exception as e:
                logger.error("--%s--获取cookie失败--proxy:%s--%s" % (cls.url, proxy, e))
        logger.info('--{}--可用 cookies 数量: {}'.format(cls.url, len(cookies)))
        return cookies
