# -*- coding: utf-8 -*-

import requests
from requests.exceptions import RequestException
import random
import json
from common.instances import logging_instance
from json import JSONDecodeError
from retrying import retry
from spider.consts import RETRY_TIMES, STOP_MAX_DELAY, WAIT_FIXED

logger = logging_instance(__name__)


class Proxies(object):

    _proxies = []

    @classmethod
    def refresh_proxies(cls):
        cls._proxies = cls._get_proxies()

    @staticmethod
    @retry(stop_max_attempt_number=RETRY_TIMES, stop_max_delay=STOP_MAX_DELAY,
           wait_fixed=WAIT_FIXED)
    def _get_proxies():
        try:
            r = requests.get("http://123.207.153.235:5051/get_all/")
            if r.status_code == 200:
                return json.loads(r.text)
        except RequestException as e:
            logger.error(e)
            raise e
        except JSONDecodeError as e:
            logger.error(e)
            raise e

    @classmethod
    def get_random_proxy(cls):
        if len(cls._proxies) == 0:
            cls.refresh_proxies()
        return random.choice(cls._proxies)

    @classmethod
    def get_proxies(cls, number=400):
        if len(cls._proxies) == 0:
            cls.refresh_proxies()
        if len(cls._proxies) < number:
            return cls._proxies
        return random.choices(cls._proxies, k=number)

    @classmethod
    def remove_proxy(cls, proxy):
        return cls._proxies.remove(proxy)

