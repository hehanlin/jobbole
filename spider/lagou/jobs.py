# -*- coding: utf-8 -*-

import requests
from spider.lagou import http_headers, Cookies
import json
from spider.consts import LAGOU
from urllib.parse import quote_plus
from common.instances import logging_instance
from spider.utils.util import crawler_sleep
from retrying import retry
from spider.consts import RETRY_TIMES, WAIT_FIXED, STOP_MAX_DELAY
from pprint import pprint

logger = logging_instance(__name__)


def generate_xhr_search_headers(keyword, city):
    headers = http_headers()
    headers.update({
        'Origin': 'https://www.lagou.com',
        'Referer': LAGOU.JOB_SEARCH_URL.format(keyword=quote_plus(keyword), city=quote_plus(city)),
        'X-Anit-Forge-Code': '0',
        'X-Anit-Forge-Token': 'None',
        'X-Requested-With': 'XMLHttpRequest'
    })
    return headers


def crawl_search_keyword(keyword_id: int, keyword: str, city_code: str)->list:
    logger.info("task crawl_search_keyword --keyword:{}--city_code:{}-- start".format(keyword, city_code))
    urls = request_job_list(keyword, city_code)
    # TODO: update job detail
    return urls


def request_job_list(keyword: str, city_code: str)->set:
    """
    获得一个关键字的url列表
    :param keyword: 
    :param city_code: 
    :return: 
    """
    # TODO: ip pool and cookie pool
    try:
        crawler_sleep()
        r = requests.post(LAGOU.JOB_JSON_URL,
                          headers=generate_xhr_search_headers(keyword, city_code),
                          data={'first': 'true', 'pn': '1', 'kd': keyword})
        res = json.loads(r.text)['content']['positionResult']
        total_count = int(res['totalCount'])
        page_size = int(res['resultSize'])
        page_count = total_count//page_size
        url_list = []
        for pn in range(1, page_count+1):
            res = request_each_page(pn, keyword, city_code)
            pprint(res)
            if res and len(res) != 0:
                url_list.extend(res)
        return set(url_list)
    except Exception as e:
        logger.error(e)


@retry(stop_max_attempt_number=RETRY_TIMES, stop_max_delay=STOP_MAX_DELAY, wait_fixed=WAIT_FIXED)
def request_each_page(pn: int, keyword: str, city_code: str)->list:
    crawler_sleep()
    cookies = Cookies.get_random_cookies()
    r = requests.post(LAGOU.JOB_JSON_URL,
                      headers=generate_xhr_search_headers(keyword, city_code),
                      data={'first': 'false', 'pn': pn, 'kd': keyword},
                      cookies=cookies)
    res = json.loads(r.text)['content']['positionResult']['result']
    return res


if __name__ == '__main__':
    urls = crawl_search_keyword(1, 'php', '全国')
    pprint(urls)