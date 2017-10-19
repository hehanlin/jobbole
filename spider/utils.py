# -*- coding: utf-8 -*-

from spider import consts
from random import choice


def generate_http_headers():
    """
    生成http请求头
    :return: dict
    """
    headers = consts.HTTP_HEADER
    headers['User-Agent'] = choice(consts.USER_AGENT_LIST)
    return headers


