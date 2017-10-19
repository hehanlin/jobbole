# -*- coding: utf-8 -*-
import requests
from lxml import etree
from spider.boss import http_headers, BASE_URL
from requests.exceptions import RequestException
from common.instances import logging_instance
from spider.models import JobTags

logger = logging_instance(__name__)


def crawl_job_tags():
    """
    职位搜索标签
    :return: None
    """
    try:
        resp = requests.get(BASE_URL, headers=http_headers())
        html = etree.HTML(resp.text)
        tag_list = set(
            html.xpath("//div[@class='menu-sub']//a/text()")
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

