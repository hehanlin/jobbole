# -*- coding: utf-8 -*-

import requests
from requests.exceptions import RequestException
from lxml import etree
from spider.lagou import BASE_URL
from spider.utils import generate_http_headers
from common.instances import logging_instance
from spider.models import JobTags
logger = logging_instance(__name__)


def crawl_job_tags():
    """
        职位搜索标签
        :return: None
        """
    try:
        resp = requests.get(BASE_URL, headers=generate_http_headers())
        html = etree.HTML(resp.text)
        tag_list = set(
            html.xpath("//div[@class='mainNavs']//a/text()")
        )
        JobTags.objects.insert(
            [JobTags(each) for each in tag_list]
        )

    except RequestException as e:
        logger.error(e)
    except Exception as e:
        logger.error(e)


if __name__ == "__main__":
    crawl_job_tags()