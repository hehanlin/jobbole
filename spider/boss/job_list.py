# -*- coding: utf-8 -*-

import requests
from common.instances import celery_instance, logging_instance
from spider.boss import http_headers, Cookies

logger = logging_instance(__name__)


def search_tag(tag: str)->list:
    """
    请求搜索，抓取url列表
    :param tag: 搜索关键字
    :return: url_list: list
    """
    search_url = "http://www.zhipin.com/job_detail/?query={}&scity=100010000&source=2".format(tag)
    try:
        pass
    except:
        pass

