# -*- coding: utf-8 -*-

import requests
from common.instances import celery_instance, logging_instance
from spider.boss import http_headers
from spider.consts import BOSS
from lxml.etree import HTML
from spider.utils.util import crawler_sleep
from urllib.parse import urljoin

logger = logging_instance(__name__)


def crawl_search_keyword(keyword_id: int, keyword: str, city_code: str)->list:
    logger.info("task crawl_search_keyword --keyword:{}--city_code:{}-- start".format(keyword, city_code))
    search_url = BOSS.SEARCH_JOB_URL.format(keyword=keyword, city_code=city_code)
    urls = request_job_list(search_url)
    # TODO: update job detail
    return urls


def request_job_list(url, static_url_list=[])->list:
    """
    请求搜索页，提取job详情url,返回列表
    """
    try:
        crawler_sleep()
        resp = requests.get(url, headers=http_headers())
        items_url, next_url = get_job_items_and_next(resp.text)
        if items_url:
            for each in items_url:
                static_url_list.append(each)
                logger.info("find job url in boss {}".format(each))
        if next_url:
            request_job_list(next_url)
        return static_url_list
    except Exception as e:
        logger.error(e)


def get_job_items_and_next(html: str)->(list, str):
    """
    返回详情页的url列表和下一翻页的url
    :param html:
    :return:
    """
    html = HTML(html)
    url_list = html.xpath("//div[@class='job-list']/ul/li//div[@class='info-primary']//a/@href")
    if not url_list:
        return None, None
    url_list = [urljoin(BOSS.BASE_URL, each) for each in url_list]
    page_next = html.xpath("//div[@class='page']/a[last()]/@href")[0]
    if page_next == BOSS.PAGE_STOP_FLAG:
        return url_list, None
    else:
        return url_list, urljoin(BOSS.BASE_URL, page_next)


if __name__ == "__main__":
    urls = crawl_search_keyword(1, "python", "101010100")
    print(len(urls))